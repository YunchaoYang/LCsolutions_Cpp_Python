# auto 
```cpp
int add(int x, int y)
{
    return x + y;
}
 
int main()
{
    auto sum { add(5, 6) }; // add() returns an int, so sum's type will be deduced to int
    return 0;
}
```
But this is not good use of auto, since the program need to be very clear about the data type a function returns. Otherwise, it may cause trouble.

When type is very very long due to the class inheritance, probably use auto, but also can be replaced by "typedef" or "using".


# const
* Syntax:
* const Class_Name Object_name;
or `const int 5;`

