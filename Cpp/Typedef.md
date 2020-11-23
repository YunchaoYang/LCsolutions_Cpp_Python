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
