模板是泛型编程的基础，泛型编程即以一种独立于任何特定类型的方式编写代码。
编写一段通用的逻辑，可以把任意类型的变量传进去处理.
*模板定义本身不参与编译，而是编译器根据模板的用户使用模板时提供的类型参数生成代码，再进行编译，这一过程被称为模板实例化。用户提供不同的类型参数，就会实例化出不同的代码。

### 函数模板
模板函数定义的一般形式如下所示：
```cpp
template <typename T>
inline T const& Max (T const& a, T const& b) 
{ 
    return a < b ? b:a; 
} 
```
在这里，type 是函数所使用的数据类型的占位符名称。


int a = b is setting a's VALUE to b's VALUE
int* a = &b is setting a's VALUE to the ADDRESS of b
int& a = b is setting a's ADDRESS to b's ADDRESS (a is a reference to b)

使用非类型形参
```cpp
// N 必须是编译时的常量表达式
template
void printArray(const T (&a)[N]) {
std::cout << "[";
const char *sep = "";
for (int i = 0; i < N; i++, (sep = ", ")) {
std::cout << sep << a[i];
}
std::cout << "]" << std::endl;
}
int main() {
// T: int, N: 3
int a[]={1, 2, 3};
printArray(a);
float b[] = {1.1, 2.2, 3.3};
printArray(b);
return 0;
}
```
