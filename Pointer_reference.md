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
