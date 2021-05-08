# 2 Disjoint Sets

## 2.2.1 Disjoint Sets ADT
* Maintain a collection S = {s0,s1,...sk}
* Each set has a representative member

* Methods
  * Find
  * Union
 
* API
  * `void makeSet(const T& t);`
  * `void set_union(const T & k1, const T& k2);`
  * `T & find(const T & k);`

"Disjoint Sets" are sometimes refered to as "Union-Find" data structure, because of its primary methods, union and find.

## 2.1.2 Disjoint Sets: Naive Implementation

Each member is initialized as an "set identity", the first member of this set. 

- Find O(1)
- Union O(n) - traverse entire array

## 2.1.3 Disjoint Sets: UpTrees - A Better Implementation

* We will continue to use an array where the index is the key.
* The value of the array is:
   * -1, if we ahve found the represented element
   * the index of the parent, if we haven't found the present element.
   
 It is called __UpTrees__.
 
* Example:

  Union: put the parent index, no need to traverse entire tree 

- Union two tree, just need to update the root tree
 
 The worst case is that the tree behaves like a long single linked list.
 
## 2.1.4 UpTrees: Simple Running Time
 
 ```cpp
 int DisjointSets::find()
 {
    if ( s[i] < 0 ) 
        return i;
    else  
        return _find(s[i]); 
} 
 ```
 
-  Running time?
    - proportional to the height of the tree. 
    - O(h)
    - worst case (linked list): h = N;
    - best case (ideal structure): a single root node, each child is directly linked to root. h = 1
    
## 2.1.5A UpTrees: Smart Union & Path Compression I

- Good tree: Short and wide 
- Bad tree: long and thin

- Represent the root tree not -1, but (-h-1) . 

- Union by Height
   - When unioning tree together, add the shorter tree to higher tree. 
- Union by Size
   - Add smaller-size tree to the larger-size tree.

- Both guarantee h - O(lg(n)).

### Path Compression in "find(s)" method;
Each node in the route of finding an element s, update all node pointing directly to the root node .


### 2.1.5B UpTrees: Smart Union & Path Compression II
- Disjoint Set Analysis
   - The __iterated log__ function: The number of times you can take a log of a number;

- log*(n) = 
  - 0, if( n <= 1)
  - 1 + log*(log(n)), if ( n > 1)

What is __lg*(2^65536)__?
