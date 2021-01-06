### basic concept

#### heap vs priority queue
heap并不属于STL容器组件，它分为 max heap 和min heap，在缺省情况下，max-heap是优先队列（priority queue）的底层实现机制。而这个实现机制中的max-heap实际上是以一个vector表现的完全二叉树（complete binary tree）。STL在<algorithm.h>中实现了对存储在vector/deque 中的元素进行堆操作的函数，包括make_heap, pop_heap, push_heap, sort_heap
* Priority queues can be implemented by heaps, and heaps can be implemented by arrays.

* Heap是一种数据结构，能保证取max/min是O(1)时间。


https://blog.csdn.net/tuke_tuke/article/details/50357939

###heap quiz
https://www.geeksforgeeks.org/data-structure-gq/heap-gq/

1. What is the time complexity of Build Heap operation. Build Heap is used to build a max(or min) binary heap from a given array. 
Build Heap is used in Heap Sort as a first step for sorting. O(n)
```
BUILD-HEAP(A) 
    heapsize := size(A); 
    for i := floor(heapsize/2) downto 1 
        do HEAPIFY(A, i); 
    end for 
END
```
Heapify costs O(lg(n)) and Build-Heap makes O(n) such calls. This upper bound O(nlg(n)), though correct, is not asymptotically tight. 

We can derive a tighter bound by observing that the running time of Heapify depends on the height of the tree ‘h’
(which is equal to lg(n), where n is number of nodes) and the heights of most sub-trees are small.
https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/

2. 
