# Constructors in C++
* Default Constructors
* Parameterized Constructors: 
* Copy Constructor: `ClassName (const ClassName &old_obj);` 
## Default Constructors

## Parameterized Constructors: 

## Copy Constructor
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
