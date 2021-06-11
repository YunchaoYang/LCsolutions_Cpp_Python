#
There are two principle types of data represented in ITK: images and meshes. both of which are subclasses of
itk::DataObject

## itk::Image
itk::Image represents an n-dimensional, regular sampling of data. T

One of the important ITK concepts regarding images is that rectangular, continuous pieces of the
image are known as regions.

1. LargestPossibleRegion—the image in its entirety.
2. BufferedRegion—the portion of the image retained in memory.
3. RequestedRegion—the portion of the region requested by a filter or other class when operating on the image.

## itk::Mesh
The itk::Mesh class represents an n-dimensional, unstructured grid. The topology of the mesh is
represented by a set of cells defined by a type and connectivity list; the connectivity list in turn refers
to points. The geometry of the mesh is defined by the n-dimensional points in combination with
associated cell interpolation functions. Mesh is designed as an adaptive representational structure
that changes depending on the operations performed on it.

The mesh is defined in terms of three template parameters: 1) a pixel type associated with the
points, cells, and cell boundaries; 2) the dimension of the points (which in turn limits the maximum
dimension of the cells); and 3) a “mesh traits” template parameter that specifies the types of the
containers and identifiers used to access the points, cells, and/or boundaries.

Mesh is a subclass of itk::PointSet.

## Data Processing Pipeline

While data objects (e.g., images and meshes) are used to represent data, process objects are classes
that operate on data objects and may produce new data objects. Process objects are classed as
sources, filter objects, or mappers.

The data processing pipeline ties together data objects (e.g., images and meshes) and process objects.
The pipeline supports an automatic updating mechanism that causes a filter to execute if and only
if its input or its internal state changes.

Typically data objects and process objects are connected together using the SetInput() and
GetOutput() methods as follows:

``` cpp
using FloatImage2DType = itk::Image<float,2>;

itk::RandomImageSource<FloatImage2DType>::Pointer random; // 

random = itk::RandomImageSource<FloatImage2DType>::New(); // 
random->SetMin(0.0);
random->SetMax(1.0);

itk::ShrinkImageFilter<FloatImage2DType,FloatImage2DType>::Pointer shrink;
shrink = itk::ShrinkImageFilter<FloatImage2DType,FloatImage2DType>::New();
shrink->SetInput(random->GetOutput());
shrink->SetShrinkFactors(2);
itk::ImageFileWriter<FloatImage2DType>::Pointer writer;
writer = itk::ImageFileWriter<FloatImage2DType>::New();
writer->SetInput (shrink->GetOutput());
writer->SetFileName( "test.raw" );
writer->Update();
```
  
  In this example the source object itk::RandomImageSource is connected to
the itk::ShrinkImageFilter, and the shrink filter is connected to the mapper
itk::ImageFileWriter.

When the Update() method is invoked on the writer, the data
processing pipeline causes each of these filters to execute in order, culminating in writing the final
data to a file on disk.

ITK spatial objects provide a common interface for accessing the physical location and geometric
properties of and the relationship between objects in a scene that is independent of the form used
to represent those objects.

Currently implemented types of spatial objects include: Blob, Ellipse, Group, Image, Line, Surface,
and Tube.

