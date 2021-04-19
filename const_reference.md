# Error 1
invalid initialization of non-const reference of type ‘std::string&’ from an rvalue of type ‘std::string’
```cpp
void PrintStr(std::string& str) {    cout<< str << endl; }
int main(){    
    PrintStr(string("HelloWorld!"));   //string("HelloWorld!")  为一个临时变量
    return 0;}
```
说明：临时变量是转瞬即逝的，在上面的代码中，用str引用临时变量的时候临时变量已经不存在了。
解决方案：`void PrintStr(std::string& str);` 改为 `void PrintStr(const std::string& str)`;
const 引用可以初始化为不同类型的对象或者初始化为右值。例如：
```cpp 
double dval = 1.131;
const int &ri = dval;
const int &r = 30;
```
From csdn blog.

# Error 2
