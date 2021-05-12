

### Difference ADT vs Data Structure
ADT is a logical description and data structure is concrete. 
ADT is the logical picture of the data and the operations to manipulate the component elements of the data. 
Data structure is the actual representation of the data during the implementation and the algorithms to manipulate the data elements.

- ADT is implementation independent. For example, it only describes what a data type _List_ consists (data) and what are the operations it can perform, but it has no information about how the List is actually implemented.
- Data structure is implementation dependent, as in the same example, it is about how the List implemented ie., using array or linked list. Ultimately, data structure is how we implement the data in an abstract data type.

### Commonly Used Abstract Data Type(ADT)
- List (or sequence or vector)
- Set
- Multi-set (or bag)
- Stack
- Queue
- Priority Queue
- Tree (A generalized tree has a value and children)
- Map (or dictionary) 

### Commonly Used Data Structures 
- array
- linked list (Doubly Linked List)
- hash table (open, closed, circular hashing) 
- trees (binary search trees, heaps, AVL trees, 2-3 trees, tries, red/black trees, B-trees)

### Implementing an ADT
* Interface (*.h):
  - class declaration
  - prototypes for the operations (interface)
  - data members for the actual (concrete) representation
* Implementation (*.cpp)
  - function definitions for the operations
  - depends on representation of data members (their oncrete implementation)

## STL: Standard Template Library of ADTs implemented in C++
Two categories of STL ADTs:
- containers: classes that store a collection of data and impose some organization on it
- iterators: behave like pointers; a mechanism for accessing elements in a container the iterator is associated with

* array: Static contiguous array (class template)
* vector: Dynamic contiguous array (class template)
* deque: Double-ended queue (class template)
* forward_list: Singly-linked list (class template)
* list : Doubly-linked list (class template)

* Set: Collection of unique keys, sorted by keys
(class template)
* Map: Collection of key-value pairs, sorted by keys, keys are unique (class template).
* multiset: Collection of keys, sorted by keys (class template)
* multimap: Collection of key-value pairs, sorted by keys (class template)

https://userweb.cs.txstate.edu/~js236/201505/cs3358/w5adtintro.pdf
