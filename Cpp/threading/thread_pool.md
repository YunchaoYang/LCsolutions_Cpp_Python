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
