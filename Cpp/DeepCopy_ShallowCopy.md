# Why need
* Copy Constructor
* Default assignment operator

Depending upon the resources like dynamic memory held by the object, either we need to perform Shallow Copy or Deep Copy in order to create a replica of the object.

### Shallow Copying

``` cpp 
class X
{
private:
    int i;
    int *pi;
public:
    X()
        : pi(new int)
    { }
    X(const X& copy)   // <-- copy ctor
        : i(copy.i), pi(copy.pi)
    { }
};
```
### Deep Copying

``` cpp 
class X
{
private:
    int i;
    int *pi;
public:
    X()
        : pi(new int)
    { }
    X(const X& copy)   // <-- copy ctor
        : i(copy.i), pi(new int(*copy.pi))  // <-- note this line in particular!
    { }
};
```
