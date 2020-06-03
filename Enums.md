Enums or Enumerated type (enumeration) is a user-defined data type which can be assigned some limited values. 
These values are defined by the programmer at the time of declaring the enumerated type.

```cpp 
#include <iostream>
using namespace std;
enum direction {East=11, West=22, North=33, South=44};
int main(){
   direction dir;
   dir = South;
   cout<<dir; 
   return 0;
}
```

give consts names

* Enum Class
C++11 has introduced enum classes (also called scoped enumerations), that makes enumerations both strongly typed and strongly scoped. 
Class enum doesn’t allow implicit conversion to int, and also doesn’t compare enumerators from different enumerations.
```cpp 
// Declaration
enum class EnumName{ Value1, Value2, ... ValueN};
// Initialisation
EnumName ObjectName = EnumName::Value;
```
```cpp
// C++ program to demonstrate working 
// of Enum Classes 
  
#include <iostream> 
using namespace std; 
  
int main() 
{ 
  
    enum class Color { Red, 
                       Green, 
                       Blue }; 
    enum class Color2 { Red, 
                        Black, 
                        White }; 
    enum class People { Good, 
                        Bad }; 
  
    // An enum value can now be used 
    // to create variables 
    int Green = 10; 
  
    // Instantiating the Enum Class 
    Color x = Color::Green; 
  
    // Comparison now is completely type-safe 
    if (x == Color::Red) 
        cout << "It's Red\n"; 
    else
        cout << "It's not Red\n"; 
  
    People p = People::Good; 
  
    if (p == People::Bad) 
        cout << "Bad people\n"; 
    else
        cout << "Good people\n"; 
  
    // gives an error 
    // if(x == p) 
    // cout<<"red is equal to good"; 
  
    // won't work as there is no 
    // implicit conversion to int 
    // cout<< x; 
  
    cout << int(x); 
  
    return 0; 
} 
```
