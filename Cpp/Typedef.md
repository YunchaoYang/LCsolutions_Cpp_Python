### Internal typedefs in C++ - good style or bad style?
```cpp
class Lorem
{
    typedef boost::shared_ptr<Lorem> ptr;
    typedef std::vector<Lorem::ptr>  vector;
}

Lorem::vector lorems;
Lorem::ptr    lorem( new Lorem() );

lorems.push_back( lorem );
```
https://stackoverflow.com/questions/759512/internal-typedefs-in-c-good-style-or-bad-style

### what is difference between typedef struct vs struct"?
```cpp
typedef struct S{
    int one;
    int two;
} S;
```

https://stackoverflow.com/questions/1675351/typedef-struct-vs-struct-definitions
