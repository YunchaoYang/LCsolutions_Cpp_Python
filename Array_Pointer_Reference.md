
* Array name is a fixed pointer to the beginning of a block of memories
* 

Static array:
```cpp
int a[5],p 
```
Dynamic array:
```cpp
p = new int[n]
```

```cpp
    int a = 3;
    int b = 4;

    int* pointerToA = &a;
    int* pointerToB = &b;
    int* p = pointerToA;
    cout << p << endl;

    p = pointerToB;
    printf("%d %d %d\n", a, b, *p); // Prints 3 4 4
    cout << p << endl;

    int& referenceToA = a;
    int& referenceToB = b;
    int& r = referenceToA;
    cout << referenceToA <<' '<< referenceToB <<' '<< r <<' '<< endl;
    r = referenceToB;
    printf("%d %d %d\n", a, b, r); // Prints 4 4 4
    cout << referenceToA <<' '<< referenceToB <<' '<< r <<' '<< endl;
```
如何记忆
1 \*， 代表取“地址”
2 \&, 永远代表取“值”，因为是代表and

reference就是指向改地址的值，一定注意到值

