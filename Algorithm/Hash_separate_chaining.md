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

Sample code from greek
```cpp
// C++ implementation of Hashtable 
// using doubly linked list 
#include <bits/stdc++.h> 
using namespace std; 

const int tablesize = 25; 

// declaration of node 
struct hash_node { 
	int val, key; 
	hash_node* next; 
	hash_node* prev; 
}; 

// hashmap's declaration 
class HashMap { 
public: 
	hash_node **hashtable, **top; 

	// constructor 
	HashMap() 
	{ 
		// create a empty hashtable 
		hashtable = new hash_node*[tablesize]; 
		top = new hash_node*[tablesize]; 
		for (int i = 0; i < tablesize; i++) { 
			hashtable[i] = NULL; 
			top[i] = NULL; 
		} 
	} 

	// destructor 
	~HashMap() 
	{ 
		delete[] hashtable; 
	} 

	// hash function definition 
	int HashFunc(int key) 
	{ 
		return key % tablesize; 
	} 

	// searching method 
	void find(int key) 
	{ 
		// Applying hashFunc to find 
		// index for given key 
		int hash_val = HashFunc(key); 
		bool flag = false; 
		hash_node* entry = hashtable[hash_val]; 

		// if hashtable at that index has some 
		// values stored 
		if (entry != NULL) { 
			while (entry != NULL) { 
				if (entry->key == key) { 
					flag = true; 
				} 
				if (flag) { 
					cout << "Element found at key "
						<< key << ": "; 
					cout << entry->val << endl; 
				} 
				entry = entry->next; 
			} 
		} 
		if (!flag) 
			cout << "No Element found at key "
				<< key << endl; 
	} 

	// removing an element 
	void remove(int key) 
	{ 
		// Applying hashFunc to find 
		// index for given key 
		int hash_val = HashFunc(key); 
		hash_node* entry = hashtable[hash_val]; 
		if (entry->key != key || entry == NULL) { 
			cout << "Couldn't find any element at this key "
				<< key << endl; 
			return; 
		} 

		// if some values are present at that key & 
		// traversing the list and removing all values 
		while (entry != NULL) { 
			if (entry->next == NULL) { 
				if (entry->prev == NULL) { 
					hashtable[hash_val] = NULL; 
					top[hash_val] = NULL; 
					delete entry; 
					break; 
				} 
				else { 
					top[hash_val] = entry->prev; 
					top[hash_val]->next = NULL; 
					delete entry; 
					entry = top[hash_val]; 
				} 
			} 
			entry = entry->next; 
		} 
		cout << "Element was successfully removed at the key "
			<< key << endl; 
	} 

	// inserting method 
	void add(int key, int value) 
	{ 
		// Applying hashFunc to find 
		// index for given key 
		int hash_val = HashFunc(key); 
		hash_node* entry = hashtable[hash_val]; 

		// if key has no value stored 
		if (entry == NULL) { 
			// creating new node 
			entry = new hash_node; 
			entry->val = value; 
			entry->key = key; 
			entry->next = NULL; 
			entry->prev = NULL; 
			hashtable[hash_val] = entry; 
			top[hash_val] = entry; 
		} 

		// if some values are present 
		else { 
			// traversing till the end of 
			// the list 
			while (entry != NULL) 
				entry = entry->next; 

			// creating the new node 
			entry = new hash_node; 
			entry->val = value; 
			entry->key = key; 
			entry->next = NULL; 
			entry->prev = top[hash_val]; 
			top[hash_val]->next = entry; 
			top[hash_val] = entry; 
		} 
		cout << "Value " << value << " was successfully"
				" added at key " << key << endl; 
	} 
}; 

// Driver Code 
int main() 
{ 
	HashMap hash; 
	hash.add(4, 5); 
	hash.find(4); 
	hash.remove(4); 
	return 0; 
} 

```
