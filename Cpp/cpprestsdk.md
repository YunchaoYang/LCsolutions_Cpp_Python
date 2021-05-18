
* 功能
  * URI构造/解析，
  * JSON编解码，
  * HTTP客户端、
  * HTTP服务端，
  * WebSocket客户端，
  * 流式传输，
  * oAuth验证

* Dependencies
  * Boost Asio
  * OpenSSL
  * CMake

https://devblogs.microsoft.com/cppblog/connecting-to-facebook-with-the-c-rest-sdk/

Client:
1. use Singleton to avoid proliferate facebookclient instance.
2. use OAuth to perform user logins
3. uri_bulder 

Parallelism is hard, concurrency is harder.
"Concurrent program wait faster."

### Concurrency in C++ today
* Threading Building Blocks (Intel TBB)
* Prallel Patterns Library Library (Microsoft PPL)
* CUDA
* OpenCL
* Clik
* AMP


### std::future in C++ 11.
``` cpp
// launch a task
future<int> work1 = async([]{return compute();};
// launch another task
future<int> work2 = async([]{return compute();};

//collect the results
cout << work1.get() + work2.get();
```
### Concurrency as Composition of Work
``` cpp
// collect the results
cout << work1.get() + work2.get(); // problem: blocking call get(), which hold a thread
// future.get() is used to retrieve the result of computation.

```
### PPL task<T>

``` cpp
// launch a task
task<int> work1 = create_task([]{return compute();};
// launch another task
task<int> work2 = create_task([]{return compute();};

//collect the results
cout << work1.get() + work2.get(); 
``` 
### continuation Chaining
``` cpp
// launch a task
task<int> work1 = create_task([]{return compute();};
// launch another task
task<int> work2 = create_task([]{return compute();};

//collect the results
cout << work1.get() + work2.get();
```

# cpprestsdk 
https://github.com/stgates/webservicescppcon2014

https://stackoverflow.com/questions/44597525/cpp-rest-sdk-json-how-to-create-json-w-array-and-write-to-file

需要注意的是，C++ REST SDK在Windows下，使用Windows系统自带的WinHTTP/HTTP Server API来实现HTTP协议通信，而在其它平台下是用Boost ASIO来实现HTTP协议通信，

### on linux: 
c++ -o restserver -std=c++11 restserver.cpp -lcpprest -lboost_system -lssl -lcrypto

1.用C++ REST SDK编写HTTP客户端，当服务端返回响应码301/302时，Windows下会用新地址自动重发请求，而Linux下则不会(运行C++ REST SDK自带的BingRequest示例即可看到这一差异)。
2.用C++ REST SDK编写HTTP服务端，需要在所有的网络接口上监听时，Windows下应使用地址"http://*:8080"，而Linux下应使用地址"http://0.0.0.0:8080"。

1.用C++ REST SDK编写HTTP客户端，当服务端返回响应码301/302时，Windows下会用新地址自动重发请求，而Linux下则不会(运行C++ REST SDK自带的BingRequest示例即可看到这一差异)。
2.用C++ REST SDK编写HTTP服务端，需要在所有的网络接口上监听时，Windows下应使用地址"http://*:8080"，而Linux下应使用地址"http://0.0.0.0:8080"。

另外，在Windows下用C++ REST SDK开发HTTP服务时，还有两个坑需要注意：
第一，由于HTTP Server API自身的一些特性，当C++ REST SDK服务程序在localhost之外的地址上监听时，默认需要以__管理员身份__运行程序，如果以普通用户身份运行上面的小程序，则发生异常：
Exception: Access denied: attempting to add Address 'http://*:8080/'. Run as administrator to listen on an hostname other than localhost, or to listen on port 80.
如果不希望每次都以管理员身份运行，可以用以下命令开放普通用户的权限：
netsh http add urlacl url=http://*:8080/ user=BUILTIN\Users listen=yes
该命令本身要以管理员身份运行，在Windows 8.1系统下，用Win+X组合键打开“命令提示符(管理员)”，输入命令即可

第二：由于HTTP Server API内部用到了一个内核模块http.sys，C++ REST SDK服务程序通过Windows防火墙的方式和普通TCP服务程序不太一样，直接用程序的可执行文件建立防火墙规则是无效的。正确的方式是新建一个入站规则，程序名称设为system，并设置本地端口为想要监听的端口号。


### Example 
简单的HTTP服务器程序，接收HTTP POST或GET请求，在控制台上打出请求的方法名，URI和查询参数，并返回"ACCEPTED"字符串。
``` cpp
#include <stdio.h>
#include <cpprest/uri.h>
#include <cpprest/http_listener.h>
#include <cpprest/asyncrt_utils.h>

#pragma comment(lib, "cpprest_2_7.lib")
#pragma comment(lib, "bcrypt.lib")
#pragma comment(lib, "crypt32.lib")
#pragma comment(lib, "winhttp.lib")
#pragma comment(lib, "httpapi.lib")

using namespace web;
using namespace http;
using namespace utility;
using namespace http::experimental::listener;

class CommandHandler
{
  public:
     CommandHandler() {}
     CommandHandler(utility::string_t url);
     pplx::task<void> open() { return m_listener.open(); }
     pplx::task<void> close() { return m_listener.close(); }
  private:
     void handle_get_or_post(http_request message);
     http_listener m_listener;
};

CommandHandler::CommandHandler(utility::string_t url) : m_listener(url)
{
 m_listener.support(methods::GET, std::bind(&CommandHandler::handle_get_or_post, this, std::placeholders::_1));
 m_listener.support(methods::POST, std::bind(&CommandHandler::handle_get_or_post, this, std::placeholders::_1));
}

void CommandHandler::handle_get_or_post(http_request message)
{
 ucout << "Method: " << message.method() << std::endl;
 ucout << "URI: " << http::uri::decode(message.relative_uri().path()) << std::endl;
 ucout << "Query: " << http::uri::decode(message.relative_uri().query()) << std::endl << std::endl;
 message.reply(status_codes::OK, "ACCEPTED");
};

int main(int argc, char argv[])
{
 try
 {
  utility::string_t address = U("http://*:8080");
  uri_builder uri(address);
  auto addr = uri.to_uri().to_string();
  CommandHandler handler(addr);
  handler.open().wait();
  ucout << utility::string_t(U("Listening for requests at: ")) << addr << std::endl;
  ucout << U("Press ENTER key to quit...") << std::endl;
  std::string line;
  std::getline(std::cin, line);
  handler.close().wait();
 }
 catch (std::exception& ex)
 {
  ucout << U("Exception: ") << ex.what() << std::endl;
  ucout << U("Press ENTER key to quit...") << std::endl;
  std::string line;
  std::getline(std::cin, line);
 }
 return 0;
}
```
https://blog.51cto.com/wdx04/1727907

``` cpp 
#include <http_client.h> 
#include<filestream.h> 
#include <uri.h> using namespace concurrency::streams; 
using namespace web::http::client; 
using namespace web::http; 

int main () 
{ 
  // Open stream to file. file_stream<unsigned char>::open_istream (L"myfile.txt") .then ([](basic_istream<unsigned char> fileStream) 
  { 
    // Make HTTP request with the file stream as the body. http_client client (L"http://www.myhttpserver.com"); 
    client.request (methods::PUT, L"myfile", fileStream) .then ([fileStream](http_response response) 
    { 
      fileStream.close (); 
      // Perform actions here to inspect the HTTP response... if(response.status_code () == status_codes::OK) 
      { 
      } 
    }); 
  }); 

  return 0; 
}
```

```cpp 

```
