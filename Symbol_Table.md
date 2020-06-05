# Algorithms

## Week4.2
_Key-value_ pair abstraction.
* `insert` a value with specified key.
* Given a key, `search` for the corresponding value.

```
A Symbol table is a data structure used by the `compiler`, where each identifier in program’s source code
is stored along with information associated with it relating to its `declaration`. 
It stores `identifier` as well as it’s associated `attributes` like scope, type, line-number of occurrence,etc.
```

* key-value pairs
![](https://algs4.cs.princeton.edu/31elementary/images/symbol-table-applications.png)


Symbol table can be implemented using various data structures like:
* Linked List (unordered list, search average cost N/2, insert average cost N,)
![](https://algs4.cs.princeton.edu/31elementary/images/sequential-search.png)
* Hash Table ()
* Binary Search Tree (ordered array, search average cost logN, insert average cost N/2)
![](https://algs4.cs.princeton.edu/31elementary/images/binary-search.png)

* Ordered symbol tables
In typical applications, keys are `Comparable` objects, so the option exists of using the code
`a.compareTo(b)` to compare two keys a and b. Several symbol-table implementations take advantage
of order among the keys that is implied by Comparable to provide efficient implementations of the
`put()` and `get()` operations. More important, in such implementations, we can think of the symbol
table as keeping the keys in order and consider a significantly expanded API that defines
numerous natural and useful operations involving relative key order. 

* Sequential search in an unordered linked list. 

* Operations of Symbol table 
![](https://media.geeksforgeeks.org/wp-content/uploads/asd1-1.png)

Basic symbole table API 
(array abstraction)

Convention

* Below is the sample C++ implementation of Symbol Table using the concept of 
Hashing with separate chaining:
by https://www.geeksforgeeks.org/cpp-program-to-implement-symbol-table/#:~:text=A%20Symbol%20table%20is%20a,%2Dnumber%20of%20occurrence%2C%20etc.

```cpp
// C++ program to implement Symbol Table 
#include <iostream> 
using namespace std; 

const int MAX = 100; 

class Node { 

	string identifier, scope, type; 
	int lineNo; 
	Node* next; 

public: 
	Node() 
	{ 
		next = NULL; 
	} 

	Node(string key, string value, string type, int lineNo) 
	{ 
		this->identifier = key; 
		this->scope = value; 
		this->type = type; 
		this->lineNo = lineNo; 
		next = NULL; 
	} 

	void print() 
	{ 
		cout << "Identifier's Name:" << identifier 
			<< "\nType:" << type 
			<< "\nScope: " << scope 
			<< "\nLine Number: " << lineNo << endl; 
	} 
	friend class SymbolTable; 
}; 

class SymbolTable { 
	Node* head[MAX]; 

public: 
	SymbolTable() 
	{ 
		for (int i = 0; i < MAX; i++) 
			head[i] = NULL; 
	} 

	int hashf(string id); // hash function 
	bool insert(string id, string scope, 
				string Type, int lineno); 

	string find(string id); 

	bool deleteRecord(string id); 

	bool modify(string id, string scope, 
				string Type, int lineno); 
}; 

// Function to modify an identifier 
bool SymbolTable::modify(string id, string s, 
						string t, int l) 
{ 
	int index = hashf(id); 
	Node* start = head[index]; 

	if (start == NULL) 
		return "-1"; 

	while (start != NULL) { 
		if (start->identifier == id) { 
			start->scope = s; 
			start->type = t; 
			start->lineNo = l; 
			return true; 
		} 
		start = start->next; 
	} 

	return false; // id not found 
} 

// Function to delete an identifier 
bool SymbolTable::deleteRecord(string id) 
{ 
	int index = hashf(id); 
	Node* tmp = head[index]; 
	Node* par = head[index]; 

	// no identifier is present at that index 
	if (tmp == NULL) { 
		return false; 
	} 
	// only one identifier is present 
	if (tmp->identifier == id && tmp->next == NULL) { 
		tmp->next = NULL; 
		delete tmp; 
		return true; 
	} 

	while (tmp->identifier != id && tmp->next != NULL) { 
		par = tmp; 
		tmp = tmp->next; 
	} 
	if (tmp->identifier == id && tmp->next != NULL) { 
		par->next = tmp->next; 
		tmp->next = NULL; 
		delete tmp; 
		return true; 
	} 

	// delete at the end 
	else { 
		par->next = NULL; 
		tmp->next = NULL; 
		delete tmp; 
		return true; 
	} 
	return false; 
} 

// Function to find an identifier 
string SymbolTable::find(string id) 
{ 
	int index = hashf(id); 
	Node* start = head[index]; 

	if (start == NULL) 
		return "-1"; 

	while (start != NULL) { 

		if (start->identifier == id) { 
			start->print(); 
			return start->scope; 
		} 

		start = start->next; 
	} 

	return "-1"; // not found 
} 

// Function to insert an identifier 
bool SymbolTable::insert(string id, string scope, 
						string Type, int lineno) 
{ 
	int index = hashf(id); 
	Node* p = new Node(id, scope, Type, lineno); 

	if (head[index] == NULL) { 
		head[index] = p; 
		cout << "\n"
			<< id << " inserted"; 

		return true; 
	} 

	else { 
		Node* start = head[index]; 
		while (start->next != NULL) 
			start = start->next; 

		start->next = p; 
		cout << "\n"
			<< id << " inserted"; 

		return true; 
	} 

	return false; 
} 

int SymbolTable::hashf(string id) 
{ 
	int asciiSum = 0; 

	for (int i = 0; i < id.length(); i++) { 
		asciiSum = asciiSum + id[i]; 
	} 

	return (asciiSum % 100); 
} 

// Driver code 
int main() 
{ 
	SymbolTable st; 
	string check; 
	cout << "**** SYMBOL_TABLE ****\n"; 

	// insert 'if' 
	if (st.insert("if", "local", "keyword", 4)) 
		cout << " -successfully"; 
	else
		cout << "\nFailed to insert.\n"; 

	// insert 'number' 
	if (st.insert("number", "global", "variable", 2)) 
		cout << " -successfully\n\n"; 
	else
		cout << "\nFailed to insert\n"; 

	// find 'if' 
	check = st.find("if"); 
	if (check != "-1") 
		cout << "Identifier Is present\n"; 
	else
		cout << "\nIdentifier Not Present\n"; 

	// delete 'if' 
	if (st.deleteRecord("if")) 
		cout << "if Identifier is deleted\n"; 
	else
		cout << "\nFailed to delete\n"; 

	// modify 'number' 
	if (st.modify("number", "global", "variable", 3)) 
		cout << "\nNumber Identifier updated\n"; 

	// find and print 'number' 
	check = st.find("number"); 
	if (check != "-1") 
		cout << "Identifier Is present\n"; 
	else
		cout << "\nIdentifier Not Present"; 

	return 0; 
} 
```
