# Constructors in C++
* Default Constructors
* Parameterized Constructors: 
* Copy Constructor: `ClassName (const ClassName &old_obj);` 

## Default Constructors

## Parameterized Constructors: 

### 构造函数初始化(The Constructor Initializer)
构造函数是一个函数，由函数名、参数表和函数体构成。与其它函数不同的是，构造函数可以包含构造函数初始化列表(consturctor initializer list)。

###

构造函数的参数个数不定，这使得构造函数可以重载。

#### 带默认参数的构造函数(constructor with default argument)

一是构造函数参数表为空的构造函数。
二是构造函数参数表中参数值全为默认值的构造函数。

类中如果显式定义了构造函数，编译器是不会为我们提供默认构造函数的。所以，当显式定义了一个构造函数后，最好也定义一个默认构造函数，这个默认构造函数最好是无参构造函数。

### 隐式的调用构造函数

构造函数除了可以初始化类的对象外，它还有一个很重要的作用，就是将一种类型转换成类类型。转换过程通常是隐式的调用对应的构造函数完成的。

例如：我们在`Test类`中定义了一个函数，它接受Test类的对象的引用为参数，比如 `bool compare(Test& ap)`;
倘若我们定义了程序的构造函数，我们可以这样调用函数，设app为Test类的一个对象，则可以这样写：`int a=20; bool c=app.compare(a)`;这个过程中，整型变量a作为参数传递给函数compare，虽然compare函数需要接受类对象，但是由于存在构造函数，编译器会隐式的调用构造函数，将实参a构造成一个临时对象，进而参与到函数中，当函数执行完成后，该临时对象被删除。

当我们在构造函数声明时，在构造函数名前加上关键字explicit，这个关键字使得无法隐式的调用构造函数来完成类型转换。

当构造函数声明为explicit后，我们可以显式的进行类型转换。如`app.compare(Test(a))`;，有没有感到很熟悉？这个过程十分类似于强制类型转换，只不过是类类型的强制类型转换。

通常，单个参数的构造函数会加上explicit关键字，这样可以避免很多错误，防止隐式的类型转换。当需要进行类型转换时，显式的使用类型转换会让代码更加清晰明了。

## Copy Constructor 拷贝构造函数
复制构造函数是指只有一个参数，且参数为类对象的引用的构造函数。形为` Test(Test& ap){}`。

什么时候会用到Copy Constructor? 
* 当我们定义一个对象时，它是由另外一个对象来初始化的时候就用到Copy Constructor了。
* 一个方法以 "值" 作为参数传进去或者一个方法中以值作为返回。
```cpp
void setPeople(People p1){//以值传入会调用 copy constructor
	}
void setPeople(People& p1){//以引用传入不会调用 copy constructor
	}
```
调用copy constructor的消耗比较大，所以一般都以引用方式作为函数参数。

### copy constructor 与 assignment operator 的区别
下面这种写法也会触发copy constructor:
```cpp
People p1(18);
	cout << "p1's age " << p1.getAge() << endl;
	People p2 = p1; // 触发copy constructor:
	cout << "p2's age " << p2.getAge() << endl;
```

```cpp
 // copy constructor
    People(const People& p){
        cout << "copy constructor" << endl;
    }

// assignment operator
	People& operator=(const People& p1){
        cout << "assignment operator" << endl;
        m_age = p1.getAge();
        return *this;
    }
    
//测试代码
People p1(18);
    cout << "p1's age " << p1.getAge() << endl;
    People p2 = p1; // copy constructor
    cout << "p2's age " << p2.getAge() << endl;
    p2 = p1; // assignment operator
cout << p2.getAge() << endl; 
```
* "=" 什么时候会调用Copy Constructor呢
    * ？在初始化的时候，也就是第一个 People p2 = p1。
    因为Copy Constructor 是一种 Constructor，也是负责初始化的。
* 什么时候"="是赋值呢？
    * 两个都已经初始化，再调用"="就是赋值了。


### 禁用 Copy Constructor, Copy assignment operator, destructor, default constructor.
把Copy Constructor设置为private? in (c++03)
or make it a delete function in (c++11).

https://www.youtube.com/watch?v=EL30-a2gblQ&list=PLE28375D4AC946CC3&index=5

```cpp
#include<iostream> 
using namespace std; 
  
class Point 
{ 
private: 
    int x, y; 
public: 
    Point(int x1, int y1) { x = x1; y = y1; }   // parameter constructor 
  
    // Copy constructor 
    Point(const Point &p2) {x = p2.x; y = p2.y; } 
  
    int getX()            {  return x; } 
    int getY()            {  return y; } 
}; 
  
int main() 
{ 
    Point p1(10, 15); // Normal constructor is called here 
    Point p2 = p1; // Copy constructor is called here 
  
    // Let us access values assigned by constructors 
    cout << "p1.x = " << p1.getX() << ", p1.y = " << p1.getY(); 
    cout << "\np2.x = " << p2.getX() << ", p2.y = " << p2.getY(); 
  
    return 0; 
}
```

https://www.geeksforgeeks.org/constructors-c/?ref=lbp

