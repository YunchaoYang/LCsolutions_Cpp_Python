-  Question 
   - In what situation we want to return a reference to pointer instead of a pointer?
 doubel *&
```cpp 
//---------------------------------------------------------------------------
#include <iostream>
using namespace std;

double *& ShowNumber()
{
	double n = 1550.85;

	static double *v = &n;

	return v;
}

//---------------------------------------------------------------------------
int main()
{
    double Number = *ShowNumber();

    cout << "Number: " << Number << endl;

    return 0;
}
//---------------------------------------------------------------------------
```
In the body of the function, you can do whatever is appropriate. An important rule with this type of function is that it must return either a global or a static variable. 
In other words, the variable that is returned must conserve its value when the function exits. Here is an example that returns a static variable:
When calling the function, precede its name with an asterisk. 

- Compare the following 3 scenarios:
```cpp 
void func(type*  param); // 'param' is a 'type*' local variable,  
void func(type&  param); // 'param' is a reference to a 'type' variable,  as a reference to a variable outside.
void func(type*& param); // 'param' is a reference to a 'type*' variable, will effect the pointer variable, also the pointer-pointed variable (if in heap).
```


```cpp
void func(type* param)
{
    type x;
    ...
    param = &x;
    // Argument 'param' is regarded as a local variable in this function,
    // so setting 'param = ...' will have no effect outside this function
}
```
Of course, if you do *param = ..., then it will effect the contents of the memory pointed by param. 
And you can also do param[5] = ... for example, and effect other areas within that memory space.

```cpp
void func(type& param)
{
    type x;
    ...
    param = x;
    // Argument 'param' is regarded as a reference to a variable outside this
    // function, so setting 'param = ...' will effect the referenced variable
}
```

```cpp
void func(type*& param)
{
    type x;
    ...
    param = &x;
    // Argument 'param' is regarded as a reference to a variable outside this
    // function, so setting 'param = ...' will effect the referenced variable
}
```
