Notes from reading https://www.learncpp.com/cpp-tutorial/constructors-and-initialization-of-derived-classes/

- Here’s what actually happens when derived is instantiated:
  - 1. Memory for derived is set aside (enough for both the Base and Derived portions)
  - 2. The appropriate Derived constructor is called
  - 3. The `Base object` is constructed first using the appropriate __Base constructor__. If no base constructor is specified, the __default constructor__ will be used.
  - 4. The __initialization list__:, ,  initializes variables
  - 5. The body of the constructor{} executes,
  - 6. Control is returned to the caller

```cpp
class Base
{
public:
    int m_id;
 
    Base(int id=0)
        : m_id{ id }
    {
    }
 
    int getId() const { return m_id; }
};
 
class Derived: public Base
{
public:
    double m_cost;
 
    Derived(double cost=0.0)
        : m_cost{ cost }
    {
    }
 
    double getCost() const { return m_cost; }
};

int main()
{
    Base base{ 5 }; // use Base(int) constructor
    Derived derived{ 1.3 }; // use Derived(double) constructor
    return 0;
}
```

### Initializing base class members
One of the current shortcomings of our Derived class as written is that there is no way to initialize m_id when we create a Derived object. 

-  What if we want to set both m_cost (from the Derived portion of the object) and m_id (from the Base portion of the object) when we create a Derived object?

```cpp
class Derived: public Base
{
public:
    double m_cost;
 
    Derived(double cost=0.0, int id=0)
        // does not work
        : m_cost{ cost }, m_id{ id }
    {
    }
 
    double getCost() const { return m_cost; }
};
```
This is not right. C++ prevents classes from initializing inherited member variables in the initialization list of a constructor. 
In other words, the value of a member variable can only be set in an initialization list of a constructor belonging to the same class as the variable.

```cpp
class Derived: public Base
{
public:
    double m_cost;
 
    Derived(double cost=0.0, int id=0)
        : m_cost{ cost }
    {
        m_id = id; // assign again
    }
 
    double getCost() const { return m_cost; }
};
```

While this actually works in this case, it wouldn’t work if m_id were a const or a reference
(because const values and references have to be initialized in the initialization list of the constructor). 
It’s also inefficient because m_id gets assigned a value twice: once in the initialization list of the Base class constructor, 
and then again in the body of the Derived class constructor. And finally, what if the Base class needed access to this value during construction? 
It has no way to access it, since it’s not set until the Derived constructor is executed (which pretty much happens last).

So how do we properly initialize m_id when creating a Derived class object?

In all of the examples so far, when we instantiate a Derived class object, the Base class portion has been created using the default Base constructor. Why does it always use the default Base constructor? Because we never told it to do otherwise!

Fortunately, C++ gives us the ability to explicitly choose which Base class constructor will be called! 
To do this, simply add a call to the base class Constructor in the initialization list of the derived class:

```cpp
class Derived: public Base
{
public:
    double m_cost;
 
    Derived(double cost=0.0, int id=0)
        : Base{ id }, // Call Base(int) constructor with value id!
            m_cost{ cost }
    {
    }
 
    double getCost() const { return m_cost; }
};
```
Now, when we execute this code:

```cpp
int main()
{
    Derived derived{ 1.3, 5 }; // use Derived(double, int) constructor
    std::cout << "Id: " << derived.getId() << '\n';
    std::cout << "Cost: " << derived.getCost() << '\n';
 
    return 0;
}
```
In more detail, here’s what happens:

*  Memory for derived is allocated.
*  The Derived(double, int) constructor is called, where cost = 1.3, and id = 5
*  The compiler looks to see if we’ve asked for a particular Base class constructor. We have! So it calls Base(int) with id = 5.
*  The base class constructor initialization list sets m_id to 5
*  The base class constructor body executes, which does nothing
*  The base class constructor returns
*  The derived class constructor initialization list sets m_cost to 1.3
*  The derived class constructor body executes, which does nothing
*  The derived class constructor returns

Now we can make our members private

Now that you know how to initialize base class members, there’s no need to keep our member variables public. We make our member variables private again, as they should be.

As a quick refresher, public members can be accessed by anybody. 
Private members can only be accessed by member functions of the same class. 
Note that this means derived classes can not access private members of the base class directly! 
Derived classes will need to use access functions to access private members of the base class.

```cpp
#include <iostream>
 
class Base
{
private: // our member is now private
    int m_id;
 
public:
    Base(int id=0)
        : m_id{ id }
    {
    }
 
    int getId() const { return m_id; }
};
 
class Derived: public Base
{
private: // our member is now private
    double m_cost;
 
public:
    Derived(double cost=0.0, int id=0)
        : Base{ id }, // Call Base(int) constructor with value id!
            m_cost{ cost }
    {
    }
 
    double getCost() const { return m_cost; }
};
 
int main()
{
    Derived derived{ 1.3, 5 }; // use Derived(double, int) constructor
    std::cout << "Id: " << derived.getId() << '\n';
    std::cout << "Cost: " << derived.getCost() << '\n';
 
    return 0;
}
```

In the above code, we’ve made m_id and m_cost private. This is fine, since we use the relevant constructors to initialize them, and use a public accessor to get the values.

This prints, as expected:

Id: 5

Cost: 1.3

This is confusing because the inherited class does not hold the private member of base class, but still there exists the private data in the derived object here. 
Look at this perfect explanation: 
`A derived class doesn't inherit access to private data members. However, it does inherit a full parent object, which contains any private members which that class declares.`


