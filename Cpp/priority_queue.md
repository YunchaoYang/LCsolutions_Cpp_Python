###头文件
`#include<queue>`
###定义
`priority_queue<int> p;`
### 优先输出大数据
```cpp
priority_queue<Type, Container, Functional>
```

Type为数据类型， Container为保存数据的容器，Functional为元素比较方式。

如果不写后两个参数，那么容器默认用的是vector，比较方式默认用operator<，也就是优先队列是大顶堆，队头元素最大。
