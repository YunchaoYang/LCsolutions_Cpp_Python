### Grammar: 
```cpp 
[capture] (parameters) mutable ->return-type {statement}
```
![](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWctYmxvZy5jc2RuLm5ldC8yMDE4MDcwMzIyNTQwNTIy?x-oss-process=image/format,png)

![](https://docs.microsoft.com/en-us/cpp/cpp/media/lambdaexpsyntax.png?view=msvc-160)

1. capture clause (Also known as the lambda-introducer in the C++ specification.)
   - An empty capture clause, [ ], indicates that the body of the lambda expression accesses no variables in the enclosing scope.
   - Variables that have the ampersand (&) prefix are accessed by reference and variables that do not have it are accessed by value.
   - default capture mode 
      * `[&]` means all variables that you refer to are captured by reference,  `引用传递`捕捉所有父作用域的变量（包括this）
      * `[&var]` 表示引用传递捕捉1变量 var,
      * `[=]` means they are captured by value. `值传递方式` 捕捉所有父作用域的变量（包括this）
      *  两个通配符 `=` 和 `&` 一个取值一个取址 ` [a, &b] // a 传值，b 传址`
      *  [this] 表示值传递方式捕捉当前的this指针。
2. parameter list Optional. (Also known as the lambda declarator)
3. mutable specification Optional.
4. exception-specification Optional.
    * -> int 这个 int 是返回值  
5. trailing-return-type Optional.
6. lambda body.

``` cpp 
int main()
{
   int a = 1,b =2, c =3;
   auto retVal = [=,&a,&b]()
   {
       printf("inner c[%d]\n",c); // 3
       a = 10;
       b = 20;
       c = 30;
       return a+b;
   };
   printf("sum[%d]\n",retVal()); // 30 
   printf("a[%d] b[%d] c[%d]\n",a,b,c); //a = 10, b = 20, c =  3
   return 0;  
```
