C++ 抽象类
# 纯虚函数
在基类中声明的虚函数，它在基类中没有定义，但要求任何派生类都要定义自己的实现方法。在基类中实现纯虚函数的方法是在函数原型后加 "=0"
带有纯虚函数的类称为抽象类。抽象类是一种特殊的类，它是为了抽象和设计的目的而建立的，它处于继承层次结构的较上层。抽象类是不能定义对象的，在实际中为了强调一个类是抽象类，可将该类的构造函数说明为保护的访问控制权限。
```cpp
virtual ReturnType Function()= 0;
```
*（1）抽象类只能用作其他类的基类，不能建立抽象类对象。

*（2）抽象类不能用作参数类型、函数返回类型或显式转换的类型。

*（3）可以定义指向抽象类的指针和引用，此指针可以指向它的派生类，进而实现多态性。

```cpp
#include<iostream>
using namespace std;

const double PI=3.14159;

class Shapes   //抽象类
{
protected:
    int x, y;
public:
    void setvalue(int d, int w=0){x=d;y=w;}
    virtual void disp()=0;//纯虚函数
};

class Square:public Shapes
{
public:
    void disp(){
        cout<<"矩形面积:"<<x*y<<endl;
    }
};

class Circle:public Shapes{
public:
    void disp(){
        cout<<"圆面积:"<<PI*x*x<<endl;
    }
};

int main()
{
    Shapes *ptr[2]; //定义对象指针数组
    Square s1;
    Circle c1;
    ptr[0] = &s1;
    ptr[0]->setvalue(10, 5);
    ptr[0]->disp();
    ptr[1] = &c1;
    ptr[1]->setvalue(10);
    ptr[1]->disp();
    return 0;

}
```
https://www.cnblogs.com/balingybj/p/4771916.html
https://www.jianshu.com/p/852e5bf33f4a

# 接口
接口是一个概念。它在C++中用抽象类来实现，接口是专门被继承的。接口存在的意义也是被继承。和C++里的抽象类里的纯虚函数是相同的。不能被实例化。

# 虚基类

在派生类继承基类时，加上一个virtual关键词则为虚拟基类继承，如：
``` cpp
class derive : virtual public base
{
};
```
虚基类是相对于它的派生类而言的，它本身可以是一个普通的类。只有它的派生类虚继承它的时候，它才称作虚基类，如果没有虚继承的话，就称为基类。比如类B虚继承于类A，那类A就称作类B的虚基类，如果没有虚继承，那类B就只是类A的基类。
虚继承主要用于一个类继承多个类的情况，避免重复继承同一个类两次或多次。
例如 由类A派生类B和类C，类D又同时继承类B和类C，这时候类D就要用虚继承的方式避免重复继承类A两次。
