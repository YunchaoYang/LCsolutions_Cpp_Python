# When to use extern "C" in C++ files?
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

## Example, how to use printf in C++,

- Right

```cpp
extern "C"{
   int printf(const char *format,...);
}
main() {
   printf("Hello World");
}
```
- wrong
```cpp
int printf(const char *format,...);
main() {
   printf("Hello World");
}
```
Error: undefined reference to printf(char const*, ...)' ld returned 1 exit status

# What is a good practice of using extern "C"?
```cpp
#ifdef __cplusplus  
extern "C" { 
#endif 
    /* Declarations of this file */
#ifdef __cplusplus 
} 
#endif 
```
# What is name mangling?
Due to function overloading in C++, C++ compiler will generate a new name for function. 
see following link for example.

The C language does not support function overloading, So we have to make sure that name of a symbol is not changed, when we link a C code in C++.

To undertstand name mangling, https://www.tutorialspoint.com/what-is-the-effect-of-extern-c-in-cplusplus

