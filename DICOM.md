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

## DICOM RT

Development of DICOM RT Information Objects started in January, 1995
Radiotherapy Information Objects (Supp 11, Final Text June 1997)
* RT Structure Set – image segmentation
* RT Plan – beam/source geometry and dosimetry
* RT Image – projection image in beam geometry
* RT Dose – dose matrix and DVHs

Radiotherapy Treatment Record (Supp 29, Final Text May 1999)
* RT Beams Treatment Record
* RT Brachy Treatment Record
* RT Treatment Summary Record

Radiotherapy Extensions for Ion Therapy (Supp 102, Final Text Mar 2006)
- RT Ion Plan 
- RT Ion Beams Treatment Record

