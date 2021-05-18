https://www.educative.io/blog/modern-multithreading-and-concurrency-in-cpp

Real World example
1. web crawler
2. Email server

The key question in my mind:
1. in thread pool, how a function is transfered in a thread?
2. How the hardware concurrency (threads = core) and task scheduling are switched in real OS?
3.  What is the key difference between concurrency and parallelism
   * My Answer: 
   * Other Explanation from online
      * Concurrent and parallel are effectively the same principle as you correctly surmise, both are related to tasks being executed 
        simultaneously although I would say that parallel tasks should be truly multitasking, executed "at the same time" 
        whereas concurrent could mean that the tasks are sharing the execution thread while still appearing to be executing in parallel.
      * Concurrency means multiple tasks which start, run, and complete in overlapping time periods, in no specific order. 
      * Parallelism is when multiple tasks OR several part of a unique task literally run at the same time, e.g. on a multi-core processor.


4.  Key difference between concurrency and threading?
  * My tentative answer: concurrency involves the linking interaction between multiple threads, while the multithreading technology itself is designed to run several threads in single-core or multi-core machines. The subject of concurrency is about task while threading refers more to the way of doing task.   
  * Online explanation: 
     *  Multithreading — This is a software implementation allowing different threads to be executed concurrently. 
        A multithreaded program appears to be doing several things at the same time even when it’s running on a single-core machine. 
        This is a bit like chatting with different people through various IM windows; although you’re actually switching back and forth, 
        the net result is that you’re having multiple conversations at the same time.

* 并发，并行的区别
  * 并发：同一时间段内交替运行多个进程（线程）
  * 并行：同一时刻运行多个进程（线程）。很明显，只有多处理器才能支持。

* 同步，异步
  有了之前的概念，我们可以想象，当几个线程或者进程在并发执行时，如果我们不加任何干预措施，那么他们的执行顺序是由系统当时的环境来决定的，所以不同时间段不同环境下运行的顺序都会不尽相同，这便是异步（有差异的步骤）。当然，同步肯定就是通过一定的措施，使得几个线程或者进程总是按照一定顺序来执行（总是按照相同的步骤）。

* 阻塞与非阻塞
  * 当一个进程或者线程请求某一个资源而不得时，如I/O，便会进入阻塞状态，一直等待。scanf()便是一个很好的例子，当程序运行到scanf()时，如果输入缓存区为空，那么程序便会进入阻塞状态等待我们从键盘输入，这便是以阻塞的方式调用scanf()。
  * 通过一定方法，我们可以将scanf()变成非阻塞的方式来执行。如给scanf()设置一个超时时间，如果时间到了还是没有输入那么便跳过scanf()，这个时候我们就称为用非阻塞的方式来调用scanf()。

对比可以发现，同步即阻塞。想要按照某特定顺序来执行一系列过程，在上一个过程完成之前下一个过程必须等待，这就是阻塞在了这个地方。当同步运行的时候，会等待同步操作完成才会返回，否则会一直阻塞在同步操作处。

相反的，异步即非阻塞，当异步调用某个函数时，函数会立刻返回，而不会阻塞在那。
怎么判断异步操作是否已经完成？通常有3种方式：
1.状态：异步操作完成时会将某个全局变量置为特定值，可以通过轮询判断变量的值以确定是否操作完成。
2.通知：异步操作完成会给调用者发送特定信号。
3.回调：异步操作完成时会调用回调函数。

``` cpp 
// 由于recvMsg（）和getline（）都是以阻塞方式运行的，所以只能收一条信息发一条消息这样轮回，而不能想什么时候发就什么时候发。
int main(int argc, char *argv[])
{
    ...
    string recvBuf,sendBuf;
    while(1)
    {
	recvBuf = recvMsg();            		//由于涉及到网络编程，所以这里仅用recvMsg()来表示获取别人发来的消息，如果没有消息则阻塞，之后我会写一些网络编程的文章
	cout << "对方向你发送：" << revcBuf << endl;    //输出对方发来的信息
	getline(cin,sendBuf);           		//输入要发送的信息至sendBuf中，如果没有输入则阻塞
	sendMsg(sendBuf);				//发送自己输入的信息
    }
    ...
    return 0;
}
```

``` cpp 
#include<thread>
...
void getMsg()
{
    ...
    while(1)
    {
	recvBuf = recvMsg();
	cout << "对方向你发送：" << revcBuf << endl;
    }
    ...
    return;
}
int main(int argc, char *argv[])
{
    ...
    string sendBuf;
    thread trdRecv(getMsg);        //创建子线程以完成getMsg
    while(1)
    {                  
	getline(cin,sendBuf);           		
	sendMsg(sendBuf);				
    }
    ...
    return 0;
}
```
此时，你的进程由2个线程组成，一个主线程（main），一个子线程（trdRecv），主线程用来发送消息，子线程用来接收消息，2者并发执行，共用CPU，所以实现了我们想要的功能。然而，大功告成了吗？还记得上面提过的join() 和detach() 吗，我们并没有使用，所以结果必然是导致子线程终止之后不被回收，造成内存泄露，资源不被释放。那好，我们加上一个 join() 试试？


 5. Common Problems associated with Concurrency
    * Thread interference errors (Race Conditions)
    * Deadlock

C++17 added parallel algorithms — and parallel implementations of many standard algorithms.
