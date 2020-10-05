When to use extern "c" in C++ files?
extern c is only

- use C library in C++
```c
  extern "C" int foo(int);
```
- export some C++ code to C
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
