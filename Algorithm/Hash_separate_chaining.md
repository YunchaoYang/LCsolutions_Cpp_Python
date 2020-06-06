# Separate Chaining Symbol Table (Open Hashing)
* How to deal with Collision?
* each entry in the hash table is a `linked list`
## Hash: map key to integer i in [0, M-1]
* Insert:put at ith chain
* Search: search ith chain list
* PrepositionL:
Under uniform hashing assumption, probablitity taht the number of kesy in a list
is within a constant factor of N/M is exteremely cloase to 1
* Proof sketch: Distribution of list size obeys a `binomial distribution`(二项分布)

## Hash Node Data Type
* M too large => too marny empty chains
* M too small => too long chain
* Typical choise M ~ N/5

`hash = hash_func(key)`

`index = hash % array_size`

Sample code from geeksforgeeks
https://www.geeksforgeeks.org/hashtables-chaining-with-doubly-linked-lists/
https://www.geeksforgeeks.org/c-program-hashing-chaining/
https://www.geeksforgeeks.org/program-to-implement-separate-chaining-in-c-stl-without-the-use-of-pointers/

```cpp
// CPP program to implement hashing with chaining
#include<bits/stdc++.h> //#include <bits/stdc++.h> is an implementation file for a precompiled header.
using namespace std;

class Hash
{
	int BUCKET; // No. of buckets

	// Pointer to an array containing buckets
	list<int> *table;
public:
	Hash(int V); // Constructor

	// inserts a key into hash table
	void insertItem(int x);

	// deletes a key from hash table
	void deleteItem(int key);

	// hash function to map values to key
	int hashFunction(int x) {
		return (x % BUCKET);
	}

	void displayHash();
};

// construction
Hash::Hash(int b)
{
	this->BUCKET = b;
	table = new list<int>[BUCKET];
}

// insertion
void Hash::insertItem(int key)
{
	int index = hashFunction(key);
	table[index].push_back(key);
}

void Hash::deleteItem(int key)
{
// get the hash index of key
int index = hashFunction(key);

// find the key in (index)th list
list <int> :: iterator i;
for (i = table[index].begin(); i != table[index].end(); i++) {
	if (*i == key)
	break;
}

// if key is found in hash table, remove it
if (i != table[index].end())
	table[index].erase(i);
}

// function to display hash table
void Hash::displayHash() {
for (int i = 0; i < BUCKET; i++) {
	cout << i;
	for (auto x : table[i])
	cout << " --> " << x;
	cout << endl;
}
}

// Driver program
int main()
{
// array that contains keys to be mapped
int a[] = {15, 11, 27, 8, 12};
int n = sizeof(a)/sizeof(a[0]);

// insert the keys into the hash table
Hash h(7); // 7 is count of buckets in
			// hash table
for (int i = 0; i < n; i++)
	h.insertItem(a[i]);

// delete 12 from hash table
h.deleteItem(12);

// display the Hash table
h.displayHash();

return 0;
}

```
