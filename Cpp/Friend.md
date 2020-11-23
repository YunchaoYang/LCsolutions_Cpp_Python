1. 为什么要使用友元？

通常对于普通函数来说，要访问类的保护成员是不可能的，如果想这么做那么必须把类的成员都生命成为 `public(共用的)` ，然而这做带来的问题遍是任何外部函数都可以毫无约束的访问它操作它；另一种方法是利用 C++ 的 friend 修饰符，可以让一些你设定的函数能够对这些`私有(private)`或`保护(protected)数据`进行操作。

2. 使用友元有哪些缺点？

使用友元的同时也破坏了类的封装特性，这即是友元最大的缺点。当对外声明为友元后，你的所有细节全部都暴露给了对方。
就好像你告诉你朋友你很有钱这个密秘，进而又把你有多少钱，多少古董，多少家产，多少小妾等等所有的家底全给他说了。

3. 友元怎样理解？

定一个友元函数，或是友元类，就是告诉对方：我的所有元素对你是开放的。

* 普通函数做为类的一个友元函数
* 一个普通函数可以是多个类的友元函数
* 一个类的成员函数也可以是另一个类的友元
* 整个类也可以是另一个类的友元 friend class MyClass_B;

* Friend;
Friend Class A friend class can access private and protected members of other class in which it is declared as friend. It is sometimes useful to allow a particular class to access private members of other class. 
For example a LinkedList class may be allowed to access private members of Node.

```cpp
class Node { 
private: 
    int key; 
    Node* next; 
    /* Other members of Node Class */
  
    // Now class  LinkedList can 
    // access private members of Node 
    friend class LinkedList; 
}; 
```

* Friend function
```cpp
class Node { 
private: 
	int key; 
	Node* next; 

	/* Other members of Node Class */
	friend int LinkedList::search(); 
	// Only search() of linkedList 
	// can access internal members 
}; 
```

* A simple and complete C++ program to demonstrate friend Class

```cpp
#include <iostream> 
class A { 
private: 
	int a; 

public: 
	A() { a = 0; } 
	friend class B; // Friend Class 
}; 

class B { 
private: 
	int b; 

public: 
	void showA(A& x) 
	{ 
		// Since B is friend of A, it can access 
		// private members of A 
		std::cout << "A::a=" << x.a; 
	} 
}; 

int main() 
{ 
	A a; 
	B b; 
	b.showA(a); 
	return 0; 
} 
```

* A simple and complete C++ program to demonstrate friend function of another class
```
#include <iostream> 

class B; 

class A { 
public: 
	void showB(B&); 
}; 

class B { 
private: 
	int b; 

public: 
	B() { b = 0; } 
	friend void A::showB(B& x); // Friend function 
}; 

void A::showB(B& x) 
{ 
	// Since showB() is friend of B, it can 
	// access private members of B 
	std::cout << "B::b = " << x.b; 
} 

int main() 
{ 
	A a; 
	B x; 
	a.showB(x); 
	return 0; 
}
```
A simple and complete C++ program to demonstrate global friend
```cpp
#include <iostream> 

class A { 
	int a; 

public: 
	A() { a = 0; } 

	// global friend function 
	friend void showA(A&); 
}; 

void showA(A& x) 
{ 
	// Since showA() is a friend, it can access 
	// private members of A 
	std::cout << "A::a=" << x.a; 
} 

int main() 
{ 
	A a; 
	showA(a); 
	return 0; 
}
```
