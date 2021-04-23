ITK

### VTK ITK OPENCV，从图像处理的角度来说，哪种用的人多？
ITK是用于图像处理，而VTK用于可视化显示。
ITK更偏重于医学图像处理，而OpenCV偏重于通用图像处理。如果做医学图像处理的话，首选ITK；如果做其他方面的图像处理，还是用OpenCV吧。
如果是做医学图像处理的话建议用ITK+VTK，ITK做底层图像处理算法，VTK做可视化显示，ITK和VTK中间用itkImageToVTKImageFilter ITK/Examples/ItkVtkGlue/itkImageToVTKImageFilter /itkVTKImageToImageFilter ITK: itk::VTKImageToImageFilter< TOutputImage 类进行格式转换。
opencv主要是计算机视觉方向，机器学习方向；itk是图像分割和配准方向

VTK是对OpenGL的一个扩展.OpenGL是开放图形库（英文Open Graphics Library的缩写），它是用于跨平台、跨语言的API。这个接口由近350个不同的函数调用组成，用来绘制从简单的图形比特到复杂的三维景象。它其实没有给出具体的实现方式，而是一个标准，具体实现是各个厂家自己按照这个标准实现的。
，现在非常火的新版的paraview也是基于这些的。 并可以绘制复杂的三维景象。
VTK和Qt简直是好基友。。。提供了很多好用的类和接口，看ParaView的源代码就知道了

ITK的话，纯粹图像分割，配准，统计的，不具有可视化功能。 支持GPU加速，

#### ITK学习笔记

itk::Image 是遵循范型编程思想的类，其类型是由算法行为的类演化而来。ITK 支持任何像素类型和空间维的图像。
```cpp
#include “itkImage.h” //包含头文件
 
//设置好模板参数，并给模板起别名，（两种写法都可）
//typedef itk::Image< unsigned short, 3 > ImageType; 
using ImageType = itk::Image<unsigned short,2>;
 
//创建image数据对象（智能指针写法）
ImageType::Pointer image = ImageType::New( ); 
```
参数1 ：unsigned short: 像素类型，通常为C++基础数据类型，也可自定义，但必须支持 + - * /。
参数2 ： 3 : 图像空间维数， 通常 2维空间 或3维空间。

ITK 中，图像(Image)以一个或多个区域(Region)组合的形式存在。一个区域是图像的一个子集，并有可能是系统中其他类所占有图像的一部分。LargePossibleRegion 是一个完全定义的图像。

BufferedRegion 是内存中图像的一部分。

RequestedRegion 是在对图像进行操作时被滤波器或其他类要求的一部分。

人为创建image后，需要指定图像区域。
```cpp
//一个区域是由两个类来定义的：itk::Index 和 itk::Size 类
// itk::Index ： 像素位置索引（整数）：
// itk::Size  ：图像大小（整数）：
ImageType::IndexType start; //创建itk::Index对象,用来指定图像起点位置
index[0]  = 0 : 代表像素所在行。（对应x坐标）
index[1] = 0：代表像素所在列。（对应y坐标）
index[2] = 0：代表像素所在层（有三维的话，对应z坐标）。
 
ImageType::SizeType size;   //创建itk::Size对象,指定图像各方向大小
size[0] = 200; X 方向大小
size[1] = 200; Y 方向大小
size[2] = 200; Z方向大小
```
最后，这个区域传递给图像对象来定义其延伸和初始地址。SetRegion 方法同时设定了 LargePossibleRegion、BufferedRegion 和 RequestedRegion。
```cpp
image->SetRegions( region );
image->Allocate( );   //注意：这里才真正给image对象分配内存
```
实际上，很少直接给图像分配内存和对图像进行初始化，图像通常都是从一个源文件直接读取的，比如从一个文件或从硬件获取数据。

设置和获取像素数据 `image->GetPixel(index)` 和 `image->SetPixel(index,value)`。根据索引位置访问像素值。
```cpp
ImageType::IndexType pixelIndex;   //创建像素位置
pixelIndex[0] = 27; // x position
pixelIndex[1] = 29; // y position
pixelIndex[2] = 37; // z position 
 
ImageType::PixelType pixelValue = image->GetPixel( pixelIndex ); //通过位置获取像素值
image->SetPixel( pixelIndex, pixelValue+1 ); 给指定位置设置像素值
```
定义原点和间距:

- 图像原点和间距是很多应用的基础。在坐标系中用来指定像素和图像之间的物理空间位置。
- 通俗讲，即为像素所在行/列/层  到物理空间x/y/z坐标的映射，如下图所示

![](https://github.com/YunchaoYang/MyCodingNotes/blob/master/Cpp/ITK/20190619135524822.png)
```cpp
ImageType::SpacingType spacing;  //创建像素间距对象
spacing[0] = 0.33; // spacing along X
spacing[1] = 0.33; // spacing along Y
spacing[2] = 1.20; // spacing along Z
 
image->SetSpacing( spacing );     //给图像设置间距
 
ImageType::PointType origin;       //创建像素原点对象
origin[0] = 0.0; 
origin[1] = 0.0;
origin[2] = 0.0;
image->SetOrigin( origin );        //给图像指定原点
```

```cpp
//获取图像的间距信息
const ImageType::SpacingType& sp = image->GetSpacing( );
std::cout << "Spacing = ";
std::cout << sp[0] << ", " << sp[1] << ", " << sp[2] << std::endl; 
 
//获取图像的原点信息
const ImageType::PointType& orgn = image->GetOrigin( );
std::cout << "Origin = ";
std::cout << orgn[0] << ", " << orgn[1] << ", " << orgn[2] << std::endl; 
```
图像原点和间距一经初始化，就会以物理空间坐标来正确映射到图像像素。（常用于查找鼠标所在位置的像素值等情况）
自定义图像完整代码展示：
```cpp
//创建一个二维图像
    using ImageType = itk::Image<unsigned char,2>;
    ImageType::Pointer image = ImageType::New();
 
    ImageType::IndexType start; //创建itk::Index对象,用来指定图像起点位置
    start[0] = 0;
    start[1] = 0;
 
    ImageType::SizeType size;   //创建itk::Size对象,指定图像各方向大小
    size[0] = 200;
    size[1] = 256;
 
    ImageType::RegionType region; //创建图像区域，并设置起点和大小
    region.SetSize( size );
    region.SetIndex( start );
    image->SetRegions(region);
 
    ImageType::SpacingType spacing;  //定义像素间距
    spacing[0] = 0.1;
    spacing[1] = 0.1;
    image->SetSpacing( spacing );
 
    ImageType::PointType origin;     //定义像素原点
    origin[0] = 0.0;
    origin[1] = 0.0;
    image->SetOrigin( origin );
 
    image->Allocate( );   //分配内存
    image->FillBuffer( itk::NumericTraits<unsigned char>::Zero ); //初始化图像缓冲区
 
    for(int i = 0 ; i < 200; i++) //像素所在行
    {
        start[0] = i;
        for(int j = 0; j < 256; j++) //像素所在列
        {
            start[1] = j;
            image->SetPixel(start,j);  //给指定位置设置像素值
        }
    }
 
     using WriterType = itk::ImageFileWriter<ImageType>;
     WriterType::Pointer writer = WriterType::New();
     writer->SetInput(image);
     writer->SetFileName("../createImage.jpg");
 
     using ImageIOType = itk::JPEGImageIO;
     ImageIOType::Pointer io = ImageIOType::New();
     writer->SetImageIO(io);
 
     try
     {
       writer->Update();
     }
     catch( itk::ExceptionObject & error )
     {
       std::cerr << "Error: " << error << std::endl;
     }
```
————————————————
原文链接：https://blog.csdn.net/qq_34760715/article/details/92820073




