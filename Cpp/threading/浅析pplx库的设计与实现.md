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


接下来我们修改上面的程序，打印出线程 id 以便观察并行任务的执行情况。

``` cpp
#include <iostream>
#include <thread>

using namespace concurrency;
using namespace std;

int main(int argc, char *argv[])
{
    cout << "Major thread id is: " << this_thread::get_id() << endl;

    task<int> final_answer([]
    {
        cout << "Thread id in task is:" << this_thread::get_id() << endl;
        return 42;
    });
    
    cout << "The final answer is: " << final_answer.get() << endl;
    
    return 0;
}
```
注意两个线程 id 是相同的，很有些意外，任务是在主线程执行的而非预计的其他后台工作线程。实际上这是 PPL 的优化策略造成的。

再修改下程序，在 task 对象构造完成后加一个 sleep 调用挂起当前线程一小段时间：

``` cpp 
int main(int argc, char *argv[])
{
    cout << "Major thread id is: " << this_thread::get_id() << endl;

    task<int> final_answer([]
    {
        cout << "Thread id in task is:" << this_thread::get_id() << endl;
        return 42;
    });
    
    this_thread::sleep_for(chrono::milliseconds(1));

    cout << "The final answer is: " << final_answer.get() << endl;
    
    return 0;
}
```

PPL 使用了一个新的线程执行并行任务，实际上 PPL 是使用了线程池来执行被调度到的任务。

而在上一个程序中，由于没有 sleep，也没有其他耗时的代码，执行到 task::get 方法时并行任务尚未被调度所以直接在当前线程执行该任务，这样就节省了两次线程切换的开销。

MSDN 中对 task::wait 方法的说明：

It is possible for wait to execute the task inline, if all of the tasks dependencies are satisfied, and it has not already been picked up for execution by a background worker.

task::get 方法的内部实现会先调用 task::wait 方法所以有同样的效果。

 
本章小结：

1. task 类对象构造完成后即可被调度执行；

2. 并行有可能被优化在当前线程执行；

# 创建并运行任务
可以通过多种途径创建任务：
``` cpp
 //构造函数
auto task = pplx::task<int>([](){
    return 10;
});
 
//lambda
auto task = []()->pplx::task<int>{
    return pplx::task_from_result(10);
};
 
//create_task
auto task = pplx::create_task([](){
    return 10;
});
 
//create_task 创建延迟任务
pplx::task_completion_event<int> tce;// task_completion_event 需按值传递
auto task = pplx::create_task(tce);
```

# 可以创建任务链：
pplx::task<std::string> create_print_task(const std::string& init_value)
{
    return pplx::create_task([init_value]() {
        std::cout <<"Current value:" << init_value << std::endl;
        return std::string("Value 2");
    })

    .then([](std::string value) {
        std::cout << "Current value:" << value << std::endl;
        return std::string("Value 3");
    })

    .then([](std::string value) {
        std::cout << "Current value:" << value << std::endl;
        return std::string("Value 4");
    });
}

# 使用task.get()或者task.wait()执行任务：
* 阻塞方式get(): 阻塞直到任务执行完成，并返回任务结果，当任务取消时，抛出task_canceled异常，发生其它异常也会被抛出；
* 非阻塞方式wait()：等待任务到达终止状态，然后返回任务状态：completed、canceled，如果发生异常会被抛出。
``` cpp 
void test_task_chain()
{
    auto task_chain = create_print_task("Value 1");
    task_chain.then([](std::string value) {
        std::cout << "Result value: " << value << std::endl;
        return value;
    })

    // process exception
    .then([](pplx::task<std::string> previousTask) {
        try {
            previousTask.get();
        }
        catch (const std::exception& e) {
            std::cout << "exception: " << e.what() << std::endl;
        }
    })

    .wait();
}
```

# 组任务
可以创建和执行一组任务，根据需要来选择是全部执行再返回，还是执行任一任务就返回。

- `when_all`：返回组任务，只有当所有任务都完成时组任务才会返回成功；如果任一任务被取消或者抛出异常，则组任务会完成并处理取消状态，在组任务`get()`或者`wait()`时抛出异常。如果任务类型为`task<T>`，则组任务类型为`task<vector<T>>`。
- `when_any`：返回组任务，当任一任务完成时组任务就会返回成功；如果所有任务都被取消或者抛出异常，则组任务会完成并处理取消状态，并且如果任何任务发生异常，在组任务get或者wait时抛出异常。如果任务类型为task<T>，则组任务类型为task<T, size_t>，size_t 返回完成任务的索引。

```cpp 
void test_group_tasks()
{
    auto sleep_print = [](int seconds, const std::string& info) {
        if (seconds > 0) {
            sleep(seconds);
        }

        std::cout << info << std::endl;
    };

    auto/*std::array<pplx::task<int>, 3>*/ tasks = {
        pplx::create_task([sleep_print]() -> int { sleep_print(2, "Task 1"); return 1; }),
        pplx::create_task([sleep_print]() -> int { sleep_print(2, "Task 2"); return 2; }),
        pplx::create_task([sleep_print]() -> int { sleep_print(4, "Task 3"); return 3; })
    };

    {
        std::cout << "=== when_all ===" << std::endl;

        auto joinTask = pplx::when_all(std::begin(tasks), std::end(tasks));
        auto result = joinTask.wait();
        std::cout << "All joined thread. result: " << result << std::endl;
    }

    {
        std::cout << "=== when_any ===" << std::endl;

        auto joinTask = pplx::when_any(std::begin(tasks), std::end(tasks))
        .then([](std::pair<int, size_t> result) {
            std::cout << "First task to finish returns "
                  << result.first
                  << " and has index "
                  << result.second << std::endl;
        });

        auto result = joinTask.wait();
        std::cout << "Any joined thread. result: " << result << std::endl;
    }
}
```

# 取消任务
cancellation_token_source 通过封装一个 cancellation_token 指针来提供取消操作，通过cancellation_token.is_canceled()在执行任务的过程中判断任务是否要被取消。

示例中的任务会循环执行，直到显式取消任务：
``` cpp
void test_cancellation()
{
    pplx::cancellation_token_source cts;
    std::cout << "Creating task..." << std::endl;

    auto task = pplx::create_task([cts]{
        bool moreToDo = true;
        while (moreToDo) {
           if (cts.get_token().is_canceled()) {
               return;
           }
           else {
               moreToDo = []()->bool {
                   std::cout << "Performing work at " << now() << std::endl;
                   sleep(1);
                   return true;
               }();
           }
        }
    });

    sleep(3);

    std::cout << "Canceling task... " << now() << std::endl;
    cts.cancel();

    std::cout << "Waiting for task to complete... " << now() << std::endl;
    task.wait();

    std::cout << "Done. " << now() << std::endl;
}
————————————————
版权声明：本文为CSDN博主「飘飘白云」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/kesalin/article/details/86713720
```

当要在异步任务链中支持取消时，需要将cancellation_token作为构造task的参数传递，然后结合task.wait()判断是否要取消：
```
void test_cancellation_async()
{
    pplx::cancellation_token_source cts;
    auto task = pplx::task<void>([cts]() {
        std::cout << "Cancel continue_task" << std::endl;
        cts.cancel();
    })

    .then([]() {
        std::cout << "This will not run" << std::endl;
    }, cts.get_token());

    try {
        if (task.wait() == pplx::task_status::canceled) {
            std::cout<<"Taks has been canceled"<<std::endl;
        }
        else {
            task.get();
        }
    }
    catch (const std::exception& e) {
        std::cout << "exception: " << e.what() << std::endl;
    }
}
```
# 处理异常

之前说过如果任务发生异常，会在get或者wait时抛出，但是如果希望在异步任务链中判定之前执行是否发生异常做出操作时，可以采用另外的方式。
当使用task.then时一般是这样写的：
``` cpp
task<T>.then([](T t){
     //处理任务结果t
})
```
这时候进入then时之前的任务已经执行完成了，task.then有另外一种写法，能够在then时并没有执行任务：
``` cpp
task<T>.then([](task<T> task){
       try 
       {
              task.get(); //使用get或者wait执行任务
       }
       catch(...)
       {
           //处理异常
       }
})
```
# C++ concurrency::task实现异步编程
主要使用task class 及其相关类型和函数，它们都包含在 concurrency 命名空间中且在 <ppltasks.h> 中定义。concurrency::task 类是一个通用类型，但是当使用 /ZW 编译器开关（对于 Windows 运行时应用和组件而言是必需的）时，任务类会封装 Windows 运行时异步类型，以便更容易地完成以下工作：
1.将多个异步和同步操作结合在一起
2.在任务链中处理异常
3.在任务链中执行取消
4.确保单个任务在相应的线程上下文或单元中运行

task::then 函数创建并返回的任务称为延续。用户提供的 lambda 输入参数（在此情况下）是任务操作在完成时产生的结果。
它与你在直接使用 IAsyncOperation 接口时通过调用 IAsyncOperation::GetResults 检索到的值相同。
task::then 方法立即返回，并且其代理直至异步工作成功完成后才运行。 

# 创建任务链

在异步编程中，常见的做法是定义一个操作序列，也称作任务链，其中每个延续只有在前一个延续完成后才能执行。在某些情况下，上一个（或先行）任务会产生一个被延续接受为输入的值。通过使用 task::then 方法，你可以按照直观且简单的方式创建任务链；该方法返回一个 task<T>，其中 T 是 lambda 函数的返回类型。你可以将多个延续组合到一个任务链中： myTask.then(…).then(…).then(…);
当延续创建一个新的异步操作时，任务链尤其有用；此类任务称为异步任务。
    
    
# Lambda 函数返回类型和任务返回类型

在任务延续中，lambda 函数的返回类型包含在 task 对象中。如果该 lambda 返回 double，则延续任务的类型为 task<double>。 
    
    https://ninesun.blog.csdn.net/article/details/75735001?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EOPENSEARCH%7Edefault-8.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EOPENSEARCH%7Edefault-8.control
