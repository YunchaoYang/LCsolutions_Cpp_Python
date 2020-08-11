https://www.cnblogs.com/fly1988happy/archive/2012/04/26/2471099.html

# 当编译器看到这个句子：
string *ps=new string("memory management");

它必须产生一些代码，或多或少会反映如下行为：

1) void* memory=operator new(sizeof(string));   //取得原始内存，用于放置一个string对象

2) call string::string("memory management") on *memory;//将内存中对象初始化

3) string *ps=static_cast<string*>(memory);   //让ps指向新完成的对象
