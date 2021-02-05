#### Searching for Header Files and Libraries (-I, -L and -l)
When compiling the program, the  `compiler` needs the `header` files to compile the source codes (include-paths); 
The include-paths are specified via -Idir option (or environment variable `CPATH`). 
Since the header's filename is known (e.g., iostream.h, stdio.h), the compiler only needs the directories.
- $CPLUS_INCLUDE_PATH
- $C_INCLUDE_PATH

The `linker` needs the `libraries` to resolve `external references` from other object files or libraries ().
The linker searches the so-called `library-paths` for libraries needed to link the program into an executable. 
The library-path is specified via `-Ldir` option (uppercase 'L' followed by the directory path) (or environment variable `LIBRARY_PATH`). 
In addition, you also have to specify the library name. 
In Unixes, the library `libxxx.a` is specified via `-lxxx option` (lowercase letter 'l', without the prefix "lib" and ".a" extension). 
In Windows, provide the full name such as -lxxx.lib. 
The linker needs to know both the directories as well as the library names. Hence, two options need to be specified.
echo $LD_LIBRARY_PATH
If you use autotools, you can just configure with `LDFLAGS=-L/some/path/lib`


### How to check GCC environment variable:
GCC uses the following environment variables:

* **PATH**: For searching the executables and run-time shared libraries (.dll, .so).
* **CPATH**: For searching the include-paths for headers. It is searched after paths specified in -I<dir> options. C_INCLUDE_PATH and CPLUS_INCLUDE_PATH can be used to specify C and C++ headers if the particular language was indicated in pre-processing.
* **LIBRARY_PATH** : For searching library-paths for link libraries. It is searched after paths specified in -L<dir> options.
* Verbose Mode (-v)
* Defining Macro (-D)

* -"file"- Utility - Determine File Type

$ gcc -c hello.c
$ gcc -o hello.exe hello.o
 
$ file hello.c
hello.c: C source, ASCII text, with CRLF line terminators

$ file hello.o
hello.o: data
 
> file hello.exe
hello.exe: PE32 executable (console) x86-64, for MS Windows

* -"nm"- Utility - List Symbol Table of Object Files, nm命令存在于多数后出版本的Unix及类似的操作系统中。nm被用来检查二进制文件（包括库，编译后的目标模块，共享目标文件，和独立可执行文件）并显示这些文件的内容，或存储在其中的元信息，特别是符号表。"nm" is commonly-used to check if a particular function is defined in an object file. A 'T' in the second column indicates a function that is defined, while a 'U' indicates a function which is undefined and should be resolved by the linker.

Example: $ nm hello.o
0000000000000000 b .bss
0000000000000000 d .data
0000000000000000 p .pdata
0000000000000000 r .rdata
0000000000000000 r .rdata$zzz
0000000000000000 t .text
0000000000000000 r .xdata
                 U __main
0000000000000000 T main
                 U puts

* -"ldd"- Utility - List Dynamic-Link Libraries, The utility "ldd" examines an executable and displays a list of the shared libraries that it needs. For example,

> ldd hello.exe
ntdll.dll => /cygdrive/c/WINDOWS/SYSTEM32/ntdll.dll (0x7ff9ba3c0000)
KERNEL32.DLL => /cygdrive/c/WINDOWS/System32/KERNEL32.DLL (0x7ff9b9880000)
KERNELBASE.dll => /cygdrive/c/WINDOWS/System32/KERNELBASE.dll (0x7ff9b6a60000)
SYSFER.DLL => /cygdrive/c/WINDOWS/System32/SYSFER.DLL (0x6ec90000)
ADVAPI32.dll => /cygdrive/c/WINDOWS/System32/ADVAPI32.dll (0x7ff9b79a0000)
msvcrt.dll => /cygdrive/c/WINDOWS/System32/msvcrt.dll (0x7ff9b9100000)
sechost.dll => /cygdrive/c/WINDOWS/System32/sechost.dll (0x7ff9b9000000)
RPCRT4.dll => /cygdrive/c/WINDOWS/System32/RPCRT4.dll (0x7ff9b9700000)
cygwin1.dll => /usr/bin/cygwin1.dll (0x180040000)


# Try running the compilation in verbose mode (-v) to study the library-paths (-L) and libraries (-l) used in your system:

![GCC_CompilationProcess](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/images/GCC_CompilationProcess.png)

```diff
- soname 
```
In Unix and Unix-like operating systems, a soname is a field of data in a shared object file. The soname is a string, which is used as a "logical name" describing the functionality of the object.
How to get soname 
 - objdump -p libxxx.so | grep SONAME

`ldconfig` creates the necessary links and cache to the most recent shared libraries found in the directories specified on the command line, in the file /etc/ld. so. conf, and in the trusted directories (/lib and /usr/lib).
 ldconfig -n directory_with_shared_libraries

Takeaway
1. ldd
2. ln
3. -v 
4. -Idir 
5. -Ldir  -lxxx option
6. printenv
7. soname


| Cmd      |      usage       |    Example  |     Example   |
|----------|:----------------:|------------:|:-------------:|
| ln       | Symoblic link    |             |               |


The difference between hard links and soft (or symbolic) links comes down to what they reference.
Hard links point, or reference, to a specific space on the hard drive. You can have multiple files hard linked to the same place in the hard drive, but if you change the data on one of those files, the other files will also reflect that change.
Symbolic links work a bit differently. A symbolic link still points to a specific point on the hard drive, but if you create a second file, this second file does not point to the harddrive, but instead, to the first file.
