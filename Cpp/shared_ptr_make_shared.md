A good image shows what is in a smart pointer.
![ST5xPgtrtB0ZluZibn6rSw3p](https://user-images.githubusercontent.com/6526592/118654224-56048600-b7b6-11eb-83a0-c7b7db3b94f7.png)

Whenever possible, use the make_shared function to create a shared_ptr when the memory resource is created for the first time. 
`make_shared` is exception-safe. It uses the same call to allocate the memory for the control block and the resource, which reduces the construction overhead. 
If you don't use make_shared, then you have to use an explicit new expression to create the object before you pass it to the shared_ptr constructor. 
The following example shows various ways to declare and initialize a shared_ptr together with a new object.

```cpp 
std::shared_ptr<int> foo = std::make_shared<int> (10);
```


``` cpp 
//example from microsoft

#include <memory> // the header for smart pointers



// Ok, but slightly less efficient. 
// Note: Using new expression as constructor argument
// creates no named variable for other code to access.
shared_ptr<Song> sp2(new Song(L"Lady Gaga", L"Just Dance"));

shared_ptr<Song> sp5(nullptr); //Equivalent to: shared_ptr<Song> sp5;
// When initialization must be separate from declaration, e.g. class members, 
// initialize with nullptr to make your programming intent explicit.
sp5 = make_shared<Song>(L"Elton John", L"I'm Still Standing");

//Initialize with copy constructor. Increments ref count.
auto sp3(sp2);

std::cout << sp2.use_count() << std::endl; // 2

//Initialize via assignment. Increments ref count.
shared_ptr<Song>  sp4 = sp2;

std::cout << sp2.use_count() << std::endl; // 3

//Initialize with nullptr. sp7 is empty.
shared_ptr<Song> sp7(nullptr);

// Initialize with another shared_ptr. sp1 and sp2
// swap pointers as well as ref counts.
sp1.swap(sp2);

// 
vector<shared_ptr<Song>> v {
  make_shared<Song>(L"Bob Dylan", L"The Times They Are A Changing"),
  make_shared<Song>(L"Aretha Franklin", L"Bridge Over Troubled Water"),
  make_shared<Song>(L"Thalía", L"Entre El Mar y Una Estrella")
};

vector<shared_ptr<Song>> v2;
remove_copy_if(v.begin(), v.end(), back_inserter(v2), [] (shared_ptr<Song> s) 
{
    return s->artist.compare(L"Bob Dylan") == 0;
});

for (const auto& s : v2)
{
    wcout << s->artist << L":" << s->title << endl;
}


```


``` cpp
// what is exactly smart ptr
#include <iostream> 
using namespace std; 
  
class SmartPtr { 
    int* ptr; // Actual pointer 
public: 
    // Constructor: Refer https:// www.geeksforgeeks.org/g-fact-93/ 
    // for use of explicit keyword 
    explicit SmartPtr(int* p = NULL) { ptr = p; } 
    
    // Destructor 
    ~SmartPtr() { delete (ptr); } 
  
    // Overloading dereferencing operator 
    int& operator*() { return *ptr; } 
}; 
  
int main() 
{ 
    SmartPtr ptr(new int()); 
    *ptr = 20; 
    cout << *ptr; 
  
    // We don't need to call delete ptr: when the object 
    // ptr goes out of scope, the destructor for it is automatically 
    // called and destructor does delete ptr. 
  
    return 0; 
}

```
