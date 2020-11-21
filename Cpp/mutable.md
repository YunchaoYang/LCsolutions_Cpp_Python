* 为什么要有const常函数这个概念? (&#x1F34E;)
  * 因为为了封装的良好性，用到的一些函数并不需要我们去改变类中的参数和成员变量，仅仅只是为了显示和输出的作用，因此才引进常函数，

* 为什么要再这里提到常函数呢?(&#x1F536;)
  * 我们了解到c++中，一件事情并不是绝对的，如果有const常函数，那么一定有可以修改的方法，这里就用到了这个关键字

* mutable是用来修饰类中的non-static成员变量，目的是为了使这些成员变量在被const关键字修饰的成员函数中使用时，可以被修改。

* mutable一种常用的场景是在线程安全时，若类的成员函数定义了多个线程函数，并且定义了互斥锁mutex，
由于多线程需要操作mutex，那么在const成员函数中，则可将互斥锁mutex用mutable关键字修饰，以实现线程安全。



[Example](https://blog.csdn.net/DeliaPu/article/details/108013141?utm_medium=distribute.pc_relevant_t0.none-task-blog-searchFromBaidu-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-searchFromBaidu-1.control)
