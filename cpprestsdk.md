

https://devblogs.microsoft.com/cppblog/connecting-to-facebook-with-the-c-rest-sdk/

Client:
1. use Singleton to avoid proliferate facebookclient instance.
2. use OAuth to perform user logins
3. uri_bulder 



cpprestsdk 

How to use json?

https://stackoverflow.com/questions/44597525/cpp-rest-sdk-json-how-to-create-json-w-array-and-write-to-file


#ifdef _EXPORTING
  #define DECLSPEC    __declspec(dllexport)
#else
   #define DECLSPEC    __declspec(dllimport)
#endif

#ifdef __cplusplus
   extern "C" {  
#endif

__cdecl specifies the calling convention, which specifies how parameters are passed to the function via the stack, and, very importantly, who cleans up the stack afterwards (in the case of __cdecl it is the caller who tidies up).
the __cdecl calling convention indicates that the function uses the traditional "C" language convention for passing parameters. There are other styles, notably __stdcall.

__declspec(dllimport/dllexport) is used to simplify exporting function definitions from a DLL: you don't need to use them, but the other ways of exporting functions are quite klunky.


