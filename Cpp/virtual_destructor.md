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
