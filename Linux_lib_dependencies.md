#### Searching for Header Files and Libraries (-I, -L and -l)
When compiling the program, the  `compiler` needs the `header` files to compile the source codes (include-paths); 
The include-paths are specified via -Idir option (or environment variable CPATH). 
Since the header's filename is known (e.g., iostream.h, stdio.h), the compiler only needs the directories.

The `linker` needs the `libraries` to resolve `external references` from other object files or libraries ().
The linker searches the so-called library-paths for libraries needed to link the program into an executable. 
The library-path is specified via `-Ldir` option (uppercase 'L' followed by the directory path) (or environment variable LIBRARY_PATH). 
In addition, you also have to specify the library name. 
In Unixes, the library libxxx.a is specified via -lxxx option (lowercase letter 'l', without the prefix "lib" and ".a" extension). 
In Windows, provide the full name such as -lxxx.lib. 
The linker needs to know both the directories as well as the library names. Hence, two options need to be specified.

How to check environment variable:
`printenv`
GCC Environment Variables
GCC uses the following environment variables:

* PATH: For searching the executables and run-time shared libraries (.dll, .so).
* CPATH: For searching the include-paths for headers. It is searched after paths specified in -I<dir> options. C_INCLUDE_PATH and CPLUS_INCLUDE_PATH can be used to specify C and C++ headers if the particular language was indicated in pre-processing.
* LIBRARY_PATH: For searching library-paths for link libraries. It is searched after paths specified in -L<dir> options.

* "file" Utility - Determine File Type
* "nm" Utility - List Symbol Table of Object Files
* "ldd" Utility - List Dynamic-Link Libraries


# Try running the compilation in verbose mode (-v) to study the library-paths (-L) and libraries (-l) used in your system:



| Cmd      |      usage       |    Example  |     Example   |
|----------|:----------------:|------------:|:-------------:|
| ln       | Symoblic link  |  |

![GCC_CompilationProcess](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/images/GCC_CompilationProcess.png)
