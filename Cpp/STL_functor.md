functor: class function
Functors are _objects_ that can be treated as though they are a function or function pointer. 
Functors are most commonly used along with STLs in a scenario like following:

To create a functor, we create a object that overloads the `operator()`.

```cpp
/*
 * Function Objects (functors)
 *
 * Example:
 */
class X {
   public:
   void operator()(string str) { 
      cout << "Calling functor X with parameter " << str<< endl;
   }  
};

int main()
{
   X foo;
   foo("Hi");    // Calling functor X with parameter Hi
}

```
/*
 * Benefits of functor:
 * 1. Smart function: capabilities beyond operator()
 * 	It can remember state.
 * 2. It can have its own type.
 */
 
https://www.geeksforgeeks.org/functors-in-cpp/

### Parameterized Function

```cpp
void add2(int i) {
   cout << i+2 << endl;
}

template<int val>
void addVal(int i) {
   cout << val+i << endl;
}

class AddValue {
   int val;
   public:
   AddValue(int j) : val(j) { }
   void operator()(int i) {
      cout << i+val << endl;
   }
};

int main()
{
   vector<int> vec = { 2, 3, 4, 5};   
   //for_each(vec.begin(), vec.end(), add2); // {4, 5, 6, 7}
   int x = 2;
   //for_each(vec.begin(), vec.end(), addVal<x>); // {4, 5, 6, 7}
   for_each(vec.begin(), vec.end(), AddValue(x)); // {4, 5, 6, 7}
}
```

 * Build-in Functors
```
less greater  greater_equal  less_equal  not_equal_to
logical_and  logical_not  logical_or
multiplies minus  plus  divide  modulus  negate

int x = multiplies<int>()(3,4);  //  x = 3 * 4 

if (not_equal_to<int>()(x, 10))   // if (x != 10)
   cout << x << endl;
```

### Parameter Binding

```cpp
set<int> myset = { 2, 3, 4, 5};   
vector<int> vec;

int x = multiplies<int>()(3,4);  //  x = 3 * 4 

// Multiply myset's elements by 10 and save in vec:
transform(myset.begin(), myset.end(),    // source
	      back_inserter(vec),              // destination
			bind(multiplies<int>(), placeholders::_1, 10));  // functor
    // First parameter of multiplies<int>() is substituted with myset's element
    // vec: {20, 30, 40, 50}


void addVal(int i, int val) {
   cout << i+val << endl;
}
for_each(vec.begin(), vec.end(), bind(addVal, placeholders::_1, 2));
```


```cpp
void addVal(int i, int val) {
   cout << i+val << endl;
}
for_each(vec.begin(), vec.end(), bind(addVal, placeholders::_1, 2));

// C++ 03: bind1st, bind2nd

// Convert a regular function to a functor
double Pow(double x, double y) {
	return pow(x, y);
}

int main()
{
  set<int> myset = {3, 1, 25, 7, 12};
  deque<int> d;
  auto f = function<double (double,double)>(Pow);   //C++ 11
  transform(myset.begin(), myset.end(),     // source
		      back_inserter(d),              // destination
				bind(f, placeholders::_1, 2));  // functor
            //  d: {1, 9, 49, 144, 625}
}
// C++ 03 uses ptr_fun 



set<int> myset = {3, 1, 25, 7, 12};
// when (x > 20) || (x < 5),  copy from myset to d
deque<int> d;

bool needCopy(int x){
   return (x>20)||(x<5);
}


transform(myset.begin(), myset.end(),     // source
          back_inserter(d),               // destination
          needCopy
          );

// C++ 11 lambda function:
transform(myset.begin(), myset.end(),     // source
          back_inserter(d),              // destination
          [](int x){return (x>20)||(x<5);}
          );
```
https://www.youtube.com/watch?v=shqvSkk8r0M&t=610s

## 函数对象  详解
任何定义了函数调用操作符的对象都是函数对象

封装器 std::function

https://blog.csdn.net/y1196645376/article/details/51289254?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160571793819725255562589%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160571793819725255562589&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-3-51289254.pc_first_rank_v2_rank_v28&utm_term=%E5%87%BD%E6%95%B0%E5%AF%B9%E8%B1%A1&spm=1018.2118.3001.4449

https://blog.csdn.net/dadan1314/article/details/80406554?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160571799819724836724961%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160571799819724836724961&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-1-80406554.pc_first_rank_v2_rank_v28&utm_term=%E5%87%BD%E6%95%B0%E5%AF%B9%E8%B1%A1+c%2B%2B&spm=1018.2118.3001.4449

* 函数指针怎么声明？能用来做什么？什么时候用？
指向函数地址的指针变量，
在C编译时，每一个函数都有一个入口地址，那么这个指向这个函数的函数指针便指向这个地址。
函数指针主要由以下两方面的用途：
调用函数和用作函数参数。

* 函数指针变量名称一定要和函数名字一样吗？一个函数只能定义一个函数指针吗？


* 给函数指针变量初始化，获取函数的地址时，有几种方式？可以不加取址&符号吗？想要传入另外一个函数，一定要提前定义吗？

* 函数对象的实质是什么？怎么理解这个东西？

* 怎么调用函数对象？

* 函数对象和函数指针的比较？

函数对象可以把附加对象保存在函数对象中是它最大的优点。

另外，C++函数对象还有一个函数指针无法匹敌的用法：可以用来封装类成员函数指针。

它的弱势也很明显，它虽然用起来象函数指针，但毕竟不是真正的函数指针。在使用函数指针的场合中，它就无能为力了。例如，你不能将函数对象传给qsort函数！因为它只接受函数指针。


* C++11中的function函数对象又是什么，是用来干什么的？
类模版std::function是一种通用、多态的函数封装。std::function可以对任何可以调用的实体进行封装，这些目标实体包括普通函数、Lambda表达式、函数指针、以及其它函数对象等。std::function对象是对C++中现有的可调用实体的一种类型安全的包裹（我们知道像函数指针这类可调用实体，是类型不安全的）。 通常std::function是一个函数对象类，它包装其它任意的函数对象，被包装的函数对象具有类型为T1, …,TN的N个参数，并且返回一个可转换到R类型的值。std::function使用 模板转换构造函数接收被包装的函数对象；特别是，闭包类型可以隐式地转换为std::function。 
也就是说，通过std::function对C++中各种可调用实体（普通函数、Lambda表达式、函数指针、以及其它函数对象等）的封装，形成一个新的可调用的std::function对象；让我们不再纠结那么多的可调用实体。一切变的简单粗暴。




https://blog.csdn.net/vict_wang/article/details/81590984?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160571799819724836724908%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=160571799819724836724908&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v28-6-81590984.pc_first_rank_v2_rank_v28&utm_term=%E5%87%BD%E6%95%B0%E5%AF%B9%E8%B1%A1+c%2B%2B&spm=1018.2118.3001.4449
