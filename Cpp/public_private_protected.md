  ```cpp
 class Base
 {
  public: var

  private:
``` 

* Questions: What it the difference between public, private and protected?  
   * 1) Accessible 三种访问权限
       * `public` - can be accessed by objects in public. protected: 可以被该类中的函数、子类的函数、其友元函数访问,也可以由该类的对象访问 
       * `protected` - same as private. public: 
       可以被该类中的函数、子类的函数、以及其友元函数访问,但不能被该类的对象访问
       * `private` - only be accessed by the class member function and friend member function private: 
       只能由该类中的函数、其友元函数访问,不能被任何其他访问，该类的对象也不能访问. 

|          |class member function| child class member function|     friends    |      object      | 
|----------|---------------------|----------------------------|----------------|------------------|
|public    | Yes                 | Yes                        |Yes             |      Yes         |
|protected | Yes                 | Yes                        |Yes             |      No          |
|private   | Yes                 | No                         |Yes             |      No          |

* 2) inheritance  三种继承方式  
    * public inheritance - 
    使用public继承,父类中的方法属性不发生改变;
    * private inheritance -
    使用private继承,父类的所有方法在子类中变为private; 
    * protected inheritance - 
    使用protected继承,父类的protected和public方法在子类中变为protected,private方法不变; 

组合结果

|基类member |继承方式 |子类member|
|-----------------|-----------|---------|
|public |＆ public继承 |=> public|
|public |＆ protected继承| => protected|
|public |＆ private继承| |= > private|
|protected |＆ public继承 |=> protected|
|protected |＆ protected继承 |=> protected|
|protected |＆ private继承 |= > private|
|private |＆ public继承 |=> 子类无权访问|
|private |＆ protected继承 |=> 子类无权访问|
|private |＆ private继承 |= > 子类无权访问|


* How to access public, private, protected member?
* What is the difference between public and protected?
