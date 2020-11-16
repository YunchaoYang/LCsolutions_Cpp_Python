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

# example and explanation
https://www.boost.org/doc/libs/1_72_0/doc/html/thread/synchronization.html#thread.synchronization.condvar_ref

# thread pool vs thread group
https://en.wikipedia.org/wiki/Thread_pool

# Concurrency pattern
https://en.wikipedia.org/wiki/Concurrency_pattern

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
