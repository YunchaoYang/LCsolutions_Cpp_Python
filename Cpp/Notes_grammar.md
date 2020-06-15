## 构造函数
https://zhuanlan.zhihu.com/p/66568817

# define预处理器和const关键字
存储类：
auto ：自动推断该变量的类型、声明函数时函数返回值的占位符。

C++成员函数的重载

C++多态(polymorphism)是通过虚函数来实现的，虚函数允许子类重新定义成员函数，而子类重新定义父类的做法称为覆盖(override)，或者称为重写。

最常见的用法就是声明基类的指针，利用该指针指向任意一个子类对象，调用相应的虚函数，动态绑定。由于编写代码的时候并不能确定被调用的是基类的函数还是哪个派生类的函数，所以被成为“虚”函数。如果没有使用虚函数的话，即没有利用C++多态性，则利用基类指针调用相应的函数的时候，将总被限制在基类函数本身，而无法调用到子类中被重写过的函数。
————————————————
版权声明：本文为CSDN博主「i_chaoren」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/i_chaoren/java/article/details/77281785