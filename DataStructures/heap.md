### basic concept

* Priority queues can be implemented by heaps, and heaps can be implemented by arrays.

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
