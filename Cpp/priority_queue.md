#### 头文件
`#include<queue>`

#### 定义
`priority_queue<int> p;`

#### 优先输出大数据
```cpp
priority_queue<Type, Container, Functional>
```
- Type为数据类型, int
- Container为保存数据的容器，vector<int>
- Functional为元素比较方式。greater<int> 

如果不写后两个参数，那么容器默认用的是vector，比较方式默认用operator<，也就是优先队列是大顶堆，队头元素最大。

- queue，stack是基于deque实现的，都是顺序容器。
  - deque支持随机访问，queue和stack由于容器特性屏蔽了随机访问（operator []）。

- priority_queue是基于vector实现的，底层数据结构是堆。
  - vector支持随机访问，priority_queue由于容器特性屏蔽了随机访问（operator []）。

一般需要用到最小堆、最大堆时可以用priority_queue来实现。

一般需要用到队列时可以用queue来实现。

一般需要用到栈时可以用stack来实现。

一般需要用到双向队列时可以用deque来实现。


#### heap vs priority queue
heap并不属于STL容器组件，它分为 max heap 和min heap，在缺省情况下，max-heap是优先队列（priority queue）的底层实现机制。而这个实现机制中的max-heap实际上是以一个vector表现的完全二叉树（complete binary tree）。STL在<algorithm.h>中实现了对存储在vector/deque 中的元素进行堆操作的函数，包括make_heap, pop_heap, push_heap, sort_heap
* Priority queues can be implemented by heaps, and heaps can be implemented by arrays.

优先队列(priority_queue)首先是一个queue，那就是必须在末端推入，必须在顶端取出元素。除此之外别无其他存取元素的途径。内部元素按优先级高低排序，优先级高的在前。缺省情况下，priority_heap利用一个max-heap完成，后者是一个以vector表现的完全二叉树。我们说优先队列不是一个STL容器，它以底部容器而实现，修改了接口，形成另一种性质，这样的东西称之为适配器（adapter）。

自对自定义的数据类型自定义优先级，

1.通过自定义operator<操作符来比较元素中的优先级。
2.自定义一个比较“类”，重载括号，operator ()，这这种方式可以由less“继承”。


1.为什么使用deque作为stack和queue的底层结构？

首先deque的优点是头部和尾部操作方便，效率可以达到O(1)，缺点是因为deque的底层空间是不连续的，之所以看起来是连续的都是迭代器的功劳

而stack和queue是作为容器适配器来使用的，其不需要遍历，只需要在两端进行操作即可，刚好避开deque的缺陷。

