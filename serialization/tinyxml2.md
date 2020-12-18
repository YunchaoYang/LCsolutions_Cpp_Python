源码 https://github.com/leethomason/tinyxml2

简单地说，TinyXML解析一个XML文档并由此生成一个可读可修改可保存的文档对象模型（DOM）。

tinyXML2是一个开源、简单、小巧、高效的C++ XML解析器，它只有一个.h文件和一个.cpp文件组成，可以轻松集成到其它程序中。

它解析XML文档并从中构建可以读取、修改和保存的文档对象模型(Document Object Model, DOM)。
它不能解析DTD(Document Type Definitions, 文档类型定义)或XSL(eXtensible Stylesheet Language, 扩展样式表语言)。

由于 XML 的树状结构，TinyXML2 将 XML 的节点抽象为 XMLNode，XML 中除了把属 性 key-value 抽象为 XMLAttribute 类型外，其余的都看作 XMLNode 的子类，
首先将整个 XML 文档抽象为 XMLDocument，将声明部分抽象为 XMLDeclaration，将注释抽象为 XMLComment，将元素抽象为 XMLElement，将文本抽象为 XMLText。

* XMLNode - 是几乎 XML 所有元素(XMLAttribute 除外)的基类，XML 本质是一种树形结构，而 整个 XML 就是由许多的节点(XMLNode)组成，
在 TinyXML2 中每个 XMLNode 节点都 保存了父亲、前驱、后继、孩子头节点和孩子尾节点信息，便于查询、插入、检 索。
XMLNode 的其他实体类把构造函数定义为 protected，不能被外部实例化，这样保证使用 XMLDocument 进行内存的管理，避免产生内存泄漏的风险。

* XMLDocument - 代表 XML 整个实体，TinyXML2 中只有 XMLDocument 类可以被实例化，其他的类必 须通过 XMLDocument 提供的 new 方法进行实例化，而不能直接实例化
* XMLElementXMLElement 类是 XMLNode 中最重要的一个类，其存储方式有<foo/>和<foo></foo> 两 种 形 式 ， 它 包 含 了 一 个 XMLAttribute 的 根 指 针 ， 
这 个 root 指 针 指 向 XMLAttribute 的第一个属性键值对。
* XMLAttribute - 解析 XML 的属性的类，XML 中的属性都与 XML 的 Element 绑定，并且为 key-value 类型。
* XMLHandle        主要用来访问元素。
* XMLDeclaration - XML 中 声明，`"<? declaration ?>"`
* XMLUnknown       存储形式为"<! unknown>"。
* XMLText 主要是处理 XML 文本的类，文本信息又分为 CDATA 和普通文本。CDATA 是有专属的 开始字符"<![CDATA["，而普通的文本存储形式如">text<"。
* XMLVisitor 访问者模式的基类，它主要定义了访问者的接口，而在 XMLNode 的子类的 accept 方法中调用这些方法来完成对自身的访问。
* XMLPrinter 是 XMLVisitor 类的子类，主要实现的写 XML 的功能，其提供了两种书写方式，一 是构建 XMLDocument，二是直接 push 字段。

https://blog.csdn.net/jenie/article/details/106729883?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control

https://blog.csdn.net/tiankongtiankong01/article/details/85001529?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control

https://blog.csdn.net/silangquan/article/details/8491154?utm_medium=distribute.pc_relevant_download.none-task-blog-searchFromBaidu-1.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-searchFromBaidu-1.nonecas

