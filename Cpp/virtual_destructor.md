#### virtual 析构函数
```cpp
class Base{ 
public:
  virtual ~Base(){cout<<"~B"<<endl;}; 
}

class Derived:public Base{ 
public:
  virtual ~Derived(){cout<<"~D"<<endl;}; 
}
 
void main (){ 
  Base *b=new Derived();
  delete b; 
} 
```
类型需要虚析构函数的另外一个特征是该类型具有指针成员或引用成员。如果有指针成员和引用成员，则该类型通常需要实现析构函数以及拷贝操作。通常，一个实现了析构函数的类型同时也需要实现拷贝构造函数与拷贝复制函数。

C++多态的精华就是virtual函数。

1.纯虚函数。这个就是virtual void show()=0;类似java中的接口。必须实现。

2.普通虚函数

* 作为一个经验法则：如果你有一个带有虚函数功能的类，则它需要一个虚析构函数，原因如下：

1. 如果一个类有虚函数功能，它经常作为一个基类使用。

2.如果它是一个基类，它的派生类经常使用new来分配。

3.如果一个派生类对象使用new来分配，并且通过一个指向它的基类的指针来控制，那么它经常通过一个指向它的基类的指针来删除它（如果基类没有虚析构函数，结果将是不确定的，实际发生时，派生类的析构函数永远不会被调用）。基类有虚析构函数的话，最底层的派生类的析构函数最先被调用，然后各个基类的析构函数被调用。


#### 析构函数写成virtual的好处[](https://blog.csdn.net/heibao111728/article/details/80814313?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)
相信学习c++的很多同志都听过这样的建议：最好将类的析构函数写成虚函数，如下：
```cpp
class B
{
public:
    B() { printf("B()\n"); }
    virtual ~B() { printf("~B()\n"); }
private:
    int m_b;
};
```
这么写到底有什么好处呢？

我们删掉父类B的指针pB，但是pB指向的是子类D的对象，通过虚函数表，编译器知道要去执行子类D的析构函数`~D()`，
执行完子类的析构函数后，按照c++的内部机制紧接着会去执行父类的析构函数`~B()`.

### 注：c++中有这样的约束：执行子类构造函数之前一定会执行父类的构造函数；
同理，执行子类的析构函数后，一定会执行父类的析构函数，这也是为什么我们一直建议类的析构函数写成虚函数的原因。
