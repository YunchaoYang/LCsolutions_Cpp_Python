https://blog.csdn.net/zstarwalker/article/details/88367509?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_baidulandingword-3&spm=1001.2101.3001.4242
DICOMweb能做什么？

那么DICOMweb能做些什么呢？参考下图，可以用一句话来概括，DICOMweb定义了在互联网上基于RESTful接口，如何进行DICOM影像的查询、获取、存储和工作流程协同，以及如何查询一台服务对外提供哪些接口。

QIDO-RS，DICOM查询服务
QIDO-RS请求必须使用RESTful中的GET操作。

WADO-RS，DICOM获取服务
WADO-RS请求必须使用RESTful中的GET操作。

Capabilities， DICOMweb服务能力查询


什么是 PACS ？
PACS 在医学领域是 Picture Archiving and Communication System 的缩写，指的是医学影像存储和通信系统。PACS 存储要求更小，同时为多种模态的医学影像提供方便的访问接口。

什么是 PACS 组件 ？
PACS 组件包括：
用于存储，索引和检索医学影像或报告的电子档案系统
用于查询和处理医学影像的工作站，如基于Web的查看器，手机、平板或者电脑上的客户端，或者是桌面工作站。
安全的传输网络
获取影像的仪器





传统的DICOM标准中，用于点对点数据交换的DIMSE Services无法适用于互联网.相比于当前互联网普遍采用的RESTFul架构，DIMSE显得有些“笨重”，不够轻盈和灵活。
同时，DIMSE从起源上，是面向局域网应用设计的，它往往要求通讯双方具有固定且已知的IP，并且在开始正式传输数据前，通讯双方要先完成一套稍显复杂的“握手互认”过程。
此外，互联网通讯具有高延迟、高并发特点，这些也是DIMSE不能很好支持的。

DIMSE：DICOM Message Service Element（DICOM 消息服务元素）

DIMSE-C：DICOM Message Service Element - Composite（复合 DICOM 消息服务元素）

DIMSE-N：DICOM Message Service Element - Normalized（标准化的 DICOM 消息服务元素）

DIMSE-service-user：that part of an application entity that makes use of the DICOM Message Service Element.（使用 DICOM 消息服务元素的应用实体部分）

https://blog.csdn.net/weixin_34405557/article/details/89628383?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control
