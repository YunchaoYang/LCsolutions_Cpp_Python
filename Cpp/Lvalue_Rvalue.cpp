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
 
 int square1(const int& x) {return x*x;} // both square1(40) and square1(i) work.

 
 
