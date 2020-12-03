### Reference

[](https://www.ibm.com/developerworks/cn/aix/library/au-boostserialization/index.html#resources)

### 字符串string内容归档到文本文件中
```
#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
```

1. `std::ofstream file("filename.txt");`
2. `boost::archive::textoarchive oa(file);`
3. `std::string s = "Hello World";`
3. `os & s;` 使用&运算符执行“转储-恢复”操作

Boost 创建了一个文本归档文件（一个文本文件），它含有需要转储的内容。为了转储这些内容，您需要创建了一个 text_oarchive。为了恢复内容，您还创建了一个 text_iarchive，并分别在头文件 text_oarchive.hpp 和 text_iarchive.hpp 中声明它。转储和恢复内容很直观，使用 << 和 >> 运算符，
其工作原理非常类似于流 I/O，除了要将内容转储到文件中，然后过一段时间以后再从该文件中恢复。
不过，您可能想只用一个 & 运算符完成转储和恢复操作，而不是使用上述的两个不同运算符。

### 从xml文档文件执行“转储-恢复”操作

```cpp
#include <boost/archive/xml_iarchive.hpp>
#include <boost/archive/xml_oarchive.hpp>

oa & BOOST_SERIALIZATION_NVP(s);  //如果您想使用 XML 归档文件，而不是文本归档文件,需要将数据打包到一个名为 BOOST_SERIALIZATION_NVP 的宏中
```
变量名可充当标记 (<s>Hello World!</s>)。

### 
要对某个类进行序列化，则必须在类定义中定义一个名为 serialize 的方法。在转储和恢复类的过程中会调用该方法。以下是对 serialize 方法的声明：
```cpp
// serialize 是一个模板函数，
template<class Archive>
void serialize(Archive& archive, const unsigned int version) // 第一个参数是对 Boost 归档文件的引用。
{
    archive & BOOST_SERIALIZATION_NVP(m_day);
    archive & BOOST_SERIALIZATION_NVP(m_month);
    archive & BOOST_SERIALIZATION_NVP(m_year);
}
```
BOOST_SERIALIZATION_NVP is a macro, boost::serialization::make_nvp()

### 处理类层次结构
类通常是从其他类派生的，因此您需要找到一种能够在序列化派生类的同时序列化基类的方法。
对于基类和派生类，都必须定义 serialize 方法。
另外，还需要调整派生类的 serialize 定义。

```cpp
template<class Archive>
void serialize(Archive& archive, const unsigned int version)
{
     // serialize base class information
     archive & boost::serialization::base_object<Base Class>(*this);
     // serialize derived class members
     archive & derived-class-member1;
     archive & derived-class-member2;
     // … 
}
```
直接在派生类的 serialize 方法中调用基类的 serialize 方法是一个很糟糕的想法。
尽管能够这么做，但是无法追踪类版本控制（稍后讲述），或者无法消除生成的归档文件中的冗余。
避免这种错误的一种推荐编码方式是在 __所有类__ 中将 `serialize` 方法设置为 `private`，
并在所有将要序列化的类中使用 `friend class boost::serialization::access` 声明。

### 通过基类指针转储派生类
通过指针转储派生类是完全有可能的；但是，该类和派生类都应该有各自的已定义的 serialize 方法。还有，您需要在转储和恢复过程中调用以下方法。
`<archive name>.register_type<derived-type name>( )`

* 使用Base class pointer基类指针实现派生类Derived object序列化:

```cpp
void save() 
{ 
  std::ofstream file("archive.xml"); 
  boost::archive::xml_oarchive oa(file); 
  oa.register_type<date>( );  // 注册 date 类型。
  base* b = new date(15, 8, 1947);
  oa & BOOST_SERIALIZATION_NVP(b); 
} 
 
void load() 
{ 
  std::ifstream file("archive.xml"); 
  boost::archive::xml_iarchive ia(file); 
  ia.register_type<date>( ); // 注册 date 类型。
  base *dr;
  ia >> BOOST_SERIALIZATION_NVP(dr); 
  date* dr2 = dynamic_cast<date*> (dr); 
  std::cout << dr2;
}
```
在这里，在转储和恢复过程中使用了 base 指针。但序列化的实际上是 date 对象。
在转储和恢复之前，已经在这两个类中注册了 date 类型。

### 在执行 “转储 - 恢复” 操作过程中使用对象指针(Object Pointer)

* 使用指针执行 “转储 - 恢复” 操作
```cpp
void save() 
{ 
  std::ofstream file("archive.xml"); 
  boost::archive::xml_oarchive oa(file); 
  date* d = new date(15, 8, 1947); // d对象指针(Object Pointer)
  std::cout << d << std::endl;
  oa & BOOST_SERIALIZATION_NVP(d); 
  // … other code follows
} 
 
void load() 
{ 
  std::ifstream file("archive.xml"); 
  boost::archive::xml_iarchive ia(file); 
  date* dr;                    // d对象指针(Object Pointer) 请注意，在此清单中，d 和 dr 的值是不同的，但内容相同。
  ia >> BOOST_SERIALIZATION_NVP(dr); 
  std::cout << dr << std::endl;
  std::cout << *dr;
}
```

* 两个指针转储到同一个对象, 只有一个对象被转储。第二个指针处理方法, 加入 <d2 class_id_reference="0" object_id_reference="_0"></d2>

* 引用的处理方法:
对于引用的处理方法与用户应用程序代码中一样。尽管如此，请注意，在恢复过程中，创建了两个独特的对象。因此，归档文件应该保存两个具有相同值的对象。

### 将 serialize 拆分成 save 和 load
有时候，您不想使用同样的 serialize 方法来转储和恢复对象。
在这种情况下，您可以将 serialize 方法拆分成两个方法，
即 save() 和 load()，它们具有类似的签名?。
这两个方法都是之前定义的 serialize() 方法的一部分。

```cpp
template<class Archive>
void save(Archive& archive, const unsigned int version) const
{
//… 
} 
 
template<class Archive>
void load(Archive& archive, const unsigned int version)
{
//…
} 
 
BOOST_SERIALIZATION_SPLIT_MEMBER( ) // must be part of class
```
注意 save 方法签名后的 const。如果没有 const 限定符，该代码将无法编译。

* date 类:
```
template<class Archive>
void save(Archive& archive, const unsigned int version) const
{
    archive << BOOST_SERIALIZATION_NVP(m_day);
    archive << BOOST_SERIALIZATION_NVP(m_month);
    archive << BOOST_SERIALIZATION_NVP(m_year)
} 
 
template<class Archive>
void load(Archive& archive, const unsigned int version)
{
    archive >> BOOST_SERIALIZATION_NVP(m_day);
    archive >> BOOST_SERIALIZATION_NVP(m_month);
    archive >> BOOST_SERIALIZATION_NVP(m_year)
} 
 
BOOST_SERIALIZATION_SPLIT_MEMBER( ) // must be part of class
```

### 使用共享指针
共享指针是一项经常使用且功能极其强大的编程技术。再次强调，Boost Serialization 一个主要优势在于能轻松将共享指针序列化，并保持目前所知的语法不变。
* 注意1，必须在应用程序代码中包含 boost/serialization/shared_ptr.hpp 头文件

* 2 指向栈对象的指针需要在实际对象之后转储

* 3. 如果有多个指针指向同一个对象，Serialization 会使用 class_id_reference 将指针与原对象关联起来（每个对象都有一个唯一的类 ID）。原对象的每个后续指针都会将 object_id_reference 改成 _1、_2，以此类推。


#### [C++Boost序列化（Serialization）库教程](https://blog.csdn.net/qq2399431200/article/details/45621921?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522160694445319215668815520%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=160694445319215668815520&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-2-45621921.pc_first_rank_v2_rank_v28&utm_term=c++%20serialization&spm=1018.2118.3001.4449)


### 对整数数组 Array of integers “转储-恢复”操作
```cpp
#include <boost/archive/xml_oarchive.hpp>
#include <boost/archive/xml_iarchive.hpp>

  int arrary1[ ] = { 34, 78, 22, 1, 910 };
	oa & BOOST_SERIALIZATION_NVP(arrary1);
```
### 串行化STL集合
```cpp
#include <boost/serialization/list.hpp>
#include <boost/serialization/vector.hpp>

	float array[ ] = {34.2, 78.1, 22.221, 1.0, -910.88};
	std::list<float> L1(array, array+5);
	std::vector<float> V1(array, array+5);
	oa & BOOST_SERIALIZATION_NVP(L1);
	oa & BOOST_SERIALIZATION_NVP(V1);
```

### serialize方法的侵入版本

```cpp
typedef struct date{
	unsigned int m_day;
	unsigned int m_month;
	unsigned int m_year;
 
	date(int d, int m, int y):m_day(d), m_month(m) ,m_year(y) {  }
	date( ):m_day(1),m_month(1),m_year(2000) { }
	
	friend std::ostream& operator << (std::ostream& out, date& d)
	{
		out << "day:" << d.m_day << "month:" << d.m_month << "year:" << d.m_year;
		return out;
	}
	
	template<typename Archive>
	void serialize(Archive& archive, const unsigned int version)
	{
		archive & BOOST_SERIALIZATION_NVP(m_day);
		archive & BOOST_SERIALIZATION_NVP(m_month);
		archive & BOOST_SERIALIZATION_NVP(m_year);
	}
	
}date;

void save( )
{
	std::ofstream file("archive.xml");
	boost::archive::xml_oarchive oa(file);
	date d(15, 8, 1947);
	oa & BOOST_SERIALIZATION_NVP(d); 	//
}

void load( )
{
	std::ifstream file("archive.xml");
	boost::archive::xml_iarchive ia(file);
	date dr;
	ia >> BOOST_SERIALIZATION_NVP(dr); // using >> operator
	std::cout << dr;		   // using << operator 
}

```
### serialize方法的非侵入版本

```
typedef struct date
{
	...
	friend std::ostream& operator << (std::ostream& out, date& d)
	{
		out << "day:" << d.m_day << "month:" << d.m_month << "year:" << d.m_year;
		return out;
	}
}date;

// 序列化相关的类和函数都属于boost::serialization命名空间里，所以自定义的serialize函数也可被其中的其它类和函数调用
namespace boost
{
	namespace serialization
	{
		template<typename Archive>
		void serialize(Archive& archive, date& d, const unsigned int version)
		{
			archive & BOOST_SERIALIZATION_NVP(d.m_day);
			archive & BOOST_SERIALIZATION_NVP(d.m_month);
			archive & BOOST_SERIALIZATION_NVP(d.m_year);
		}
	}
}

```
### 使用xml文件归档

### 文本文件归档

### 使用指针执行“转储-恢复”操作

#### 将两个指针转储到同一个对象

### 包含作为d的引用d2的归档文件

### serialize拆成save和load

### Boost::serialize的版本控制

### 使用共享指针boost::shared_ptr执行“转储-恢复”操作

### 指向栈对象的指针需要在实际对象之后转储
