https://blog.csdn.net/weixin_35829279/article/details/114329326?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162093918216780271539880%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=162093918216780271539880&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-3-114329326.pc_search_result_cache&utm_term=lambda%E5%87%BD%E6%95%B0+cpprestsdk

主要有三部分组成，threadpool，scheduler，task。

pplx只着重实现了task部分功能，scheduler跟threadpool只是简略实现。

- threadpool主要依赖boost.asio达到跨平台的目标
- cpprestsdk的 io操作同时也依赖这个threadpool。
- 默认的scheduler只是简单地将work投递到threadpool进行分派。
- 用户可以根据自己需要，实现scheduler_interface，提供复杂的调度。

每个task关联着一个_Task_impl实现体，一个_TaskCollection_t(唤醒事件，后继任务队列，这个队列的任务之间的关系是并列的)，还有一个_PPLTaskHandle代码执行单元。

task，并行执行的单位任务。通过scheduler将代码执行单元调度到线程去执行。

task提供类似activeobject模式的功能，可以看作是一个future，通过get()同步阻塞等待执行结果。

task提供拓扑模型，通过then()创建后续task，并作为后继执行任务。注意的是每个task可以接受不限数量的then()，这些后继任务之间并不串行。例 task().then().then()串行，(task1.then(), task1.then())并行。一个任务在执行完成时，会将结果传递给它的所有直接后继执行任务。

此外，task拓扑除了then()函数外，还可以在执行lambda中添加并行分支，然后可以在后继任务中同步这些分支。

也就是说后继任务同步原本task拓扑外的task拓扑才能继续执行。

1 auto fork0 =

2 task([]()->task{
3 auto fork1 =

4 task([]()->task{
5 auto fork2 =

6 task([](){
7 // do your fork2 work

8

9 });

10 // do your fork1 work

11

12 returnfork2;

13 }).then([](task& frk2){ frk2.wait(); }); // will sync fork2

14 // do your fork0 work

15

16 returnfork1;

17 }).then([](task& frk1){ frk1.wait(); }); // will sync fork1

18 fork0.wait(); // sync fork1, fork2

上面的方式有一个问题，如果里层的fork先完成，将不要阻塞线程，但是外层fork先完成就不得不阻塞线程等待内层fork完成。

所以可以用when_all

task >([]()->task{
std::vector >forks;

forks.push_back( task([]() { /* do fork0 work */}) );

forks.push_back( task([]() { /* do fork1 work */}) );

forks.push_back( task([]() { /* do fork2 work */}) );

forks.push_back( task([]() { /* do fork3 work */}) );

returnwhen_all(std::begin(forks), std::end(forks));

}).then([](taskforks){
forks.wait();

}).wait();

通过上面的方式，也可以在lambda中，将其它task拓扑插入到你原来的task拓扑。

task结束，分两种情况，完成以及取消。取消执行，只能在执行代码时通过抛出异常，task并没有提供取消的接口。任务在执行过程中抛出的异常，就会被task捕捉，并暂存异常，然后取消执行。异常在wait()时重新抛出。下面的时序分析可以看到全过程 。

值得注意的是，PPL中task原本的设计是的有Async与Inline之分的。在_Task_impl_base::_Wait()有一小段注释说明

// If this task was created from a Windows Runtime async operation, do not attempt to inline it. The

// async operation will take place on a thread in the appropriate apartment Simply wait for the completed

// event to be set.

也就是task除了由scheduler调度到线程池分派执行，还可以强制在wait()函数内分派执行，后继task也不必再次调度而可以在当前线程继续分派执行。但是pplx没有实现

class_TaskCollectionImpl

{
...

void_Cancel()

{
// No cancellation support

}

void_RunAndWait()

{
// No inlining support yet

_Wait();

}

下面是对task的时序分析。
后继任务被调度到线程池继续分派执行。

这里顺便讨论一个开销，在window版本中，每个task都有一个唤醒事件，使用事件内核对象，都要创建释放一个内核对象，在高并行任务时，可能会消耗过多内核对象，消耗句柄数。

并且continuation后继任务，在默认scheduler调度下，不会在同一线程中分派，所有后继任务都会简单投递到线程池。由线程池去决定分派的线程。所以由then()串行起来的任务可能会由不同的线程顺序分派，从而产生开销。因为pplx并没有实现 Inline功能，所有task都会视作Async重新调度到线程池。

自 VS2010 起，微软就在 CRT 中集成了并发运行时（Concurrency Runtime），并行模式库（PPL，Parallel Patterns Library）是其中的一个重要组成部分。
7 年过去了，似乎大家都不怎么Care这个事情，相关文章少少且多是蜻蜓点水。实际上这个库的设计相当精彩，胜过 C++ 标准库中 future/promise/async 系列许多，所以计划写一个系列探讨 PPL 在实际项目中应用中的各种细节。

从最简单的代码开始，先演示下如何使用 task 类和 lambda 表达式创建一个并行任务：

``` cpp
// final_answer.cpp
// compile with: /EHsc 

#include <ppltasks.h>
#include <iostream>

using namespace concurrency;
using namespace std;

int main(int argc, char *argv[])
{
    task<int> final_answer([]
    {
        return 42;
    });
    
    cout << "The final answer is: " << final_answer.get() << endl;
    
    return 0;
}
```

task 类的原型如下：
``` cpp
template<typename _ReturnType>
class task;
```

其模板参数 `_ReturnType` 是任务返回值类型。 `task:get` 方法则用于获取返回值，原型如下：

``` cpp
_ReturnType get() const;
```

task 类的构造函数ctor原型：

``` cpp
template<typename T>
__declspec(noinline) explicit task(T _Param);
// 参数 _Para
```
参数 `_Para` 可以是 lambda 表达式、函数对象、仿函数、函数指针等可以以 `_Param()` 形式调用的类型，因此可以使用各种灵活的方式构造 task 对象，其中 lambda 表达式无疑是最方便常用的一种。


