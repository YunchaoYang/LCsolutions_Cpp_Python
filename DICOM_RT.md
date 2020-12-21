学习使用DCMTK工具
### 了解DICOM
1、DICOM语法
       DICOM维护一个所有标准属性（超过2000个）的列表，即所谓的DICOM数据字典（DICOM Data Dictionary）。DICOM依靠数据字典来保证属性命名和处理的一致性。

       把这些超过2000个的项目按照一定顺序排列，所有项目首先被分成编号的项目组（group）（如果项目内容的大概相似就分为一组）。
       项目组是由单独的元素组合在一起的。因此，每个项目都有其自己的编号“(项目组,元素)”，这就是所谓的元素“标签（tag）”。
       所有进行标签的元素都称作“属性（attribute）”，或 者DICOM“数据元素（data element）” 或简称为DICOM“元素”。
       项目组和元素都是用十六进制数字编号的，“（项目组，元素）”标签唯一地对应属性名称。
Example: 
 - (Group,Element) tag（项目组，元素）标
  - (0008,0001)
- Attribute(data element) name 属性（数据元素）名称
 - Length to End 到结尾的长度
 - VR：值表现，DICOM标准在PS 3.5中定义了27个基本数据类型，每个VR都有他自己两个字母的缩写；表示内容的定义；数据中允许出现的字母描述；以及规定的数据长度。 
 - VM:数据元素值多样性。

### DICOM服务命令

* DIMSE-C  composite
* DIMSE-N normal

Eg. 
C-Echo：用来校验一个DICOM AE是否与另一个AE建立了连接。
C-Store：承载着要存储的数据。
C-Find：在C-Find服务提供者（如数字归档）那里进行匹配的查询参数。
C-Move：在服务者那边下载匹配参数的文档。

3、DICOM通信

       连接建立的两端都成为AE，为了区分服务请求者和服务提供者，
       DICOM称前者为服务类用户（Service Class Users，SCU），
       称后者为服务类提供者（Service Class Providers，SCP）。

#### Dicom文件解析
- 这里讲的暂不涉及通讯那方面的问题 只讲*.dcm 也就是diocm格式文件的读取，读取本身是没啥难度的 无非就是字节码数据流处理。只不过确实比较繁琐。
整体结构先是128字节所谓的导言部分，说俗点就是没啥意义的破数据 跳过就是了，
   然后是dataElement依次排列的方式 就是一个dataElement接一个dataElement的方式排到文件结尾.
通俗的讲dataElement就是指tag 就是破Dicom标准里定义的数据字典。
https://blog.csdn.net/leaf6094189/article/details/8510325

#### 值表示法VR
- Value Representation(2个单字节Char);
怎么理解VR呢，VR其实就是表示一种类别，表示的是该dataELement的类别。
VR，类似于java的String，Long，VR有LO（LongString长字符串），IS（IntergerString整形字符串），DA（data日期）等等共27中类型，还有一种UN（UnKnow未知类型）。

VR和Tag还是很有关联的。
我们知道tag是有很多的，大概2000个，也就是说有2000种tag。
但是VR只有27种。
每一种Tag其实是有一个固定的VR类型，也就是说不同的dicom文件他的同一个tag，VR肯定也是相同的。
但是就是不同的tag数据，有些是拥有同样的VR类型。
https://blog.csdn.net/wenzhi20102321/article/details/75127140

### tools for DICOM-RT

SlicerRT project in 3D Slicer
https://www.slicer.org/wiki/Documentation/Nightly/Modules/DicomRtImport
DICOM-RT import export (handle datasets of types RT Structure Set, RT Dose, RT Plan, RT Image)
DICOM-SRO import/export (handles DICOM Spatial Registration object, both rigid and deformable)

learn from a package in Matlab ( DICOM-RT to Matlab) https://github.com/ulrikls/dicomrt2matlab
1. Load DICOM headers
2. read contours sequences (reading and converting RT structures) 
Basically in this step, it will load ROINames, Points, VoxelPoints, Segmentation files 
in each slice by looping through contours
3. Save segmentations

2、DCMTK工具介绍

scu -->  scp  发送dcm文件

scp: storescp.exe  104  –aet myaet

scu: storescu.exe 127.0.0.1 104 C:/DICOM/Source/CT1/CT.dcm

storescp.exe是Dcmtk工具包中用于接收DICOM影像并进行保存的服务端程序

-aet myaet中的aet为Application Entity Title
### DICOMRT


### 

### reference:

https://blog.csdn.net/wenzhi20102321/article/details/75127362?ops_request_misc=%25257B%252522request%25255Fid%252522%25253A%252522160832500516780308313335%252522%25252C%252522scm%252522%25253A%25252220140713.130102334..%252522%25257D&request_id=160832500516780308313335&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-75127362.nonecase&utm_term=DICOM


Too much, may not be useful.
dicom文件解析知识的其他地址：

1.dicom文件详解
http://blog.csdn.net/wenzhi20102321/article/details/75127362

2.dicom文件的值类型VR详解
http://blog.csdn.net/wenzhi20102321/article/details/75127140

3.dicom文件tag详解
http://blog.csdn.net/wenzhi20102321/article/details/75127101

4.android 解析并显示dicom文件的数据和图像
http://blog.csdn.net/wenzhi20102321/article/details/75040225

5.java代码使用ImageJ解析dicom文件成图片
http://blog.csdn.net/wenzhi20102321/article/details/74995084

前面5个是我自己写的，后面是一些我自己看过的相关资料：

6.Dicom文件解析
http://blog.csdn.net/leaf6094189/article/details/8510325

7.使用dcm4che3获取Dicom的bmp格式缩略图
http://blog.csdn.net/Kerrigeng/article/details/60866656

8.使用dcm4che3解析DICOM中，中文乱码问题
http://blog.csdn.net/Kerrigeng/article/details/53942846

9.使用dcm4che3对jpeg压缩的dcm文件进行解压
http://blog.csdn.net/Kerrigeng/article/details/62215647

10.DICOM的常用Tag分类和说明
http://www.cnblogs.com/stephen2014/p/4579443.html

11.dicom的大牛zssure的博客，几十篇文章
http://blog.csdn.net/zssureqh/article/category/1389985

12.dicom协议中文文档下载
http://download.csdn.net/detail/wenzhi20102321/9897014

13.Sante DICOM Editor 4，查看dicom文件的工具，直接打开用
http://download.csdn.net/detail/wenzhi20102321/9895616

