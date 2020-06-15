### Notes on C++ struct
```cpp
struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} book;
Books book1;
```
### 成员访问运算符（.）
 `strcpy( Book1.title, "C++ 教程");`
 
 #结构作为函数参数, 传参方式与其他类型的变量或指针类似

### 指向结构的指针

`struct Books *struct_pointer;`

or 

`struct_pointer = &Book1;`

`struct_pointer->title;`
.（点）运算符和 ->（箭头）运算符用于引用类、结构和共用体的成员: 点运算符应用于实际的对象。箭头运算符与一个指向对象的指针一起使用。

### typedef 关键字

reference: https://www.runoob.com/cplusplus/cpp-data-structures.html
