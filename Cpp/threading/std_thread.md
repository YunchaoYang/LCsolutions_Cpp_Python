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
