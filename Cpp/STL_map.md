Map的使用
需要导入头文件

```
#include <map> // STL头文件没有扩展名.h·
```
map 对象是一个模版类，需要关键字和存储对象两个模版参数
```cpp
std::map<int , std::string> person;
```
可以对模版进行类型定义使其使用方便
```cpp
typedef std::map<int , std::string> MAP_INI_STRING;`
MAP_INI_STRING person;
```
