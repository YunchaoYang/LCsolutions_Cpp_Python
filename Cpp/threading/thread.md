- Q? threading is to define "a block of code" that can be executed in parallel. How to define that? Separate that to process (as in MPI).

- Q?

- thread (C++11)
  - Threads allow multiple functions to execute concurrently. Threads begin execution immediately upon construction of the associated thread
  object (pending any OS scheduling delays), starting at the top-level function provided as a constructor argument. 
  The return value of the top-level function is ignored and if it terminates by throwing an exception, std::terminate is called. 
  The top-level function may communicate its return value or an exception to the caller via std::promise or by modifying shared variables
  (which may require synchronization, see std::mutex and std::atomic)

- jthread (C++20)
  - std::thread with support for auto-joining and cancellation

- Condition variables: a synchronization primitive that allows multiple threads to communicate with each other.
- Futures
  - The standard library provides facilities to obtain values that are returned and to catch exceptions that are thrown by asynchronous tasks
(i.e. functions launched in separate threads). 
These values are communicated in a shared state, in which the asynchronous task may write its return value or store an exception,
and which may be examined, waited for, and otherwise manipulated by other threads that hold instances of std::future
or std::shared_future that reference that shared state.

### Thread Local Storage
- Remember, all threads share the `same heap` although they each have their `own stack`
- Therefore any data element that is not automatic scope is by definition global to all threads
- Thread Local Storage is a mechanism that creates a unique variable for each thread

Thread Local Storage can be created at a variety of different scope levels:
 - namespace level (outside any class or function)
 - static class data member (static inside a class) `static thread_local std::string str;`
 - an automatic thread local variable inside a function `thread_local std::vector<int> v;`

### How Condition Variables Work

 1. A thread locks a mutex associated with a condition variable
 2. The thread tests the condition to see if it can proceed
 3. #1) If it can (the condition variable is true):
    1. your thread does its work
    2. your thread unlocks the mutex
 3. #2) If it cannot (the condition variable is false)
    1. the thread sleeps by calling cond_wait(&c,&m), and the mutex is automatically released for you
    2. some other thread calls cond_signal(&c) to indicate the condition is true
    3. your thread wakes up from waiting with the mutex automatically locked, and it does its work
    4. your thread releases the mutex when it’s done

### [Some example and explanation](https://www.boost.org/doc/libs/1_72_0/doc/html/thread/synchronization.html#thread.synchronization.condvar_ref)

### [thread pool](https://en.wikipedia.org/wiki/Thread_pool)
- thread pool vs thread group

## Thread
In every C++ application there is one default main thread i.e. main() function. In C++ 11 we can create additional threads by creating objects of std::thread class.
Each of the std::thread object can be associated with a thread.
[](https://thispointer.com/c-11-multithreading-part-1-three-different-ways-to-create-threads/)

What std::thread accepts in constructor ?
We can attach a callback with the std::thread object, that will be executed when this new thread starts. These callbacks can be,

- 1.) Function Pointer
- 2.) Function Objects
- 3.) Lambda functions

Thread objects can be created like this,
```cpp
std::thread thObj(<CALLBACK>);
```
New Thread will start just after the creation of new object and will execute the passed callback in parallel to thread that has started it. Moreover, any thread can wait for another to exit by calling join() function on that thread’s object.


### Differentiating between threads

- `std::thread::get_id()`
  - Member function, gives id of _associated thread object_ i.e.

If std::thread object does not have an associated thread then get_id() will return a default constructed std::thread::id object i.e. ``not any thread.``

- `std::this_thread::get_id()`
  - To get the identifier for the _current thread_ use,

- `std::thread::id`
  - is a Object, it can be compared and printed on console too. 

### Pass Arguments to Threads
To Pass arguments to thread’s associated callable object or function just pass additional arguments to the std::thread constructor. By default all arguments are copied into the `internal storage of new thread`.

- Don’t pass addresses of variables from local stack to thread’s callback function. Because it might be possible that local variable in Thread 1 goes out of scope but Thread 2 is still trying to access it through it’s address.


# OpenMP vs Pthread.f
## OpenMP 
* higher level, more portable. 
* Easility scaled than pthreads.
* use OpenMP, it can be as simple as adding a single pragma, and you'll be 90% of the way to properly multithreaded code with linear speedup. 

OpenMP is an implementation of __multithreading__, a method of parallelizing whereby a primary thread (a series of instructions executed consecutively) forks a specified number of sub-threads and the system divides a task among them. The threads then run concurrently, with the runtime environment allocating threads to different processors.


such as parallelization of loops, 
```C++
#pragma omp parallel for
for (i = 0; i < 500; i++)
    arr[i] = 2 * i;
```

https://en.wikipedia.org/wiki/OpenMP#Pros_and_cons

## Pthreads
is a very `low-level API` for working with threads. Thus, you have extremely fine-grained control over thread management (`create/join/etc`), `mutexes`, and so on. It's fairly bare-bones.

https://stackoverflow.com/questions/3949901/pthreads-vs-openmp#:~:text=If%20you%20use%20OpenMP%2C%20it,get%20more%20flexibility%20with%20pthreads.
