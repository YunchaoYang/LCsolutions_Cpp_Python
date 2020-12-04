### XML Schema Definition (XSD).
The purpose of an XML Schema is to define the legal building blocks of an XML document:

* the elements and attributes that can appear in a document
* the number of (and order of) child elements
* data types for elements and attributes
* default and fixed values for elements and attributes

XML Schema语言也被称为XML Schema Definition (XSD)，它的作用是定义一份XML文档的合法组件群（XML文档的结构），就像DTD的作用一样。 XML Schema以XML语言作为基础，也可以说XML Schema自身就是XML的一种应用。

Schema按照xml文件的规范，所以需要添加：<?xml version="1.0" encoding="utf-8" standalone="yes"?>。
从本质上来说，XML文档只能保存文本格式的数据，例如，length属性的值1.2和amount元素的内容2，都是字符形式，
然而，为了让XML文档能够进行数据交换（如与数据库或程序内存中的数据进行交换），需要人为地为XML文档中的数据
定义一些数据类型，以方便对元素内容和属性值进行验证。

* 什么是Schema？ 

在计算机软件中，Schema这个词在不同的应用中有不同的含义，可以翻译为：架构、结构、规则、模式等。
在XML中，Schema指的是定义和描述XML文档的规则，翻译为模式。

DOM（Document Object Model）是在分析时，一次性地将整个XML文档进行分析，并在内存中形成对应的树结构

* 元素和属性的声明

元素和属性分别通过http://www.w3.org/2001/XMLSchema名称空间中的element和attribute元素来声明.

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified" targetNamespace=“”>......</xs:schema>
```

使用命名空间:xmlns:xs ="..."  其中命名空间的地址是固定不变的。


![Schema基本内容导图](https://img-blog.csdn.net/20131128212218750?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvemhhbmdfeGlueGl1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

#### hello.xml
```xml
<?xml version="1.0"?>   
<hello>World</hello>  
```

#### hello.xsd 
- XML Schema for hello.xml

```xml
<?xml version="1.0" encoding="utf-8"?>   
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">   
    <xs:element name="hello" type="xsd:string">   
</xs:schema>  
```
- Interpretation
  - XML申明`<?xml version="1.0" encoding="utf-8"?>`。
  - 根节点 `<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"> `, ：其中xs是命名空间，schema是根节点名。
      注意xs:schema与xmlns:xs中的xs要完全一样（名称可以任意，只要一样就可以），它标明以xs:开头的节点元素是http://www.w3.org/2001/XMLSchema定义的元素。
  - element元素  `<xs:element name="hello" type="xs:string">`, name属性用来定义它所描述的XML文档中的节点名。type是表示该节点的值的类型。这里的xs:string（string类型）表示hello节点不能包含子节点，不能包含属性，它的内容值应该是string类型。
  - </xs:schema>完成整个XML Schema描述。

- xsd是什么文件，作用是什么？
  - XSD是指XML结构定义 ( XML Schemas Definition )XML Schema 是DTD的替代品。XML Schema语言也就是XSD。XML Schema描述了XML文档的结构。可以用一个指定的XML Schema来验证某个XML文档，以检查该XML文档是否符合其要求。
  - 1 个XML Schema会定义: ①定义可出现在文档中的元素 ②定义可出现在文档中的属性 ③定义哪个元素是子元素 ④定义子元素的次序 ⑤定义子元素的数目 ⑥定义元素是否为空，或者是否可包含文本 ⑦定义元素和属性的数据类型 ⑧定义元素和属性的默认值以及固定值
  - XSD元素可分为简单元素和复杂元素。
    - 简单元素
       - 例如XML文档：<Name>张三</Name>; 用XSD可写为 <xs:element name="Name" type="xs:string"/>

          - 如果要指定元素的默认值或固定值，默认值用 default定义，固定值用 fixed定义。
            - <xs:element name="Name" type="xs:string" default="张三"/>
            - <xs:element name="Name" type="xs:string" fixed="张三"/>

    - 复杂元素
       - 
  - XML Schema的优点: 
    1. XML Schema基于XML,没有专门的语法 
    2. XML可以象其他XML文件一样解析和处理 
    3. XML Schema支持一系列的数据类型(int、float、Boolean、date等) 
    4. XML Schema提供可扩充的数据模型。 
    5. XML Schema支持综合命名空间 
    6. XML Schema支持属性组。
