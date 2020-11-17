https://cpprocks.com/files/C++-concurrency-cheatsheet.pdf

https://segmentfault.com/a/1190000006691692

https://www.youtube.com/watch?v=9TM5nRHXLPo

CLR线程池分为工作者线程(workerThreads)与I/O线程(completionPortThreads)两种:
工作者线程是主要用作管理CLR内部对象的运作，通常用于计算密集的任务。
I/O(Input/Output)线程主要用于与外部系统交互信息，如输入输出，CPU仅需在任务开始的时候，将任务的参数传递给设备，然后启动硬件设备即可。等任务完成的时候，CPU收到一个通知，一般来说是一个硬件的中断信号，此时CPU继续后继的处理工作。在处理过程中，CPU是不必完全参与处理过程的，如果正在运行的线程不交出CPU的控制权，那么线程也只能处于等待状态，即使操作系统将当前的CPU调度给其他线程，此时线程所占用的空间还是被占用，而并没有CPU处理这个线程，可能出现线程资源浪费的问题。如果这是一个网络服务程序，每一个网络连接都使用一个线程管理，可能出现大量线程都在等待网络通信，随着网络连接的不断增加，处于等待状态的线程将会很消耗尽所有的内存资源。可以考虑使用线程池解决这个问题。

https://blog.csdn.net/tissar/article/details/88359860?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param

https://blog.csdn.net/liujiayu2/article/details/51007199?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160561954019725222402929%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160561954019725222402929&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-3-51007199.pc_first_rank_v2_rank_v28&utm_term=boost+threadpool&spm=1018.2118.3001.4449

* boost::thread的六种使用方法总结
https://blog.csdn.net/jack_20/article/details/79892250?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160561953219725255542202%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160561953219725255542202&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-1-79892250.pc_first_rank_v2_rank_v28&utm_term=boost+thread&spm=1018.2118.3001.4449

- 第一章 等待唤醒机制
  - 1.1 线程间通信
  
   **概念：** 多个线程在处理同一个资源，但是处理的动作（线程的任务）却不相同。
  - 1.2 等待唤醒机制
  
  这是多个线程间的一种协作机制。谈到线程我们经常想到的是线程间的竞争（race），比如去争夺锁，但这并不是故事的全部，线程间也会有协作机制。就好比在公司里你和你的同事们，你们可能存在在晋升时的竞争，但更多时候你们更多是一起合作以完成某些任务。

就是在一个线程进行了规定操作后，就进入等待状态（wait()）， 等待其他线程执行完他们的指定代码过后 再将其唤醒（notify()）;在有多个线程进行等待时， 如果需要，可以使用 notifyAll()来唤醒所有的等待线程。

wait/notify 就是线程间的一种协作机制。

- 调用wait和notify方法需要注意的细节
  - wait方法与notify方法必须要由同一个锁对象调用。
  - wait方法与notify方法是属于Object类的方法的。
  - wait方法与notify方法必须要在同步代码块或者是同步函数中使用。因为：必须要通过锁对象调用这2个方法。

线程就是在进程中的另一个空间里运行的一个函数，因此线程的创建需要传递thread对象，一个无参的可调用物(函数或函数对象)，它必须具有operator()以供线程执行。
如果可调用物(std::fuction or boost::function)不是无参的，那么thread的构造函数也支持直接传递所需的参数，这些参数被拷贝并在发生调用时传递给函数。这是一个非常体贴方便的重载构造函数，比传统的使用void*来传递参数要好很多。thread的构造函数支持最多传递9个参数，这通常足够用了。
在传递参数时需要注意，thread使用的是参数的拷贝，因此要求可调用物和参数类型都支持拷贝。如果希望传递给线程引用值就需要使用ref库进行包装，同时必须保证被引用的对象在线程执行期间一直存在，否则会引发未定义行为。

使用pthread的programmer會用以下方法啟動一個 thread
```cpp
pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine)(void*), void *arg);
```
start_routine就是thread的進入點，arg是要傳入的參數，因為只能傳一個參數，所以我們通常都是把所有參數擠在一個struct裡面......

Boost Thread是在建立thread物件時啟動一個執行緒的

```cpp
boost::thread *mythread = new boost::thread(&threadfunc);
```

跟 一般不同的是，Boost Thread是接受Boost Function來當作thread的進入點，而不是一般的function pointer而已，上面範例的function pointer只是Boost Function的其中一種type而已, 所以, 我們可以輕鬆做到以下這種事：
```cpp
struct MyClass
{
 void threadfunc() {// do something}
};
 
int main()
{
  MyClass m;
  boost::thread mythread(boost::bind(&MyClass::threadfunc, &m));
  // Wait for the thread...
}
```
直 接把non-static member function當成thread的進入點！！在以前pthread的時代，想要跑non-static member function非常麻煩，通常要寫個static wrapper之類的......拜Boost Function和Boost Bind之賜，這兩者與Boost Thread的完美結合，讓C++ programmer的生活更輕鬆了！！


有人可能已經發現了，Boost Thread在創造thread的時候，沒有地方可以傳參數進去阿！！Well，有了Boost Bind，這根本就不是問題，還能做的比以前更好。
```cpp
struct MyClass
{
  void threadfunc(int a, double b) {}
};
 
int main()
{
  MyClass m;
  boost::thread mythread(
      boost::bind(&MyClass::threadfunc, &m, 1, 2.2));
// Wait for the thread
}
```


2. Mutex的概念

以前在pthread我們都會這樣來使用mutex

```cpp
// declare mutex
pthread_mutex_t m;
pthread_mutex_init(&m, NULL);
 
void threadfunc(void* param)
 pthread_mutex_lock(&m);
 // Only one can enter here...
 pthread_mutex_unlock(&m);
}
```

Boost Thread則是把lock當成一個物件，建構出來時表示鎖住一個mutex，解構表示解鎖一個mutex。

```cpp
// declare mutex
boost::mutex m;
 
void threadfunc()
 boost::mutex::scoped_lock lock(m);
 // On exiting this function, the mutex is unlocked
}
```

boost::thread有两个构造函数： 
（1）thread()：构造一个表示当前执行线程的线程对象； 
（2）explicit thread(const boost::function0<void>& threadfunc)： 
* boost::function0<void>可以简单看为：一个无返回(返回void)，无参数的函数。这里的函数也可以是类重载operator()构成的函数；该构造函数传入的是函数对象而并非是函数指针，这样一个具有一般函数特性的类也能作为参数传入.
 https://blog.csdn.net/jack_20/article/details/79892250?utm_source=blogxgwz0&utm_medium=distribute.pc_relevant.none-task-blog-title-6&spm=1001.2101.3001.4242
第一种方式：最简单方法 
```cpp
  void hello(){}
  int main(){
    boost::thread thrd(&hello);
    thrd.join(); 
  } 
```
第二种方式：复杂类型对象作为参数来创建线程： 

第三种方式：在类内部创建线程； 
（1）类内部静态方法启动线程,在这里start()和hello()方法都必须是static方法。 
（2）如果要求start()和hello()方法不能是静态方法则采用下面的方法创建线程： 

第四种方法：用类内部函数在类外部创建线程；如果线程需要绑定的函数有参数则需要使用boost::bind

https://blog.csdn.net/sinat_33098791/article/details/52447022?utm_medium=distribute.pc_relevant.none-task-blog-title-11&spm=1001.2101.3001.4242
一． 使用boost::thread创建线程

由于每一个boost::thread对应一个线程，所以创建线程就是创建一个boost::thread对象。

template

thread(Callable func);

这里需要一个函数对象（函数指针、仿函数）

A 仿函数
struct callable
{
       void operator()(void){}
}
boost::thread thread_call(struct callable);

B.全局函数. 
void func(){}
boost::thread thread_func(func);

C. 类成员函数

借助boost::bind 轻松实现

D. 含参函数对象

void func_arg(int num) {}
boost::thread thread_arg_bind(boost::bind(&func_arg,1012));
boost::thread thread_arg(func_arg,2012);


二． 线程的管理

A. 线程标识符
在boost中也有唯一标识线程的数据结构：thread::id。

B. 线程的分离与非分离
Boos::thread线程的默认属性为非分离状态,线程结束后线程标识符、线程退出状态等信息需要通过join方法回收。
Join方法会阻塞，直到该线程执行结束。
Join函数是boost::thread中少数几个会抛出异常的方法之一。当join函数过程中如果 interrupt() 方法被调用，join函数会抛出一个boost::thread_interrupted异常。例外bool timed_join(TimeDuration const& rel_time);方法阻塞特定的时间，如果超时了但线程仍未退出，则返回false。当用户并不关心线程的退出状态时，可以设置thread状态为分离，这样boost::thread会自动回收线程资源。
bool joinable() 方法返回线程是否是分离状态。

C 线程的休眠和中断

boost::thread 中提供一个静态方法
```cpp
void boost::thread::sleep(system_time const& abs_time);
```
线程将休眠直到时间超时。
sleep 函数是boost::thread中少数几个可能抛出异常的方法之一：
当sleep休眠期间interrupt() 方法被调用，sleep会抛出一个boost::thread_interrupted异常。
去了sleep()，boost::thread提供一个void yield();方法主动放弃当前的CPU时间片。

D. 线程组

```cpp
#include 

class thread_group:
   private noncopyable
{
public:
    thread_group();
    ~thread_group();
    template
    thread* create_thread(F threadfunc);
    void add_thread(thread* thrd);
    void remove_thread(thread* thrd);
    void join_all();
    void interrupt_all();
    int size() const;
};
```

例子：

``` cpp
thread_group var_thread_group;
//! 利用thread_group创建线程
boost::thread* pthread_one var_thread_group.create_thread(func);

//!加入线程组
var_thread_group.add_thread(pthread_one);
var_thread_group.add_thread(var_thread_group.create_thread(struct callable));

```

```cpp
boost::thread_group group;
boost::thread *t1 = new boost::thread( boost::bind( &threaded_function));
group.add_thread( t1);
```
Where is the bind function? If no bind, how is it called?




boost::thread的几个函数

|--------|------------|
| 函数	| 功能 |
join()	让主进程等待子线程执行完毕后再继续执行
get_id()	获得线程的 id 号
detach()	标线程就成为了守护线程，驻留后台运行
bool joinable()	是否为 join（）
|--------|------------|






  
