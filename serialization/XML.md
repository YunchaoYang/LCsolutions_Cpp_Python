### XML——XML介绍和基本语法
* 所有XML元素Element都须有关闭标签
*  Declaration声明没有关闭标签。
*  可扩展的
*  大小写敏感。
*  必须正确地嵌套
*  必须有根元素
*  属性值须加引号
*  空格会被保留
* 5个预定义的实体引用：&lt;(<),&gt;(>), &amp;(&), &apos;(‘), &quot;(“).

### XML验证/ML文件约束
拥有正确语法的XML被称为“形式良好”的XML。文档类型定义(DTD)
*  DTD的作用是定义XML文档的结构。它使用一系列合法的元素来定义文档结构。
*  XMLSchema：W3C支持一种基于XML的DTD代替者，它名为XML Schema。

### XML验证器：
XML错误会终止你的程序。 XML文档中的错误会终止你的XML程序。

### XML解析器
解析器把XML载入内存，然后把它转换为可通过JavaScript访问的XML DOM对象。
### XMLDOM：DOM(Document Object Model,文档对象模型)
定义了访问和操作文档的标准方法。DOM把XML文档作为树结构来查看。能够通过DOM树来访问所有元素。
可以修改或删除它们的内容，并创建新元素。元素，它们的文本，以及它们的属性，都被认为是节点。

### XML命名空间(XML Namespaces)
XML命名空间提供避免元素命名冲突的方法。
XMLNamespace(xmlns)属性：XML命名空间属性被放置于元素的开始标签之中，并使用以下语法：xmlns:namespace-prefix=”namespaceURI”

### XML文件约束- DTD文档
DTD文件一般和XML文件配合使用，主要是为了约束XML文件。
XML文件引入DTD文件，这样XML可以自定义标签，但又受到DTD文件的约束。比如上一节使用XML描述一个班级的信息，如果我们给每一个学生定义一个<面积>标签，语法上也是没有错误的，但是不符合语义，学生怎么能够用面积来描述呢？这时候我们就需要用到DTD文件来约束这个XML。

```xml
<!ELEMENT 班级 (学生+)>
<!ELEMENT 学生 (名字,年龄,介绍)>
<!ELEMENT 名字 (#PCDATA)>
<!ELEMENT 年龄 (#PCDATA)>
<!ELEMENT 介绍 (#PCDATA)>
```
编写myClass.xml文件并引入DTD文件如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--引入dtd文件，约束这个xml-->
<!DOCTYPE 班级 SYSTEM "myClass.dtd">
<班级>
    <学生>
        <名字>周小星</名字>    
        <年龄>23</年龄>
        <介绍>学习刻苦</介绍>
    </学生>   
    <学生>
        <名字>林晓</名字> 
        <年龄>25</年龄>
        <介绍>是一个好学生</介绍>
    </学生>   
</班级>
```
### XML文件约束- XML Schema

### DOM 详解
xml文件多用于信息的描述，所以在得到一个xml文档之后按照xml中的元素取出对应的信息就是xml的解析。Xml解析有两种方式，一种是DOM解析，另一种是SAX解析，两种操作的方式如图。
基于DOM解析的xml分析器是将其转换为一个对象模型的集合，用树这种数据结构对信息进行储存。通过DOM接口，应用程序可以在任何时候访问xml文档中的任何一部分数据，因此这种利用DOM接口访问的方式也被称为随机访问。
因为DOM分析器将整个xml文件转换为了树存放在内存中，当文件结构较大或者数据较复杂的时候，这种方式对内存的要求就比较高，且对于结构复杂的树进行遍历也是一种非常耗时的操作。不过DOM所采用的树结构与xml存储信息的方式相吻合，同时其随机访问还可利用，所以DOM接口还是具有广泛的使用价值。

DOM解析中有以下4个核心操作接口

Document：此接口代表了整个xml文档，表示为整个DOM的根，即为该树的入口，通过该接口可以访问xml中所有元素的内容。其常用方法如下。

Node：此接口在整个DOM树中有着举足轻重的地位，DOM操作的核心接口都继承于Node(Document、Element、Attr)。在DOM树中，每一个Node接口代表了一个DOM树节点

NamedNodeMap：此接口表示一组节点和其唯一名称对应的一一关系，主要用于节点属性的表示

NodeList：此接口表示一个点的集合，一般用于有序关系的一组节点。


https://blog.csdn.net/a1353206432/article/details/80583302?ops_request_misc=%25257B%252522request%25255Fid%252522%25253A%252522160805272619724848154383%252522%25252C%252522scm%252522%25253A%25252220140713.130102334..%252522%25257D&request_id=160805272619724848154383&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-4-80583302.nonecase&utm_term=XML%20DOM
