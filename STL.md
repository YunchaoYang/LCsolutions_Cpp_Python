C++ STL（标准模板库）是一套功能强大的 C++ 模板类，提供了通用的模板类和函数，这些模板类和函数可以实现多种流行和常用的算法和数据结构，
如向量、链表、队列、栈。


| 组件	| 描述 |
|--------|-----------|
容器（Containers）	|容器是用来管理某一类对象的集合。C++ 提供了各种不同类型的容器，比如 deque、list、vector、map 等。
算法（Algorithms）|	算法作用于容器。它们提供了执行各种操作的方式，包括对容器内容执行初始化、排序、搜索和转换等操作。
迭代器（iterators）|	迭代器用于遍历对象集合的元素。这些集合可能是容器，也可能是容器的子集。

容器=数据结构+算法。
STL容器
(1) 顺序容器(Sequence Container) 
* Eg. vector  数组。查询快，插入慢。deque 数组,采用哈希映射。list 链表 ,插入快，查询慢。
顺序容器的共同函数
函数	描述
assign(n, elem)	将指定元素elem的n份拷贝加入(赋值)到容器中
assign(begin, end)	将迭代器[beg，end)间的元素赋值给当前容器
push_back(elem)	将元素附加到容器
pop_back()	删除容器尾元素
front	返回容器首元素
back()	返回容器尾元素
insert(position, elem)	将元素插入到容器指定位置

(2) 关联式容器
set  元素不能重复
*头文件: #include <set> 定义：set <data_type> set_name; 如：set <int> s;//默认由小到大排序 如果想按照自己的方式排序，可以重载小于号。
multiset  可以重复
map 存储有序，根据键来排序，不能重复
multimap 与map相同，可以重复
(3). 容器适配器
Eg. stack
头文件: #include <stack> 定义：stack<data_type> stack_name;
如：stack <int> s; 操作： empty() -- 返回bool型，表示栈内是否为空 (s.empty() )

size() -- 返回栈内元素个数 (s.size() )

top() -- 返回栈顶元素值 (s.top() )

pop() -- 移除栈顶元素(s.pop(); )

push(data_type a) -- 向栈压入一个元素 a(s.push(a); )

queue(队列，先进先出)
头文件: #include <queue>
 
定义：queue <data_type> queue_name; 如：queue <int> q; 操作： empty() -- 返回bool型，表示queue是否为空 (q.empty() )

size() -- 返回queue内元素个数 (q.size() )

front() -- 返回queue内的下一个元素 (q.front() )

back() -- 返回queue内的最后一个元素(q.back() )

pop() -- 移除queue中的一个元素(q.pop(); )

push(data_type a) -- 将一个元素a置入queue中(q.push(a); )


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
