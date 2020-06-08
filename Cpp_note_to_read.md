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

```
