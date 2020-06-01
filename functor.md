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
