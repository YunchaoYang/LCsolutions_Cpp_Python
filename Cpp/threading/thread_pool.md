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
