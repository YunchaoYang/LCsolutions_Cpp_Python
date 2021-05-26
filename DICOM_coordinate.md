# DICOM医学图像读取涉及到的医学坐标体系

确定患者的位置和躺的方向主要有3个标签:
- (0018, 5100) Patient Position CS: ‘HFS’
- (0020, 0032) Image Position (Patient) DS: [‘-167’, ‘-92’, ‘-28.5’]
- (0020, 0037) Image Orientation (Patient) DS: [‘1’, ‘0’, ‘0’, ‘0’, ‘1’, ‘0’]

![20170529115206179](https://user-images.githubusercontent.com/6526592/119679651-87accb00-be0e-11eb-997b-44ed3ce1faf0.png)

- 世界坐标为double型,范围一般为-1~1.
- 患者坐标为double型.
- 图像坐标为整型.


### 解剖学坐标体

将世界坐标转换为图像坐标时,会涉及到两个参数, origin和spacing:
 -  将需要转换的世界坐标减去origin,再除以spacing就是对应的图像坐标。
 -  对医学图像处理技术来说，最重要的坐标体系是解剖学空间坐标体系。这个坐标体系由三个位面组成，用来描述标准的人体在解剖学上的位置。

* 横断面（The axial plane）：与地面平行，分离头部（Superior）与脚部（Inferior）
* 冠状面（The coronal plane）：与地面垂直，分离人体的前（Anterior）后（Posterior）
* 矢状面（The sagittal plane）：与地面垂直，分离人体的左（Left）右（Right）
 
这个解剖学坐标体系是一个连续的三维空间，在这个空间中，图像被采样。在神经成像中，3D基本上通过解剖轴Anterior-Posterior，Inferior-Superior，Left-Right来定义。

- LPS：（Left，Posterior，Superior）用在Dicom与ITK工具包上
from right to left; from anterior to posterior; from inferior to superior
- RAS：（Right，Anterior，Superior）3D Slicer用RAS
from left to right; from posterior to anterior; from inferior to superior
从根本上来说，这两种坐标轴是等价使用的，有着相同的逻辑，但是有必要知道图像到底引用了哪种坐标轴。

在DICOM标准中通过Image Position(Patient)-（0020,0032）和Image Orientation(Patient)-（0020,0037）两个字段来确定患者Patient的空间定位. 
- Image Position:表示图像的左上角在空间坐标系中的x,y,z坐标，单位是毫米. 
- Image Orientation:表示图像坐标与解剖学坐标体系对应坐标的夹角余弦值.

要说明Image Orientation的含义,要结合解剖学坐标体系和图像坐标体系来说明。Orientation有6个参数。（下边统一以xyz表示图像坐标体系坐标，SIAPLR表示解剖学坐标体系坐标）前三个为x轴分别与LPS的夹角余弦，后3个为y轴与LPS的夹角。如果6个参数里边只有0和1或-1，则图像一定与解剖学坐标体系某个平面平行；如果出现小数，则表示不是完全是3个位面中的一个，会有一定夹角。举例来说明： 
1. Orientation为（1,0,0,0,1,0）表示x轴与L夹角0°，与PS夹角90°；y轴与P夹角0°，与LS夹角90°。表示一个背对着观察者的患者，观察者从上到下看。 
2. Orientation为（1,0,0,0，-1,0）表示x轴与L夹角0°，与PS夹角90°；y轴与P夹角180°，与LS夹角90°。表示一个背对着观察者的患者，观察者从下到上看。 
3. origin为（1,0,0,0,9912，-0.1322）表示x轴与L夹角0°，与PS夹角90°；y轴与L夹角90°，与P夹角7.6°（arccos(0.9912)=7.6°），与S夹角97.6°(arccos(-0.1322)=97.6°)。表示患者躺在病床上，床有点前倾（即身体有些前倾），观察者从患者脚处正着观察患者。该博文有医学图片，帮助更深刻理解。


![world-patient-coordinate](https://user-images.githubusercontent.com/6526592/119681080-be371580-be0f-11eb-841b-82f36cfd1eaa.PNG)

``` cpp 
/* voxel index to point world position */
void IJK2WP(double* origin,
	double* spacing,
	double* orientation,
	int* ijk, double* wp)
{
	// |x|    | x1*spx y1*spy z1*spz dx|   |i|
	// |y|  = | x2*spx y2*spy z2*spz dy| * |j|
	// |z|	  | x3*spx y3*spy z3*spz dz|   |k|
	// |1|    |  0          0      0  1|   |1|
	double orientation_z[3];
	vtkMath::Cross(orientation, orientation + 3, orientation_z);
	vtkMath::Normalize(orientation_z);

	auto matrix = vtkSmartPointer<vtkMatrix4x4>::New();
	matrix->Identity();
	for (int i = 0; i < 3; i++)
	{
		matrix->SetElement(i, 0, orientation[i] * spacing[0]);
		matrix->SetElement(i, 1, orientation[i + 3] * spacing[1]);
		matrix->SetElement(i, 2, orientation_z[i] * spacing[2]);
		matrix->SetElement(i, 3, origin[i]);
	}
	double index[]{ ijk[0],ijk[1] ,ijk[2] ,1 };
	double* temp = matrix->MultiplyDoublePoint(index);
	wp[0] = temp[0];
	wp[1] = temp[1];
	wp[2] = temp[2];
}

/* point world position to voxel index */
void WP2IJK(double* origin,
	double* spacing,
	double* orientation,
	double* wp, int* ijk)
{
	double orientation_z[3];
	vtkMath::Cross(orientation, orientation + 3, orientation_z);
	vtkMath::Normalize(orientation_z);
	auto matrix = vtkSmartPointer<vtkMatrix4x4>::New();
	matrix->Identity();
	for (int i = 0; i < 3; i++)
	{
		matrix->SetElement(i, 0, orientation[i] * spacing[0]);
		matrix->SetElement(i, 1, orientation[i + 3] * spacing[1]);
		matrix->SetElement(i, 2, orientation_z[i] * spacing[2]);
		matrix->SetElement(i, 3, origin[i]);
	}
	auto invertMatrix = vtkSmartPointer<vtkMatrix4x4>::New();
	vtkMatrix4x4::Invert(matrix, invertMatrix);

	double wp4[]{ wp[0],wp[1],wp[2],1 };
	auto temp = invertMatrix->MultiplyDoublePoint(wp4);
	ijk[0] = temp[0];
	ijk[1] = temp[1];
	ijk[2] = temp[2];
}

```

# ITK/VTK：绘制二维及三维DICOM图像分布直方图

使用ITK及VTK读取DICOM图像序列，并绘制图像统计直方图。

``` cpp
#include "vtkDICOMImageReader.h"
#include "vtkRenderWindowInteractor.h"
#include "vtkRenderer.h"
#include "vtkRenderWindow.h"
#include "vtkMarchingCubes.h"
#include "vtkStripper.h"
#include "vtkActor.h"
#include "vtkPolyDataMapper.h"
#include "vtkProperty.h"
#include "vtkCamera.h"
#include "vtkBoxWidget.h"
#include "vtkSmartPointer.h" 
#include "vtkTriangleFilter.h"
#include "vtkMassProperties.h"
#include "vtkSmoothPolyDataFilter.h"
#include "vtkPolyDataNormals.h"
#include "vtkContourFilter.h"
#include "vtkRecursiveDividingCubes.h"
#include "vtkSTLWriter.h"
#include "vtkStringArray.h"


#include <vtkDataObject.h> //
#include <vtkFieldData.h> 
#include <vtkImageAccumulate.h>
#include <vtkImageData.h>
#include <vtkIntArray.h>
#include <vtkBarChartActor.h>
#include <vtkProperty2D.h>
#include <vtkTextProperty.h>
#include <vtkLegendBoxActor.h>
#include <vtkImageActor.h>

#include "itkGDCMImageIO.h"
#include "itkGDCMSeriesFileNames.h"
#include "itkImageSeriesReader.h"
#include "itkImageSeriesWriter.h"
#include <itkImageToVTKImageFilter.h>
#include "itkMedianImageFilter.h"
#include "itkNumericSeriesFileNames.h"

using namespace std;
#define ONE_FRAME 1;
//typedef itk::Image<unsigned char, 2 > ImageType;
#define THREE_DIMENSION 0;//是否绘制三维


//static void CreateImage(ImageType::Pointer image);
using PixelType = int;
#if THREE_DIMENSION
constexpr unsigned int Dimension = 3;
#endif
#if !THREE_DIMENSION
constexpr unsigned int Dimension = 2;
#endif

//初始化待读取序列的格式类型
using ImageType = itk::Image<PixelType, Dimension>;
using ImageType2D = itk::Image<PixelType, 2>;
using ReaderType = itk::ImageSeriesReader<ImageType>;
using ReaderType2D = itk::ImageFileReader<ImageType2D>;


//int main() 
int Histgram()
{
	using ImageIOType = itk::GDCMImageIO;
	using NamesGeneratorType = itk::GDCMSeriesFileNames;

	

	//设置IO，并获取文件名
	ImageIOType::Pointer        gdcmIO = ImageIOType::New();
	

	ReaderType::Pointer reader = ReaderType::New();
	reader->SetImageIO(gdcmIO);

#if THREE_DIMENSION
	/********************************读取dcm序列************************************************/
	string directoryName = "D:\\input";//dcm序列读取地址
	NamesGeneratorType::Pointer namesGenerator = NamesGeneratorType::New();
	namesGenerator->SetInputDirectory(directoryName);

	const ReaderType::FileNamesContainer& filenames =
		namesGenerator->GetInputFileNames();

	std::size_t numberOfFileNames = filenames.size();
	std::cout << numberOfFileNames << std::endl;
	for (unsigned int fni = 0; fni < numberOfFileNames; ++fni)
	{
		std::cout << "filename # " << fni << " = ";
		std::cout << filenames[fni] << std::endl;
	}
	reader->SetFileNames(filenames);
#endif
#
#if !THREE_DIMENSION
/*********************************读取dcm图像***************************************************/
	reader->SetFileName("D:\\file.dcm");//自定义地址
#endif
	
	try
	{
		reader->Update();
	}
	catch (const itk::ExceptionObject& e)
	{
		std::cerr << "exception in file reader " << std::endl;
		std::cerr << e << std::endl;
		return EXIT_FAILURE;
	}

	using MedianFilterType = itk::MedianImageFilter<ImageType, ImageType>;

	MedianFilterType::Pointer filter = MedianFilterType::New();

	ImageType::SizeType indexRadius;

	indexRadius[0] = 2; // radius along x
	indexRadius[1] = 2; // radius along y
#if THREE_DIMENSION
	indexRadius[2] = 1; // radius along z
#endif
	

	filter->SetRadius(indexRadius);

	filter->SetInput(reader->GetOutput());
	filter->Update();

	int x = reader->GetOutput()->GetBufferedRegion().GetSize()[0];
	int y = reader->GetOutput()->GetBufferedRegion().GetSize()[1];
#if THREE_DIMENSION
	int z = reader->GetOutput()->GetBufferedRegion().GetSize()[2];
#endif
	

	int max = 0;
	int min = 0;
	for (int i = 1; i < x; i++) {
		for (int j = 1; j < y; j++) {
#if THREE_DIMENSION
			for (int k = 1; k < z; k++) {
#endif

				ImageType::IndexType id;
				id[0] = i;
				id[1] = j;
#if THREE_DIMENSION
				id[2] = k;
#endif
				
				ImageType::PixelType p = filter->GetOutput()->GetPixel(id);
				if (p > max) {
					max = p;
				}
				else if (p <= min) {
					min = p;
				}
#if THREE_DIMENSION
			}
#endif
		}
	}
	cout << "max is " << max << " min is " << min << endl;
	
	int* hist = new int[max + 1]{0};
	
	for (int i = 1; i < x; i++) {
		for (int j = 1; j < y; j++) {
#if THREE_DIMENSION
			for (int k = 1; k < z; k++) {
#endif

				ImageType::IndexType id;
				id[0] = i;
				id[1] = j;
#if THREE_DIMENSION
				id[2] = k;
#endif

				ImageType::PixelType p = filter->GetOutput()->GetPixel(id);
				
				if (p <= 0) {
					continue;//不统计亮度值小于0的点
				}

				hist[p]++;
#if THREE_DIMENSION
			}
#endif
			

		}
	}

	
#if !THREE_DIMENSION
	typedef itk::ImageToVTKImageFilter<ImageType> ConnectorType;
	ConnectorType::Pointer originalConnector = ConnectorType::New();
	originalConnector->SetInput(filter->GetOutput());
	//originalConnector->UpdateLargestPossibleRegion();
	originalConnector->Update();
#endif
	
	int bins = max - 0;
	//int bins = (max - min) / 10;
	int comps = 1;
	
	vtkSmartPointer<vtkIntArray> frequencies =
		vtkSmartPointer<vtkIntArray>::New();
	frequencies->SetNumberOfComponents(1);
	frequencies->SetArray(hist, max /4, 1);
	
	vtkSmartPointer<vtkDataObject> dataObject =
		vtkSmartPointer<vtkDataObject>::New();
	dataObject->GetFieldData()->AddArray(frequencies);

	vtkSmartPointer<vtkBarChartActor> barChart =
		vtkSmartPointer<vtkBarChartActor>::New();
	barChart->SetInput(dataObject);
	barChart->SetTitle("Histogram");
	barChart->GetPositionCoordinate()->SetValue(0.1, 0.1, 0.0);
	barChart->GetPosition2Coordinate()->SetValue(0.9, 0.9, 0.0);
	barChart->GetProperty()->SetColor(0, 0, 0);
	barChart->GetTitleTextProperty()->SetColor(0, 0, 0);
	barChart->GetLabelTextProperty()->SetColor(0, 0, 0);
	barChart->GetLegendActor()->SetNumberOfEntries(dataObject->GetFieldData()->GetArray(0)->GetNumberOfTuples());
	
	//barChart->SetBarLabel(1, "Count");
	//barChart->LegendVisibilityOff();
	barChart->LabelVisibilityOff();

	double colors[3][3] = {
		{ 1, 0, 0 },
		{ 0, 1, 0 },
		{ 0, 0, 1 } };

	int count = 0;
	for (int i = 0; i < bins; ++i)
	{
		for (int j = 0; j < comps; ++j)
		{
			barChart->SetBarColor(count++, colors[j]); //单通道 红色
		}
	}

	double barView[4] = { 0.0, 0.0, 1.0, 1.0 };

	vtkSmartPointer<vtkRenderer> barRender =
		vtkSmartPointer<vtkRenderer>::New();
	barRender->SetViewport(barView);
	barRender->AddActor(barChart);
	barRender->SetBackground(1.0, 1.0, 1.0);

	vtkSmartPointer<vtkRenderWindow> renderWindow =
		vtkSmartPointer<vtkRenderWindow>::New();
	renderWindow->AddRenderer(barRender);

	renderWindow->SetSize(640*3, 320*3);
	renderWindow->Render();
	renderWindow->SetWindowName("Gray-Image Histogram");

	vtkSmartPointer<vtkRenderWindowInteractor> interactor =
		vtkSmartPointer<vtkRenderWindowInteractor>::New();
	interactor->SetRenderWindow(renderWindow);

	interactor->Initialize();
	interactor->Start();

	return 0;

}
```
