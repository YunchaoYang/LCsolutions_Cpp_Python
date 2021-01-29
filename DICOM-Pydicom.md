DICOM dataset,是DICOM文件的主要组成部分，其由DICOM数据元素按照指定的顺序排列。 
DataElement 数据元素最基本的数据单元是数据元，按照TAG从小到大顺序排列，即一个数据元表示一个TAG。TAG从小到大顺序排列
DataElement 主要由4个部分组成：
 - TAG号：由4个字节组成，包括2字节的组号和2字节的元素号（例如：0010 0040 表示患者性别，其中的组号：0002描述设备通讯信息、0008描述特征参数、0010描述患者信息、0028描述图像信息参数）。我们后期所需要的DICOM文件相关数据时，就是根据TAG来获取。
 - 值表示（VR，value representation）：由两个字节的字符组成，存储描述该项数据元信息的数据类型，包含例如：LO（Long String，长字符串）、IS（Interger String，整型字符串），DA（data，日期）等等共27种数据类型。
 - 值长度（value length）：存储描述该项信息的数据长度
 - 值域（value)：存储描述该项信息的数据值

 其中数据元信息可以根据信息的不同，分为4类：
 - Patient
    - Study
      - Series
        - Image

! [Patient tag](https://img-blog.csdnimg.cn/20200702220449443.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4MzMwMTQ4,size_16,color_FFFFFF,t_70)

! [Study tag](https://img-blog.csdnimg.cn/20200702220506227.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4MzMwMTQ4,size_16,color_FFFFFF,t_70)


'''python
增删查改

ds = pydicom.dcmread("rtplan.dcm")
print(ds.patientName)
ds.PatientName = "ABC"
ds[0x0010,0x0010].value = "abc"
ds.saveas("newrtplan.dcm")
if("PatientName" in ds):
  print(ds.PatientName)

del ds.PatientName

ds.add_new(0x00100010, 'PN', 'a000')
'''
