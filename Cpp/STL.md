C++ STL（Standard Template Library 标准模板库）是一套功能强大的 C++ 模板类，提供了通用的模板类和函数，这些模板类和函数可以实现多种流行和常用的算法和数据结构，
如向量、链表、队列、栈。

http://www.cplusplus.com/reference/stl/

| 组件	| 描述 |
|--------|-----------|
容器（Containers）	|容器是用来管理某一类对象的集合。C++ 提供了各种不同类型的容器，比如 deque、list、vector、map 等。
算法（Algorithms）|	算法作用于容器。它们提供了执行各种操作的方式，包括对容器内容执行初始化、排序、搜索和转换等操作。
迭代器（iterators）|	迭代器用于遍历对象集合的元素。这些集合可能是容器，也可能是容器的子集。

容器=数据结构+算法。
STL容器

容器类

| STL Container	Header | 	Applications| 
| --------------|-------------- | 
vector	<vector>	| 直接访问任意元素，快速插入、删除尾部元素| 
deque	<deque>	| 直接访问任意元素，快速插入、删除头部和尾部元素| 
list	<list>	| 快速插入、删除任意位置元素| 
set	<set>	| 快速查询元素，无重复关键字| 
multiset	<set>	| 与set相同，但允许重复关键字| 
map	<map>	| Key/value pair mapping (键值对映射)。不允许重复关键字，使用关键字快速查询元素| 
multimap	<map>	| 与map相同，但允许重复关键字| 
stack	<stack>	| 后进先出容器.| 
queue	<queue>	| 先进先出容器| 
priority_queue	<queue>	| 高优先级元素先删除| 
 
 所有容器共同函数

|Functions	Description| |
| --------------|-------------- | 
|non-argconstructor |无参构造函数	构造一个空容器|
|constructor with args|带参构造函数	每个容器都有多个带有参数的构造函数|
|copy constructor |拷贝构造函数	创建一个容器，从一个已有的同类型容器中复制元素|
|destructor |析构函数	容器销毁后执行清理工作|
|empty()	|若容器中没有元素则返回空|
|size()|	返回容器中的元素数目|
|operator=	|将容器内容复制到另一个容器|
|Relational operators(<, <=, >, >=, ==, and !=)	|顺序比较两个容器中的对应元素，来确定大小关系|

## 顺序容器(Sequence Container) 
* Eg. vector  数组。查询快，插入慢。deque 数组,采用哈希映射。list 链表 ,插入快，查询慢。

顺序容器的共同函数

|函数 |	描述|
| ----- | ----- | 
|assign(n, elem)|	将指定元素elem的n份拷贝加入(赋值)到容器中|
| assign(begin, end)| 	将迭代器[beg，end)间的元素赋值给当前容器| 
| push_back(elem)| 	将元素附加到容器| 
| pop_back()	| 删除容器尾元素| 
| front	| 返回容器首元素| 
| back()	| 返回容器尾元素| 
| insert(position, elem)	| 将元素插入到容器指定位置| 

## 关联式容器(Associative Containers)
关联容器有以下四种：set、multiset、map、multimap。关联容器内的元素是排序的。插入元素时，容器会按一定的排序规则将元素放到适当的位置上，因此插入元素时不能指定位置。

### 集合(set)
#### 由节点组成的红黑树，每个节点都包含着一个元素，节点之间以某种作用于元素对的谓词排列，没有两个不同的元素能够拥有相同的次序 。快速查询元素，无重复关键字。<set>
*头文件: #include <set> 定义：set <data_type> set_name; 如：set <int> s;//默认由小到大排序 如果想按照自己的方式排序，可以重载小于号。
 
#### multiset  可以重复
#### 映射map  由{键，值}对组成的集合，以某种作用于键对上的谓词排列。Key/value pair mapping(键值对映射)。不允许重复关键字，使用关键字快速查询元素 <map>存储有序，根据键来排序，不能重复
#### 多重映射multimap 与map相同，可以重复

关联容器中的共同函数
| 函数 |	描述|
|--------|---------|
|find(key)	|搜索容器中具有key的元素，返回指向该元素的迭代器|
|lower_bound(key)	|搜索容器中具有key的第一个元素，返回指向该元素的迭代器|
|upper_bound(key)	|搜索容器中具有key的最后一个元素，返回指向该元素之后位置的迭代器|
|count(key)|	返回容器中具有key的元素的数目|
默认情况下，关联容器中的元素是从小到大排序（或按关键字从小到大排序）的，而且用<运算符比较元素或关键字大小。因为是排好序的，所以关联容器在查找时具有非常好的性能。

一级容器的通用函数
顺序容器+关联容器= 一级容器

|Functions	|Description |
|-----------------|---------------|
|c1.swap(c2)	|交换两个容器c1和c2的内容|
|c1.max_size()	|返回一个容器可以容纳的最大元素数量|
|c.clear()|	删除容器中的所有元素|
|c.begin()|	返回容器首元素的迭代器|
|c.end()	|返回容器尾元素之后位置的迭代器|
|c.rbegin()|	返回容器为元素的迭代器，用于逆序遍历|
|c.rend()	|返回容器首元素之前位置的迭代器，用于逆序遍历|
|c.erase(beg, end)	|删除容器中从beg到end-1之间的元素。beg和end都是迭代器|


## 容器适配器(Container Adapters)
### 栈(stack) 后进先出 <stack>
　 #include <stack> 　
    stack<ElementType> st;　　　  //创建一个空栈st
　　st.push(ElementType);　　　　  //在栈顶增加元素
　　st.pop();　　　　　　　　　　　  //移除栈顶元素（不会返回栈顶元素的值）
　　st.top();　　　　　　　　　　　   //返回栈顶元素
　　st.empty();　　　　　　　　　　 //判断栈是否为空，空则返回true
　　st.size();　　　　　　　　　　　 //返回栈中元素数目

### 队列(queue) 先进先出 <queue>
　　头文件: #include <queue>
    queue<ElementType> q;　　　　//创建一个空队列
　　q.push(ElementType);　　　　　 //将一个元素置入queue中
　　q.pop();　　　　　　　　　　　　 //从queue中移除一个元素(不会返回队头元素值)
　　q.front();　　　　　　　　　        //返回queue内的第一个元素(也就是第一个被置入的元素)
　　q.back();　　　　　　　　　　　　//返回queue中最后一个元素(也就是最后被插入的元素)
　　q.empty();　　　　　　　　　　　//判断队列是否为空，空则返回true
　　q.size();　　　　　　　　　　　　//返回队列中元素数目。

　　注意：pop()虽然会移除下一个元素，但是并不返回它，front()和back()返回下一个元素但并不移除该元素。

### 优先队列(priority_queue) 
    元素的次序是由作用于所存储的值对上的某种谓词决定的的一种队列 <queue>
　　priority_queue<ElementType> pq;　　　  //创建一个数据越大,优先级越高的队列
　　priority_queue<int, vector<int>, greater<int> > pq;　　//创建一个数据越小,优先级越高的队列
　　pq.push(ElementType);　　　　//将一个元素置入priority_queue中
　　pq.pop();　　　　　　　　　　　//从priority_queue中移除一个元素(不会返回队头元素值)
　　pq.top();　　　　　　　　　　　 //返回priority_queue中优先级最高的元素
　　pq.empty();　　　　　　　　　  //判断priority_queue是否为空，空则返回true
　　pq.size();　　　　　　　　　　　//返回priority_queue中元素数目  



容器都是类模板。它们实例化后就成为容器类。用容器类定义的对象称为容器对象。

例如，vector<int>是一个容器类的名字，vector<int> a;就定义了一个容器对象 a，a 代表一个长度可变的数组，数组中的每个元素都是 int 类型的变量；vector<double> b;定义了另一个容器对象 b，a 和 b 的类型是不同的。本教程后文所说的“容器”，有时也指“容器对象”，读者需要根据上下文自行判别。

任何两个容器对象，只要它们的类型相同，就可以用 <、<=、>、>=、==、!= 进行词典式的比较运算。假设 a、b 是两个类型相同的容器对象，这些运算符的运算规则如下。

a == b：若 a 和 b 中的元素个数相同，且对应元素均相等，则a == b的值为 true，否则值为 false。元素是否相等是用==运算符进行判断的。
a<b：规则类似于词典中两个单词比较大小，从头到尾依次比较每个元素，如果发生 a 中的元素小于 b 中的元素的情况，则a<b的值为 true；如果没有发生 b 中的元素小于 a 中的元素的情况，且 a 中的元素个数比 b 少，a<b的值也为 true；其他情况下值为 false。元素比较大小是通过<运算符进行的。
a != b：等价于 !(a == b)。
a > b：等价于 b < a。
a <= b：等价于 !(b < a)。
a >= b：等价于 !(a < b)。

https://www.cnblogs.com/Malphite/p/10968023.html

| C++ 标准库 | |
|--------|-----------|
| **标准函数库** | 由通用的、独立的、不属于任何类的函数组成的。函数库继承自 C 语言。| 
 | *输入/输出 I/O |  | 
 | *字符串和字符处理 |  | 
 | *数学 |  | 
 | *时间、日期和本地化 | |  
 | *动态分配 |  | 
 | * 其他 |  | 
 | *宽字符函数 | 
| **面向对象类库** | 这个库是类及其相关函数的集合。| 
| 标准的 C++ I/O 类 | 
| String 类 | 
|数值类 |
|STL 容器类 |
|STL 算法 |
|STL 函数对象 |
|STL 迭代器 |
|STL 分配器 |
|本地化库 |
|异常处理类 |
|杂项支持库 |
