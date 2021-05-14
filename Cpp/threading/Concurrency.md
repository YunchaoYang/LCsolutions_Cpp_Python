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


 5. Common Problems associated with Concurrency
    * Thread interference errors (Race Conditions)
    * 
