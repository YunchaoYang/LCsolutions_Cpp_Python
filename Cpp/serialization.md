### Reference
#### [C++Boost序列化（Serialization）库教程](https://blog.csdn.net/qq2399431200/article/details/45621921?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160694445319215668815520%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160694445319215668815520&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-2-45621921.pc_first_rank_v2_rank_v28&utm_term=c++%20serialization&spm=1018.2118.3001.4449)

### 字符串string内容归档到文本文件中

1. `std::ofstream file("filename.txt");`
2. `boost::archive::textoarchive oa(file);`
3. `std::string s = "Hello World";`
3. `os & s;` 使用&运算符执行“转储-恢复”操作

### 从xml文档文件执行“转储-恢复”操作
*	`oa & BOOST_SERIALIZATION_NVP(s); ` //如果您想使用 XML 归档文件，而不是文本归档文件,需要将数据打包到一个名为 BOOST_SERIALIZATION_NVP 的宏中


### 对整数数组执行“转储-恢复”操作

### 非侵入版本

### 使用xml文件归档

### 文本文件归档

### 使用指针执行“转储-恢复”操作

#### 将两个指针转储到同一个对象

### 包含作为d的引用d2的归档文件

### serialize拆成save和load

### Boost::serialize的版本控制

### 使用共享指针boost::shared_ptr执行“转储-恢复”操作

### 指向栈对象的指针需要在实际对象之后转储
