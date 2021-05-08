
## Elements for Hashing

1. Hash function
2. An array
3. Collision

## Lesson 1.1.2 Hashing - Hash Function

1. Onto function

Contains hash and compression
1. Computation time O(1)
2. Deterministic 
3. Satisfy SUHA (simple uniform hashing assumption)

## Lesson 1.1.3 Hashing - Hash Function Examples
Hashing function can performs quite different in different applications 
- Alice WonderLand, hashing each line with first 8 characters
- Wikipedia url, first 8 characters are the same value.

## Lesson 1.1.4 Collision Handling I: Separate Chaining
Dealing with the collision like a linked list, append the collisional elements to original elements.

* load factor

The load factor of the table is alpha is going to be defined as the number of elements inside of the table divided by the size of the table itself. 
