### XML Schema Definition (XSD).
The purpose of an XML Schema is to define the legal building blocks of an XML document:

* the elements and attributes that can appear in a document
* the number of (and order of) child elements
* data types for elements and attributes
* default and fixed values for elements and attributes

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


```xml
<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

<xs:element name="note">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="to" type="xs:string"/>
      <xs:element name="from" type="xs:string"/>
      <xs:element name="heading" type="xs:string"/>
      <xs:element name="body" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>

</xs:schema>
```
