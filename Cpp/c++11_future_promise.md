
future和promise的作用是在不同线程之间传递数据。使用指针也可以完成数据的传递，但是指针非常危险，因为互斥量不能阻止指针的访问；
而且指针的方式传递的数据是固定的，如果更改数据类型，那么还需要更改有关的接口，比较麻烦；
promise支持泛型的操作，更加方便编程处理。

假设线程1需要线程2的数据，那么组合使用方式如下：

1. 线程1初始化一个promise对象和一个future对象，promise传递给线程2，相当于线程2对线程1的一个承诺；future相当于一个接受一个承诺，用来获取未来线程2传递的值
2. 线程2获取到promise后，需要对这个promise传递有关的数据，之后线程1的future就可以获取数据了。
如果线程1想要获取数据，而线程2未给出数据，则线程1阻塞，直到线程2的数据到达

![aHR0cHM6Ly90aGlzcG9pbnRlci5jb20vd3AtY29udGVudC91cGxvYWRzLzIwMTUvMDYvcHJvbWlzZS5wbmc](https://user-images.githubusercontent.com/6526592/118506023-f1382580-b6fa-11eb-9c42-c677764a5a97.png)

``` cpp
#include <iostream>
#include <functional>
#include <future>
#include <thread>
#include <chrono>
#include <cstdlib>
 
void thread_set_promise(std::promise<int>& promiseObj) {
    std::cout << "In a thread, making data...\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    promiseObj.set_value(35);
    std::cout << "Finished\n";
}
 
int main() {
    std::promise<int> promiseObj;
    std::future<int> futureObj = promiseObj.get_future();

    std::thread t(&thread_set_promise, std::ref(promiseObj)); 
    // thread t is activated with function thread_set_promise, transfer promiseObj to thread2.
  
    std::cout << futureObj.get() << std::endl; // main thread is blocking 
    
    t.join();
 
    system("pause");
    return 0;
}
```
