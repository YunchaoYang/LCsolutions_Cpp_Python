https://blog.csdn.net/qq_43338695/article/details/98783911

reference就是alias

reference可以分为两类，正如标题所写，为const reference和non-const reference。

1. as function argument 
2. as return value

- return value
  1. 返回一个普通的value: 这个跟作为parameter一模一样，主要还是考虑会不会返回占用较大内存的object。
  2. 返回一个non-const reference：这个要优于返回一个普通的value，因为它不会产生copy。（当然了，有时候我们不得不返回一个普通的value，比如我们要返回的是一个called function body中的临时变量，这样用reference就会出错）
对于non-const reference而言，在calling function中返回的object可以被视为是普通的object，即，可以使用const或non-const的method。
  3. 返回一个const reference。要明白我们什么时候可以返回const reference，就必须搞清楚non-const reference和const reference的区别。对于const reference而言，返回的就是const object，只能使用const method。

C++ 引用作为函数返回值
（1）不能返回局部变量的引用。
（2）不能返回函数内部new分配的内存的引用。造成memory leak。
（3）可以返回类成员的引用，但最好是const。

引用做作为了函数的返回值，可以进行赋值操作。函数定义形式必须为：
`类型标识符& 函数名（）`.
用此形式时，相当于返回了一个变量，因为返回时返回的指针是指向变量的，因此，可以对它进行赋值操作，并且此处返回的变量，一般是`全局变量`或者`静态变量`，因此在函数返回时不会产生被返回值的副本。

```cpp
#include<iostream>
using namespace std;
int num=0;
 
int& func()
{
	return ++num; //此处num为全局变量
}
 
int main()
{
	int i;
	for(i=0;i<5;i++)
	  cout<<func()<<'\t';
	cout<<endl;
	func()=10;//对函数进行赋值，即将10赋给num
	for(i=0;i<5;i++)
	  cout<<func()<<'\t';
	cout<<endl;

```

c++中临时变量不能作为非const的引用参数
https://blog.csdn.net/kongying168/article/details/3864756?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-1&spm=1001.2101.3001.4242
