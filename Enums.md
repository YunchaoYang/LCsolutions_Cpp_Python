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
