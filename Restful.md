什么是REST
　　REST本身并没有创造新的技术、组件或服务，而隐藏在RESTful背后的理念就是使用Web的现有特征和能力， 更好地使用现有Web标准中的一些准则和约束。虽然REST本身受Web技术的影响很深， 但是理论上REST架构风格并不是绑定在HTTP上，只不过目前HTTP是唯一与REST相关的实例。 所以我们这里描述的REST也是通过HTTP实现的REST。

资源与URI
统一资源接口
资源的表述
资源的链接
状态的转移

　　2. 1 资源与URI

　　REST全称是表述性状态转移，那究竟指的是什么的表述? 其实指的就是资源。任何事物，只要有被引用到的必要，它就是一个资源。资源可以是实体(例如手机号码)，也可以只是一个抽象概念(例如价值) 。下面是一些资源的例子：

某用户的手机号码
某用户的个人信息
最多用户订购的GPRS套餐
两个产品之间的依赖关系
某用户可以办理的优惠套餐
某手机号码的潜在价值

要让一个资源可以被识别，需要有个唯一标识，在Web中这个唯一标识就是URI(Uniform Resource Identifier)。
URI既可以看成是资源的地址，也可以看成是资源的名称。如果某些信息没有使用URI来表示，那它就不能算是一个资源， 只能算是资源的一些信息而已。
URI的设计应该遵循可寻址性原则，具有自描述性，需要在形式上给人以直觉上的关联。这里以github网站为例，给出一些还算不错的URI：


五、如何设计Restful风格的API

1.路径设计

—>在RESTful架构中，每个网址代表一种资源（resource），所以网址中不能有动词，只能有名词，而且所用的名词往往与数据库的表名对应，一般来说，数据库中的表都是同种记录的”集合”（collection），所以API中的名词也应该使用复数。
—>举例来说，有一个API提供动物园（zoo）的信息，还包括各种动物和雇员的信息，则它的路径应该设计成下面这样。

2.HTTP动词设计

对于资源的具体操作类型，由HTTP动词表示，常用的HTTP动词如下：

请求方式 含义
GET 获取资源（一项或多项）
POST 新建资源
PUT 更新资源（客户端提供改变后的完整资源）
DELETE 删除资源
如何通过路径和http动词获悉要调用的功能：

请求方式 含义
GET /zoos 列出所有动物园
POST /zoos 新建一个动物园
GET /zoos/ID 获取某个指定动物园的信息
PUT /zoos/ID 更新某个指定动物园的信息（提供该动物园的全部信息）
DELETE /zoos/ID 删除某个动物园
GET /zoos/ID/animals 列出某个指定动物园的所有动物
DELETE /zoos/ID/animals/ID 删除某个指定动物园的指定动物

普通Api和RESTful Api的区别


RESTful：一种软件架构风格，设计风格而不是标准，只是提供了一组设计原则和约束条件。它主要用于客户端和服务器交互类的软件。基于这个风格设计的软件可以更简洁，更有层次，更易于实现缓存等机制。

RESTful风格更能清晰的去告诉别人这个操作是做什么。你当然可以使用get方式取删除数据，但是没有delete来的清晰。

RESTful Api即满足RESTful风格设计的API：

restful使用http code代表状态
resetful最重要的是资源思想，他之所以灵活，是因为他很少参与业务逻辑，只定义资源操作。

https://blog.csdn.net/wl_1013/article/details/81049691?ops_request_misc=%25257B%252522request%25255Fid%252522%25253A%252522161318271416780265415231%252522%25252C%252522scm%252522%25253A%25252220140713.130102334..%252522%25257D&request_id=161318271416780265415231&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-81049691.pc_search_result_no_baidu_js&utm_term=RESTful

REST：Representational State Transfer（表象层状态转变），如果没听说过REST，你一定以为是rest这个单词，刚开始我也是这样认为的，后来发现是这三个单词的缩写，即使知道了这三个单词理解起来仍然非常晦涩难懂。如何理解RESTful架构，最好的办法就是深刻理解消化Representational State Transfer这三个单词到底意味着什么。

1.每一个URI代表一种资源；

2.客户端和服务器之间，传递这种资源的某种表现层；

3.客户端通过四个HTTP动词（get、post、put、delete），对服务器端资源进行操作，实现”表现层状态转化”。

