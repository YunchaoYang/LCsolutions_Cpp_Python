Notes on C++ struct
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

#指向结构的指针

struct Books *struct_pointer;


struct_pointer = &Book1;

struct_pointer->title;
