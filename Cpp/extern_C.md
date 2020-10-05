When to use extern "C" in C++ files?
extern c is only

- use C library in C++, (in declaration of C functions)
```c
  extern "C" int foo(int);
```
- export some C++ code to C (in defining C++ functions)
```cpp
extern "C" int foo(int) { something; }
```
- We need an ability to resolve symbol in shared library, to get rid mangling
```cpp
extern "C" int foo(int) { something; }
typedef int (*foo_type)(int);
foo_type f = (foo_type)dlsym(handle,"foo")
```
source:https://stackoverflow.com/questions/1292138/when-to-use-extern-c-in-c


What is a good practice of using extern "C"?
```cpp
#ifdef __cplusplus  
extern "C" { 
#endif 
    /* Declarations of this file */
#ifdef __cplusplus 
} 
#endif 
```
