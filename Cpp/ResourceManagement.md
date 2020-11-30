RAII (Resource Acquisition Is Initialization)“以对象管理资源” 的概念,
有两个关键想法:
* 获得资源后立刻放入管理对象.
* 管理对象(managing object) 运用析构函数确保资源被释放

## Rule 13: Use objects to manage resources
将资源放到对象中, 当离开作用域, 调用对象的析构函数的时候, 再自动把资源给释放掉, 这样就能保证资源被合理的释放.

## Rule 14: Think carefully about copying behavior in resource-managing classes
对于RAII对象, 应该好好考虑它的复制行为.

允许复制? 那么应该考虑是 深拷贝( deep copying ) 还是 浅拷贝 ( shadow copying ).
如果是浅拷贝, 可以采用智能指针引用计数的方法来解决, 也就是说 RAII 对象中保留的是指向资源的智能指针, 这样可以保证复制时只是复制指针, 在释放时又不会出错.

普通而常见的 RAII class copying 行为是: 抑制 copying, 采用智能指针. 不过也有可能进行深拷贝或者别的操作

## Rule 15: Provide access to raw resources in resource-managing classes

还有隐式转换的方法, 能够略去每次调用 get() 的麻烦, 不过容易造成错误, 不建议使用.


