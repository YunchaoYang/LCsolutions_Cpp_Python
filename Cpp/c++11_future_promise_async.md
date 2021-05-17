
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
    std::cout << "In  thread t, making data...\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    promiseObj.set_value(35);
    std::cout << "Finished\n";
}
 
int main() {
    std::promise<int> promiseObj;
    std::future<int> futureObj = promiseObj.get_future();

    std::thread t(&thread_set_promise, std::ref(promiseObj)); 
    // thread t is activated with function thread_set_promise, transfer promiseObj to thread2. transfered reference
  
    std::cout << futureObj.get() << std::endl; // main thread is blocking 
    
    t.join();
 
    system("pause");
    return 0;
}
```
### 经典的生产-消费模型
mutex + condition_variable:

This example illustrates a typical production-consumption model.
```
#include <thread>
#include <mutex>
#include <iostream>
#include <chrono>
#include <memory>
#include <condition_variable>
 
struct _data
{
	bool ready;
	int32_t value;
};
 
_data data = { false, 0 }; // 全局变量 data
std::mutex data_mutex;     // 全局变量 data_mutex
std::condition_variable data_con; // 使用条件变量来使 process_thread 即消费线程进入休眠等待，
 
int main()
{
	//生产数据的线程
 	std::thread prepare_data_thread( [](){
 		std::this_thread::sleep_for(std::chrono::seconds(2) );    //模拟生产过程， 
	 	std::unique_lock<std::mutex> ulock(data_mutex);
	 	data.ready = true;
	 	data.value = 1;
	 	data_con.notify_one(); // 数据准备好了然后通知它来处理。
	});
 
	//消费数据的线程
	std::thread process_data_thread([](){
		std::unique_lock<std::mutex> ulock(data_mutex);
		cv.wait(ulock, [](){ return data.ready; });		
		std::cout << data.value << std::endl;
	});
 
	prepare_data_thread.join();
	process_data_thread.join();
 
	system("pause");
	return 0;
}
```

有没有更简便的方法来实现线程间的通信及同步呢？答案当然是 of course，下面我将使用C++11的这些新特性来实现这些需求。

``` cpp
#include <thread>
#include <iostream>
#include <future>
#include <chrono>
 
struct _data
{
	int32_t value;
};
 
_data data = { 0 };
 
int main()
{
	std::promise<_data> data_promise;      //创建一个承诺
	std::future<_data> data_future = data_promise.get_future();     //得到这个承诺封装好的期望
// 首先创建了一个 _data 类型data_promise ，而在 data_promise 里已经封装好了一个 _data类型的future，我们可以调用 promise 的 get_future() 方法得到与之对应的 future。

	std::thread prepare_data_thread([](std::promise<_data> &data_promise){
		std::this_thread::sleep_for(std::chrono::seconds(2));    //模拟生产过程
		data_promise.set_value({ 1 });       //通过set_value()反馈结果
	}, std::ref(data_promise));
 // 然后我们把 data_promise 传递给了 prepare_data_thread，于是我们便可以在 prepare_data_thread 里面来产出值了，在休眠2S之后，我们调用了 set_value() 方法来产出值。
 
	std::thread process_data_thread([](std::future<_data> &data_future){
		std::cout << data_future.get().value << std::endl;    //通过get()获取结果
	}, std::ref(data_future));
// 我们又将和 data_promise 相关联的 data_future 传递给了 process_data_thread，所以我们便可以在 process_data_thread 里调用 data_future 的 get() 方法获取 data_promise 的产出值。

// 这里需要注意的一点是，future 的 get() 方法是阻塞的，所以在与其成对的 promise 还未产出值，也就是未调用 set_value() 方法之前，调用 get() 的线程将会一直阻塞在 get()处直到其他任何人调用了 set_value() 方法。

	prepare_data_thread.join();
	process_data_thread.join();
 
	system("pause");
	return 0;
}
```
简单来说，promise 用来产出值，future 用来获取值，但这个 promise 和 future 必须是配对的，也就是说 future 是通过调用 promise 的 get_future() 方法来获得的

### packaged_task:
packaged_task 是对一个任务的抽象，我们可以给其传递一个函数来完成其构造。相较于 promise，它应该算是更高层次的一个抽象了吧，同样地，我们可以将任务投递给`任何线程`去完成，然后通过 `packaged_task.get_future()` 方法获取的 future 来获取任务完成后的产出值。那么，下面还是原来的配方：

``` cpp
#include <thread>
#include <iostream>
#include <future>
 
struct _data
{
	int32_t value;
};
 
_data data = { 0 };

int main()
{
 // packaged_task 也是一个类模板，模板参数为函数签名，也就是传递函数的类型，如上例中为 _data()，返回值为 _data 类型，if 函数参数为 void，其中返回值类型将决定 future 的类型也就是产出值类型。

std::packaged_task<_data()> prepare_data_task([]()->_data{
		std::this_thread::sleep_for(std::chrono::seconds(2));    //模拟数据生产过程, 
		return{ 1 };
	});
	auto data_future = prepare_data_task.get_future();          //获取future
 
 // 我们创建了一个任务，并投递给了 do_task_thread 去完成这个任务

	std::thread do_task_thread([](std::packaged_task<_data()> &task){
		task();              //调用packaged_task的调用符来运行任务
	}, std::ref(prepare_data_task));
 
 // 然后将对应的 data_future 投递 给了process_data_thread
	std::thread process_data_thread([](std::future<_data> &data_future){
		std::cout << data_future.get().value << std::endl; // 于是我们就可以在 process_data_thread 里获取任务产出值了。同样地，获取值之前必须等待任务的完成。
	}, std::ref(data_future)); 
 
	do_task_thread.join();
	process_data_thread.join();
 
	system("pause");
	return 0;
}
```

到了这里，还差一个 async 没有讲，可能你会有一肚子问题，说到底这几个东西不就是可以在线程之间实现通信及同步吗？是的，它为我们省去了使用 mutex，condition_variable 这些枯燥的细节，也降低了我们出错的可能，但是绝对不要以为 future 是线程安全的，future.get()只能被调用一次，多次调用会触发异常，如果想要在多个线程中多次获取产出值请查阅 shared_future。当然，智者见智仁者见仁，用不用是你的选择。

async:
最后，来看看 async 怎么使用。

当我想要异步完成一个操作，并在主线程中阻塞地或者非阻塞地获取这个异步操作的结果时，通常我们的做法是 new 一个子线程来完成这个异步操作，并结合锁，条件变量在主线程中来获取共享内存中的值。
`async 为我们实现了这些细节，让我们无需再亲自去开辟线程，并且提供了更多可选的功能。`为了与之前的内容形成对比，我们仍然采用老套的生产-消费模型来举例：

``` cpp

#include <thread>
#include <iostream>
#include <chrono>
#include <future>
 
struct _data
{
	int32_t value;
};
 
_data data = { 0 };
 
int main()
{
	auto start = std::chrono::steady_clock::now();

 // async 返回一个与函数返回值相对应类型的 future, 通过它我们可以在其他任何地方获取异步结果。
	std::future<_data> data_future = std::async(std::launch::async, []()->_data{
		std::this_thread::sleep_for(std::chrono::seconds(1));           //模拟生产过程
		return { 1 };
	});

 std::this_thread::sleep_for(std::chrono::seconds(2));
	std::cout << data_future.get().value << std::endl;              //使用产出值

// 由于我们给 async 提供了 std::launch::async 策略，所以生产过程将被异步执行，具体执行的时间取决于各种因素，最终输出的时间为 2000ms+，可见生产过程和主线程是并发执行的。
// 除了 std::launch::async，还有一个 std::launch::deferred 策略，它会延迟线程地创造，也就是说只有当我们调用 future.get() 时子线程才会被创建以执行任务。你可以自己改一下看看最终的输出结果是不是 3000ms+。
 
	auto end = std::chrono::steady_clock::now();
	std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() << std::endl;
 
	system("pause");
	return 0;
}

————————————————
版权声明：本文为CSDN博主「AC_hell」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/AC_hell/article/details/72718363```

————————————————
版权声明：本文为CSDN博主「AC_hell」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/AC_hell/article/details/72718363
