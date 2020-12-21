### dicom文件解析
Dicom全称是医学数字图像与通讯，这里讲diocm格式文件的解读，读取本身是没啥难度的 无非就是字节码数据流处理。只不过确实比较繁琐。

#### DICOM资料的结构
   一个患者到医院就诊，为了判断他的病灶，医生需要指定不同的检查(例如: CT，MR，超声)，每一项检查都需要由相对应的仪器完成，
   但仪器产生的是一系列的影像(例如CT产生一组10张，MR产生10张和20张各一组影像)，这些影像和病人如何产生关联呢?

 在DICOM规格中，使用了相对应的资料结构来描述: 定义出Patient，Study，Series，Image四个层次来存储上述例子。
  *  Patient中包含了该病人的所有基本资料(姓名，性别，年龄等)和医生指定的检查Study;
  *  Study中包含了检查种类(CT，MR，B超)和指定检查的Series;
  *  Series中包含检查的技术条件(毫安，FOV，层厚等)和图像IMAGE。

https://blog.csdn.net/louishao/article/details/73528985?utm_medium=distribute.pc_relevant_download.none-task-blog-baidujs-2.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-baidujs-2.nonecase
整体结构先是128字节所谓的导言部分，跳过就是了，接着就是四个字节组成的字符串，然后是dataElement元素依次排列的方式， 就是一个dataElement接一个dataElement的方式排到文件结尾.我们要读取dicom里面的各种数据就是在各个数据元素中。通俗的讲dataElement就是指tag，就是破Dicom标准里定义的数据字典，每个dataElement中的tag决定自身或整个文件的某些数据类型或自身dataElement内容类别。
其中tag和VR是要重点理解，也是比较难理解的！

一.标记tag(2字节UInt16分组号和2字节UInt16元素号);
tag是4个字节表示的 前两字节是组号后两字节是元素号 比如0008（组号） 0018（元素号）。
我们获取dicom里面的数据，就是根据tag，来知道这个dataElement里面是否是我们需要的数据，然后读取该dataElement里面的数据。

一般我们获取dataElement中的数据的主要组号
0002组描述设备通讯，0008组描述特征参数，0010组描述患者信息，0028组描述图像信息参数
还是有很多其他组号的，但是里面的数据不常用到，tag总共大约有2000个，但是我们常用的数据就那么几个！

dicom文件数据中所有dataElement从前到后按tag又可简单分段：文件元tag，普通tag，像素tag。
1.文件元tag（组号+0000）：不受传输语法影响，总是以显示VR方式表示，因为它里面就定义了传输语法；文件元tag的dataElement，并没有多大的意义，它的VF数值是整个组所有dataElement的字节长度，一个dicom中可以只有一个文件元tag，也可以有多个文件元tag。
2.普通tag：除了文件元tag和像素tag，其余的都是普tag数据。包括：图像宽，高，数据传输格式，病人姓名，病人生日，病历医院，病历科室，病情的描述等等数据；
3.像素tag（7fe0,0010）：表示dataElement存储的是病历的图像数据。

https://blog.csdn.net/m_buddy/article/details/53117427?utm_medium=distribute.pc_relevant_download.none-task-blog-baidujs-3.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-baidujs-3.nonecase

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

2、DCMTK工具介绍

scu -->  scp  发送dcm文件

scp: storescp.exe  104  –aet myaet

scu: storescu.exe 127.0.0.1 104 C:/DICOM/Source/CT1/CT.dcm

storescp.exe是Dcmtk工具包中用于接收DICOM影像并进行保存的服务端程序

-aet myaet中的aet为Application Entity Title

