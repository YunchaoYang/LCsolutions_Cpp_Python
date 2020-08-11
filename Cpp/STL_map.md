## Map的使用
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
# How to iterate over the map

## 数据的插入

```cpp
   map<int ,string> maplive;  
   maplive.insert(pair<int,string>(102,"aclive")); \\ use insert pair 
   maplive.insert(map<int,string>::value_type(321,"hai")); \\ use insert, map<int,string>::valuetype(,)
   maplive[112]="April";//map中最简单最常用的插入添加！
```
## Find
``` cpp
map<int ,string >::iterator l_it;; 
   l_it=maplive.find(112);
   if(l_it==maplive.end())
                cout<<"we do not find 112"<<endl;
   else cout<<"wo find 112"<<endl;
```

## map的大小
Int nSize = mapStudent.size();

## map的基本操作函数：

     C++ maps是一种关联式容器，包含“关键字/值”对

     begin()         返回指向map头部的迭代器

     clear(）        删除所有元素

     count()         返回指定元素出现的次数

     empty()         如果map为空则返回true

     end()           返回指向map末尾的迭代器

     equal_range()   返回特殊条目的迭代器对

     erase()         删除一个元素

     find()          查找一个元素

     get_allocator() 返回map的配置器

     insert()        插入元素

     key_comp()      返回比较元素key的函数

     lower_bound()   返回键值>=给定元素的第一个位置

     max_size()      返回可以容纳的最大元素个数

     rbegin()        返回一个指向map尾部的逆向迭代器

     rend()          返回一个指向map头部的逆向迭代器

     size()          返回map中元素的个数

     swap()           交换两个map

     upper_bound()    返回键值>给定元素的第一个位置

     value_comp()     返回比较元素value的函数
     
 # 
