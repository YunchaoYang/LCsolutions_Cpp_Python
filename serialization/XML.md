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

```dtd
<!ELEMENT 班级 (学生+)>
<!ELEMENT 学生 (名字,年龄,介绍)>
<!ELEMENT 名字 (#PCDATA)>
<!ELEMENT 年龄 (#PCDATA)>
<!ELEMENT 介绍 (#PCDATA)>
```

### XML文件约束- XML Schema
