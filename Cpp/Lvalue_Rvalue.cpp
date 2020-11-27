/*
* lvalue - an object that occupies some identifieable location in memory 
* rvalue - not a lavlue
*/

//1. Lvalue example
int i;
int * p = &i ;
i = 2;


class dog;
dog d1; //lvalue of user defined types;

// 2. Rvalue Eg.
 int x = 2;
 int x = i+2
 int * p = &(i+2) // error
 i+2 = 4 // error
 2 = i // error 
 
 dog d1;
 d1 = dog(); // dog() is rvalue of user defined types
 
 int sum(int x, int y) {return x+y;}
 int i = sum(3,4) // sum(3,4) - rvalue
 
 //Rvalues: 2, i+2, sum(3,4), x+y
 //Lvalues: x,i,d1,p
 
 //3. Referece (or Lvalue reference)
 int i;
 int & r = i;
 
 int & r = 5; //error
 
 // * Exception: 
 // Constatnt lvalue reference can be assigned a rvalue;
 const int& r = 5;
 
 int square(int& x) {return x*x;}
 square(i) // OK
 square(40); //error
 
 //How to make square(40) work?
 // Walkaround
 int square1(const int& x) {return x*x;} // both square1(40) and square1(i) work.

 // lvalue can be used to create a rvalue
int i = 1;
int x = i+2;

int x = i; // a lvalue can be implicitly transformed to a rvalue.

//rvalue can be explicitly used to create a lvalue
int v[3];
*(v+2) = 4; // *(v+2) is a lvalue

//Misconcept 1: Function or operator always yields rvalue;
int x = i+3;
int y = sum(3,4);

// Counterexample 1
int myglobal;
int& foo(){
return myglobal;
}
foo() = 50;

// Counterexample 2
array[3] = 50; //operator [] almost always gnerates a lvalue;

//Misconcept 2: Lvalue are modifiable;
const int c = 1; // c is a lvalue
c = 2; // error

//Misconcept 3: Rvalue are not modifiable;
i+3 = 6;
sum(3,4) = 7;

// However, It is not true for user defined type(class)
class dog;
dog().bark(); // dog() is rvalue, is modifiable.
