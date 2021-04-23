
<div id="article_content" class="article_content clearfix">
        <link rel="stylesheet" href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/editerView/ck_htmledit_views-b5506197d8.css">
                <div id="content_views" class="htmledit_views">
                    <p style="margin-left:0cm;"><strong>ITK</strong><strong>库梳理总结： </strong></p> 
<p style="margin-left:0cm;"><img alt="" height="534" src="https://img-blog.csdnimg.cn/20200430145748923.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM3ODA2MTA3,size_16,color_FFFFFF,t_70" width="375"></p> 
<p><strong>1、数据的表示与访问类：基类：</strong><strong>itk::Image, itk::Mesh </strong><strong>和</strong><strong> itk::PointSet.</strong></p> 
<p><strong>1）图像数据类：</strong><strong> </strong></p> 
<ul><li>基类：itk::Image ITK支持多种像素类型、多种空间维度图像进行操作。itk::ImageRegion：图像区域类：由itk::Index和itk::Size类定义；可以通过使用图像的起始索引和大小初始化该区域。成员函数：SetSize()、SetIndex()、SetRegions();</li><li>图像的读写类：itk::ImageFileReader、itk::ImageFileWriter；</li><li>像素数据访问：与itk::PointSet类可是实现交互</li><li>位置与间距定义类：利用itk::Image类中成员函数实现</li></ul>
<p style="text-indent:33px;">SetOrigin()和GetOrigin()：设置和检索图像的原点；</p> 
<p style="text-indent:33px;">SetSpacing()和GetSpacing()：将数组分配给图像、以及从图像中检索Spacing信息；</p> 
<p style="text-indent:33px;">SetDirection()和GetDirection()：设置与检索图像方向；</p> 
<p style="text-indent:33px;">TransformPhysicalPointToIndex()：计算最接近提供点的像素索引。</p> 
<ul><li>RGB图像类：</li></ul>
<p style="text-indent:33px;">结合RGB点集类对RGB图像进行操作；同时，允许自己创建属于自己的像素类型；</p> 
<ul><li>向量类型图像：</li></ul>
<p><strong>2）点集操作类</strong></p> 
<ul><li>集类：itk::PointSet是itk::Mesh的一个基类提供点集操作方法，其旨在利用N维空间中的一组点集来表示几何形状。例如：SetPoint()：将点插入PointSet中。GetPoint()：从PointSet中读取点；GetNumberOfPoints()：可以查询PointSet以确定已插入多少点； PointsContainer类型取决于PointSet类型：其中动态PointSet使用itk :: MapContainer；静态PointSet使用itk :: VectorContainer；同时，itk::PointSet与itk::Image可以实现交互；例如：SetPointData()：将数据插入PointSet；GetPointData()：从PointSet中读取数据；</li><li>RGB像素类型点集类：itk::RGBPixel</li><li>向量像素类型：itk::Vector</li><li>法线像素类型：itk::CovariantVector</li></ul>
<p><strong>3）Mesh</strong><strong>类：</strong>itk::PointSet类的派生类，用以表示空间形状；</p> 
<ul><li>单元格类型类：itk::Mesh在表示空间形状时候可以包含多种单元格类型。例如：itk::LineCell、itk::TriangleCell、itk::QuadrilateralCell、itk::TetrahedronCell和itk::PolygonCell，必须包含此类的头文件。</li></ul>
<p style="text-indent:33px;">简单操作：SetCellData()：将与单元格关联的数据插入到网格。对应有GetCellData();CellDataContainer中内置的Iterators可以更有效的访问单元格数据；</p> 
<ul><li>可以通过单元格管理数据</li><li>通过itk::DefaultStaticMeshTraits可以自定义网格；</li><li>拓扑结构数据</li><li>SetBoundaryAssignment()：可实现类似为四面体单元格分配了四个顶点以作为维数为零的边界等任务；</li><li>查询四面体单元以获取有关其边界特征的信息：GetNumberOfBoundaryFeatures（）获得每个维度的边界特征数量；GetBoundaryAssigment()可恢复边界分配；</li><li>折线表示：</li><li>利用零点与一维像元类：itk::VertexCell和itk::LineCell可以表示；</li><li>Cell的遍历</li></ul>
<p><strong>4）Path</strong><strong>类：</strong>itk::PolyLineParametricPath：常用于以简洁的方式表示2D图像分割算法的输出，同时也可以用于将N维中的任何打开或闭合曲线表示为线性分段近似。</p> 
<p style="margin-left:0cm;"><strong>2、空间对象类：基类itk::SpatialObject</strong><strong>；</strong></p> 
<p><strong>1）基类：</strong><strong>itk::SpatialObjects</strong></p> 
<ul><li>函数AddChild（）：第二个对象添加到第一个对象；</li><li>GetChildren（）可访问该对象的子级列表；</li><li>以及其他函数RemoveChild()、GetNumberOfChildren()、RemoveAllChildren()</li></ul>
<p><strong>2）空间转换的函数</strong>:以实现Object Spatial与 WorldSpace的转换；</p> 
<p><strong>3）空间对象</strong></p> 
<ul><li>Arrow空间对象：itk::ArrowSpatialObject派生于基类itk::SpatialObject</li><li>Blob空间对象：itk::BlobSpatialObject类源于itk::itkPointBasedSpatialObject类</li><li>Ellipse空间对象：itk::EllipseSpatialObject派生于基类itk::SpatialObject</li><li>Gaussian空间对象：itk::GaussianSpatialObject类</li><li>Group空间对象：itk:: GroupSpatialObject</li><li>Image空间对象：itk::ImageSpatialObject包含一个itk::Image，但添加了空间变换和父子层次结构的概念。</li><li>ImageMask空间对象：itk:: ImageMaskSpatialObject</li><li>Landmark空间对象：itk:: LandmarkSpatialObject</li><li>Line空间对象：itk:: LineSpatialObject</li><li>Mesh空间对象：itk:: MeshSpatialObject包含指向itk :: Mesh的指针，但添加了空间变换和父子层次结构的概念。</li><li>Surface空间对象：itk:: SurfaceSpatialObject</li><li>Tube空间对象：itk:: TubeSpatialObject</li><li>DTITube空间对象：itk:: DTITubeSpatialObject源自于itk:: TubeSpatialObject</li></ul>
<p><strong>4）空间对象读写：</strong>itk::SpatialObjectReader、itk::SpatialObjectWriter</p> 
<p><strong>3、图像迭代器：</strong>迭代器是内存指针的抽象，用于容器值的迭代，顺序访问。 迭代器出现在for和while循环构造中，依次访问每个数据点。 例如，C指针是迭代器的一种。 它可以在内存中向前（递增）和向后（递减）移动，以顺序引用数组的元素。 许多迭代器实现都具有类似于C指针的接口。</p> 
<p><strong>1）图像</strong><strong>Region</strong><strong>迭代器：</strong>itk::ImageRegionIterator</p> 
<p><strong>2）具有索引的图像</strong><strong>Region</strong><strong>迭代器：</strong>itk::ImageRegionIteratorWithIndex</p> 
<p><strong>3）具有索引的图像线性迭代器：</strong>itk::ImageLinearIteratorWithIndex</p> 
<p><strong>4）具有索引的图像切片迭代器：</strong>itk::ImageSliceIteratorWithIndex</p> 
<p><strong>5）具有索引的图像随机常量迭代器：</strong>itk::ImageRandomConstIteratorWithIndex</p> 
<p><strong>4、图像适配器（</strong><strong>Iamge Adaptors</strong><strong>）：</strong>基类：itk::ImageAdaptor；目的是使一个图像看起来像另一幅图像，可能是不同的像素类型。例如将像素类型为unsigned char的图像，并将其显示为像素类型为float的图像。另外，可以执行轻量级的像素操作，从而取代了对滤镜的需求。itk::ExpImageAdaptor、itk::SinImageAdaptor、itk::CosImageAdaptor</p> 
<p><strong>1）实现</strong><strong>RGB</strong><strong>图像适配；</strong></p> 
<p><strong>2）实现</strong><strong>Vector</strong><strong>图像适配</strong></p> 
<p><strong>5、图像读写类：</strong>itk::ImageFileReader、itk::ImageFileWriter，读写特定文件格式的实际低层任务是由一连串的itk :: ImageIO类在后台完成的。函数：SetFileName()、SetInput（）将这些读取器和写入器连接到过滤器以创建管道。</p> 
<p><strong>1）Pluggable Factories</strong><strong>：</strong>通过将文件名传递给类itk :: ImageIOFactory，并要求其标识能够读取或写入用户指定文件的ImageIO的任何子类来完成。</p> 
<p><strong>2）读写</strong><strong>RGB</strong><strong>：</strong>需要包含RGB图像的点操作itk::RGBPixel</p> 
<p><strong>3）读、投影、写图像时候由于涉及到图像强度调整：</strong>itk :: RescaleIntensityImageFilter用于线性重新缩放图像值；</p> 
<p><strong>4）提取图像区域与切片：</strong>利用区域图像滤波类itk::RegionOfInterestImageFilter，itk:: ExtractImageFilter</p> 
<p><strong>5）向量图像的读写：</strong>需结合点集操作中的itk::Vector类；</p> 
<p><strong>6）矢量图像中提取标量图像：</strong>滤波器类中itk :: VectorIndexSelectionCastImageFilter类；</p> 
<p><strong>7）读写图像</strong><strong>Series</strong><strong>：</strong></p> 
<ul><li>itk::ImageSeriesReader，itk::ImageSeriesWriter；</li><li>利用itk::NumericSeriesFileNames类生成文件名；</li><li>也可以完成RGB图像Series的读写，可利用点集类中的itk::RGBPixel</li></ul>
<p><strong>8）读和写</strong><strong>DICOM</strong><strong>图像：</strong>需要利用itk::GDCMImageIO类，它封装了基础GDCM库的连接。</p> 
<ul><li>itk::GDCMSeriesFileNames类可以生成文件名</li><li>成员函数实现具体的操作：SetDirectory()，SetUseSeriesDetails(true)、AddSeriesRestriction()</li></ul>
<p><strong>6、图像滤波类：</strong></p> 
<p><strong>1）阈值滤波：</strong>itk::BinaryThresholdImageFilter、itk::ThresholdImageFilter。其中包括高通、低通、带通、带阻等；</p> 
<p><strong>2）边界检测：</strong>主要是坎尼边界检测itk::CannyEdgeDetectionImageFilter.</p> 
<p><strong>3）Casting and Intensity Mapping</strong><strong>（投影与强度映射）：</strong></p> 
<ul><li>线性映射：itk::CastImageFilter：输入图像进行逐像素处理，将每个像素转换为输出图像的类型；itk::RescaleIntensityImageFilter：线性缩放像素值：将输入的最小值和最大值映射到用户提供的最小值和最大值itk::ShiftScaleImageFilter：对强度做映射；itk::NormalizeImageFilter：正则化图像滤波；</li><li>线性映射：itk::SigmoidImageFilter；</li></ul>
<p><strong>4）梯度：</strong></p> 
<ul><li>梯度幅度图像滤波（锐化）：itk::GradientMagnitudeImageFilter；（数字图像中的空域滤波算子）</li><li>梯度幅度图像滤波（平滑）：itk::GradientMagnitudeRecursiveGaussianImageFilter</li><li>Derivative 图像滤波：itk::DerivativeImageFilter</li></ul>
<p><strong>5）二阶导数</strong><strong>(</strong><strong>图像微分</strong><strong>)</strong><strong>：</strong></p> 
<ul><li>高斯滤波：itk:: RecursiveGaussianImageFilter</li><li>拉普拉斯滤波：itk::RecursiveGaussianImageFilter</li></ul>
<p><strong>6）邻域滤波：</strong></p> 
<ul><li>均值滤波：itk::MeanImageFilter</li><li>中值滤波：itk::MedianImageFilter</li><li>形态学滤波：itk:: BinaryErodeImageFilter、itk:: BinaryDilateImageFilter、itk::GrayscaleErodeImageFilter、itk::GrayscaleDilateImageFilter</li><li>投票滤波器：二进制中值滤波itk:: BinaryMedianImageFilter；孔洞填充：itk::VotingBinaryHoleFillingImageFilter；迭代孔洞填充：itk:: VotingBinaryIterativeHoleFillingImageFilter；</li></ul>
<p><strong>7）平滑滤波</strong></p> 
<ul><li>模糊：离散高斯：itk::DiscreteGaussianImageFilter；二项式模糊：itk::BinomialBlurImageFilter；递归高斯：itk::RecursiveGaussianImageFilter</li><li>局部模糊：</li><li>边界保留平滑：itk::GradientAnisotropicDiffusionImageFilter；itk::CurvatureAnisotropicDiffusionImageFilter；itk::CurvatureFlowImageFilter；itk::MinMaxCurvatureFlowImageFilter；itk::BilateralImageFilter</li></ul>
<p><strong>8）距离映射：</strong>itk::DanielssonDistanceMapImageFilter.</p> 
<ul><li>均值滤波：itk::MeanImageFilter</li><li>中值滤波：itk::MedianImageFilter</li></ul>
<p><strong>9）几何变换：</strong></p> 
<ul><li>翻转：itk::FlipImageFilter</li><li>重采样：itk::ResampleImageFilter</li></ul>
<p><strong>10）频域：</strong></p> 
<ul><li>FFT：基类itk::ForwardFFTImageFilter；派生类：itk::VnlForwardFFTImageFilter；itk::FFTWRealToComplexConjugateImageFilter</li><li>中值滤波：itk::MedianImageFilter</li></ul>
<p><strong>11）Extracting Surfaces</strong><strong>：</strong>itk::Mesh</p> 
<p><strong>12）其他图像滤波类：</strong>可用于某些特定的图像配准任务中</p> 
<ul><li>重采样图像滤波：itk::ResampleImageFilter</li><li>直方图匹配图像滤波：itk::HistogramMatchingImageFilter</li><li>Cast图像滤波：itk::CastImageFilter</li><li>Warp图像滤波：itk::WarpImageFilter</li></ul>
<p><strong>7、图像配准类：</strong>常用的基类：itk::ImageRegistrationMethodv4</p> 
<p><strong>1）Monitoring</strong><strong>配准：</strong>itk::Object、itk::Command和itk::EventObject；其中Object是大多数ITK对象的基类。此类维护指向事件观察器的指针的链接列表。 Command类扮演观察员的角色，可向对象注册，声明他们有兴趣在特定事件发生时接收通知。 EventObject类表示一组事件层次结构表示（开始，结束，进度和迭代）</p> 
<p><strong>2）中心初始化：</strong></p> 
<ul><li>刚性配准：itk::Euler2DTransform类可以执行2D刚性配准</li><li>类itk::CenteredTransformInitializer可用于其他维度的刚性配准</li><li>类itk::ImageMomentsCalculator可用于计算图像质心</li></ul>
<p><strong>3）转换：</strong></p> 
<ul><li>Identity转换：itk::IdentityTransform类主要用于调试，具体的配准任务中不常用；</li><li>Translation转换：itk::TranslationTransform简单但最有用的转换之一，通过向其添加向量来映射所有点；</li><li>Scale转换：itk::ScaleTransform表示向量空间的简单缩放；</li><li>Scale对数转换：itk::ScaleLogarithmicTransform类是itk::ScaleTransform的变种，可以对itk::ScaleTransform类中的参数进行优化；</li><li>Euler2D转换：itk :: Euler2DTransform实现了2D刚性转换；</li><li>Euler3D转换：itk::Euler3DTransform</li><li>CenteredRigid2D转换：itk :: CenteredRigid2DTransform在2D中实现刚性转换，可以指定任意旋转中心，而Euler2DTransform只可以利用原点作为旋转中心；</li><li>Similarity2D转换：itk :: Similarity2DTransform可看作是与各向同性缩放因子结合的刚性变换，并保留线之间的角度。2D实现中结合了itk :: ScaleTransform和itk :: Euler2DTransform的特征；</li><li>Similarity3D转换：itk :: Similarity3DTransform</li><li>四元刚性转换：itk::QuaternionRigidTransform，主要是实现3D的刚性变换；</li><li>Versor转换：itk::VersorTransform该类是对itk::QuaternionRigidTransform的旋转部分，且主要针对2D；</li><li>Versor刚性3D转换：itk::VersorRigid3DTransform</li><li>刚性3D透视转换：itk::Rigid3DPerspectiveTransform在3D空间中实现了刚性变换，通过透视投影。</li><li>Affine转换：itk::AffineTransform，利用线性表示实现转换；</li><li>BSpline形变转换：用于解决形变套准问题，等效于生成变形场，其中将变形矢量分配给空间中的每个点；</li><li>Kernel 转换：利用不同的核函数实现转换；Itk ::ElasticBodySplineKernelTransform；Itk ::ElasticBodyReciprocalSplineKernelTransform；Itk ::ThinPlateSplineKernelTransform；Itk ::ThinPlateR2LogRSplineKernelTransform；Itk ::VolumeSplineKernelTransform</li></ul>
<p><strong>3）内插器：</strong></p> 
<ul><li>最近邻内插：itk::NearestNeighborInterpolateImageFunction</li><li>线性内插：itk::LinearInterpolateImageFunction</li><li>B-Spline内插：itk::BSplineInterpolateImageFunction类使用B-Spline基函数表示图像强度，输入图像首先连接到插值器时，将使用递归滤波计算B-Spline系数。</li><li>窗口Sinc内插：itk::WindowedSincInterpolateImageFunction，离散网格中数字化的数据的最佳内插器，基于傅里叶变换；</li></ul>
<p><strong>4）度量器：</strong>基类：itk::ImageToImageMetricv4；其中又包括ITKv3与ITKv4两种；</p> 
<p style="margin-left:0cm;"><strong>ITKv3</strong><strong>：</strong></p> 
<ul><li>均方itk::MeanSquaresImageToImageMetricv4</li><li>相关性：itk::CorrelationImageToImageMetricv4</li><li>Mattes互信息：itk::MattesMutualInformationImageToImageMetricv4</li><li>联合直方图互信息：itk::JointHistogramMutualInformationHistogramImageToImageMetricv4</li><li>Demons度量：itk::DemonsImageToImageMetricv4</li><li>ANTS邻域相关性度量itk::ANTSNeighborhoodCorrelationImageToImageMetricv4；</li></ul>
<p style="margin-left:0cm;">&nbsp;<strong>ITKv3</strong><strong>：</strong></p> 
<ul><li>均方：itk :: MeanSquaresImageToImageMetric</li><li>归一化相关：itk :: NormalizedCorrelationImageToImageMetric</li><li>均方差：itk :: MeanReciprocalSquareDifferenceImageToImageMetric</li><li>Viola and Wells互信息：itk :: MutualInformationImageToImageMetric</li><li>Mattes互信息：itk :: MattesMutualInformationImageToImageMetric</li><li>Kullback和Liebler的Kullback Liebler距离度量：itk :: KullbackLeiblerCompareHistogramImageToImageMetric</li><li>标准化互信息：itk :: NormalizedMutualInformationHistogramImageToImageMetric</li><li>均方直方图：itk： :: MeanSquaresHistogramImageToImageMetric</li><li>相关系数直方图：itk :: CorrelationCoefficientHistogramImageToImageMetric</li><li>基数匹配指标：itk :: MatchCardinalityImageToImageMetric</li><li>Kappa统计量度：itk :: KappaStatisticImageToImageMetric</li><li>梯度差：itk :: GradientDifferenceImageToImageMetric</li></ul>
<p><strong>5）优化器：</strong></p> 
<ul><li>Amoeba优化器：itk :: AmoebaOptimizerv4</li><li>梯度下降法：itk :: GradientDescentOptimizerv4</li><li>梯度下降线搜索：tk :: GradientDescentLineSearchOptimizerv4</li><li>共轭梯度下降法：itk :: ConjugateGradientLineSearchOptimizerv4</li><li>拟牛顿法：itk::QuasiNewtonOptimizerv</li><li>LBFGS优化：itk::LBFGSOptimizerv4</li><li>LBFGSB优化：itk::LBFGSBOptimizerv4</li><li>一加一优化：itk::OnePlusOneEvolutionaryOptimizerv4</li><li>Regular Step梯度下降：itk::RegularStepGradientDescentOptimizerv4</li><li>Powell优化：itk::PowellOptimizerv4</li><li>Exhausive优化器: itk::PowellOptimizerv4参数空间上对网格进行完全采样。这个优化器是等效于在参数空间上定义的离散网格中进行穷举搜索。</li></ul>
<p><strong>6）配准方法类：</strong></p> 
<ul><li>点集配准类：itk：PointSetToPointSetRegistrationMethod</li></ul>
<p><strong>7）配准滤波：</strong></p> 
<ul><li>有限元配准滤波：itk::FEMRegistrationFilter</li><li>水平集配准滤波：tkLevelSetMotionRegistrationFilter</li><li>Demon配准滤波：Itk::DemonsRegistrationFilter：itk::FlipImageFilter</li><li>SymmetricForces配准滤波：itkSymmetricForcesDemonsRegistrationFilter</li><li>利用多分辨率参数图像滤波类：itk::MultiResolutionPyramidImageFilter can：</li></ul>
<p><strong>8、图像分割：</strong></p> 
<p><strong>1）区域生长：</strong></p> 
<ul><li>itk::ConnectedThresholdImageFilter；</li><li>itk::OtsuThresholdImageFilter</li><li>itk::NeighborhoodConnectedImageFilter</li><li>itk::ConfidenceConnectedImageFilter</li><li>tk::IsolatedConnectedImageFilter</li><li>itk::VectorConfidenceConnecte</li></ul>
<p><strong>2）基于分水岭的分割：</strong></p> 
<ul><li>itk::WatershedImageFilter</li></ul>
<p><strong>3）基于水平集的分割：</strong></p> 
<ul><li>itk::FastMarchingImageFilter；</li><li>itk::ShapeDetectionLevelSetImageFilter；</li><li>itk::GeodesicActiveContourLevelSetImageFilter；</li><li>itk::ThresholdSegmentationLevelSetImageFilter；</li><li>itk::CannySegmentationLevelSetImageFilter；</li><li>itk::LaplacianSegmentationLevelSetImageFilter；</li><li>itk::GeodesicActiveContourShapePriorLevelSetFilter</li></ul>
<p><strong>4）特征提取：</strong></p> 
<ul><li>itk::HoughTransform2DLinesImageFilter；</li><li>itk::HoughTransform2DCirclesImageFilter；</li></ul>
<p><strong>9、统计：</strong><strong>itk::Statistics</strong></p> 
<p><strong>1）数据容器：</strong></p> 
<ul><li>样本接口：itk::Statistics::Sample</li><li>样本适配器：itk::Statistics::ImageToListSampleAdaptor；itk::Statistics::PointSetToListSampleAdaptor</li><li>直方图：itk::Statistics::Histogram</li><li>Sub样本：itk::Statistics::Subsample</li><li>Membership样本：itk::Statistics::MembershipSample</li></ul>
<p><strong>2）常见的算法与函数：</strong></p> 
<ul><li>样本统计：itk::Statistics::ListSample</li><li>样本生成：</li><li>概率密度函数：itk::Statistics::GaussianMembershipFunction</li><li>距离度量：itk::Statistics:: DistanceMetric</li><li>欧几里得距离：itk::Statistics::EuclideanDistance</li><li>决策规则：</li></ul>
<p style="text-indent:33px;">最大决策：itk::MaximumDecisionRule</p> 
<p style="text-indent:33px;">最小决策：itk::MinimumDecisionRule</p> 
<p style="text-indent:33px;">最大比率决策：itk::MaximumRatioDecisionRule.</p> 
<ul><li>随机变量生成：</li></ul>
<p style="text-indent:33px;">正则化变量生成（高斯分布）：itk::Statistics::NormalVariateGenerator</p> 
<p><strong>3）统计在图像中应用：</strong></p> 
<ul><li>图像直方图操作：</li><li>图像信息论：</li></ul>
<p><strong>4）分类：</strong></p> 
<ul><li>k-d树：itk::Statistics::KdTree</li><li>基于k-d树的k-均值聚类：itk::Statistics::KdTreeBasedKmeansEstimator</li><li>k-均值聚类分类：itk::Statistics::ScalarImageKmeansImageFilter</li><li>贝叶斯分类器：利用高斯密度函数</li><li>期望最大化混合模型估计：</li></ul>
<p style="text-indent:33px;">itk::Statistics::ExpectationMaximizationMixtureModelEstimator</p> 
<ul><li>随机森林：itk::Statistics::MRFImageFilter</li></ul>
<p style="margin-left:0cm;"><strong>10、其他：</strong></p> 
<p><strong>1）Bridge</strong><strong>类：</strong>VTK、NumPy等；</p> 
<p><strong>2）兼容性：解决不同模块之间的兼容性</strong></p> 
<ul><li>图像转换：itk::ImageTransformer</li><li>向量投影图像滤波：itk::VectorCastImageFilter</li><li>条件变量：itk::Condition Variable</li></ul>
<p><strong>3）IO</strong><strong>接口类：</strong>BioRad、BMP、CSV、GDCM、GE、ImageBase、Meta、TransformMINC等</p> 
<p><strong>4）Numerics</strong><strong>：</strong>Eigen、有限元（FEM）、优化器、统计等；</p> 
<p><strong>5）第三方类：</strong></p> 
<p><strong>6）视频处理类：</strong>OpenCVd 链接、滤波、视频IO接口等；</p>
                </div><div data-report-view="{&quot;mod&quot;:&quot;1585297308_001&quot;,&quot;dest&quot;:&quot;https://blog.csdn.net/qq_37806107/article/details/105861470&quot;,&quot;extend1&quot;:&quot;pc&quot;,&quot;ab&quot;:&quot;new&quot;}"><div></div></div>
        </div>
