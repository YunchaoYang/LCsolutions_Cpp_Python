
### How to use class in class?
```cpp
class Point {
 public: double x, y;
};

class Vector {
 public: Point start, end;
 
 void offset(double offsetX, double offsetY) {
 start.x += offsetX;
 end.x += offsetX;
 start.y += offsetY;
 end.y += offsetY;
 }
 void print() {
 cout << "(" << start.x << "," << start.y << ") -> (" << end.x <<
"," << end.y << ")" << endl;
 }
};
int main() {
 Vector vec;
vec.start.x = 1.2;
}
```

```cpp
class Vector {
public:
 Point start, end;
 void offset(double offsetX, double offsetY) {
 start.offset(offsetX, offsetY);
 end.offset(offsetX, offsetY);
 }
 void print() {
 start.print();
 cout << " -> ";
 end.print();
 cout << endl;
 }
}; 

class Point {
public:
 double x, y;
 void offset(double offsetX, double offsetY) {
 x += offsetX; y += offsetY;
 }
 void print() {
 cout << "(" << x << "," << y << ")";
 }
};
```
### char* vs std:string vs char[] in C++
https://www.geeksforgeeks.org/char-vs-stdstring-vs-char-c/
http://cpp.sh/95v

The null character '\0' (also null terminator), abbreviated NUL, is a control character with the value zero.
