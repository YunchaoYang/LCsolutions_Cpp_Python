- What is the difference between executing a Bash script vs sourcing it?
   - Sourcing a script will run the commands in the current shell process.
   - Executing a script will run the commands in a new shell process.

 - What is fork?
   - fork is an operation whereby a process creates a copy of itself. 

 - What is Linux Kernal? 
   - Linux Kernal is considered as free and open-source software which is capable of managing hardware resources for the users. As it is released under General Public Licence (GPL), it becomes legal for anyone to edit it.

 -  What are the basic components of Linux?
   - Kernel: It is the core component of the Linux, it acts as an interface between software and hardware.  
   - Shell: It acts as an interface between the user and the Kernel.
   - GUI:  It stands for Graphic User Interface, which is another way for the user to interact with the system. But it is unlike images, buttons, text boxes for interaction.
   - System Utilities: These are the software functions that allow users to manage the computer.
   - Application Programs: Set of functions designed to perform a set of tasks.
   
- Enlist the basic components of LINUX

Answer: Linux operating system basically consists of 3 components. They are:

 - Kernel: This is considered as the core part and is responsible for all major activities of the Linux operating system. Linux Kernel is considered as free and open-source software that is capable of managing hardware resources for the users. It consists of various modules and interacts directly with the underlying hardware.
 - System Library: Most of the functionalities of the operating system are implemented by System Libraries. These act as a special function using which application programs accesses Kernel’s features.
 - System Utility: These programs are responsible for performing specialized, individual-level tasks.

- Enlist the features of the Linux operating system?

Answer: Following are some important features of the LINUX operating system:

- Linux Kernel and application programs can be installed on any kind of hardware platform and thus are considered portable.
   - It serves the purpose of multitasking by serving various functions simultaneously.
   - It provides security services in three ways namely, Authentication, Authorization, and Encryption.
   - It supports multiple users to access the same system resource but by using different terminals for operation.
   - Linux provides a hierarchical file system and its code is freely available to all.
   - It has its own application support (to download and install applications) and customized keyboards.
   - Linux distros provide live CD/USB to their users for installation.

# 6) Explain LILO?

Answer: LILO (Linux Loader) is the boot loader for the Linux operating system to load it into the main memory so that it can begin its operations. Bootloader here is a small program that manages a dual boot. LILO resides in MBR (Master Boot Record).

 - Its major advantage is that it allows the fast bootup of Linux when installing in the MBR.
 - Its limitation lies in the fact that it is not possible for all computers to tolerate modification of MBR.
 
 # 7) What is Swap space?

Answer: Swap space is the amount of physical memory that is allocated for use by Linux to hold some concurrent running programs temporarily. This condition usually occurs when RAM does not have enough memory to support all concurrent running programs. This memory management involves the swapping of memory to and from physical storage.

Q #10) Differentiate between BASH and DOS?

| BASH                       | DOS                      | 
| -------------------------- |:------------------------:| 
| case sensitive     | not case sensitive. | 
| ‘/’  as a directory separator.      | ‘\’ as a directory separator.      |  
| ‘\’ as an escape character. | ‘/’ character: serves as a command argument delimiter.   |   

- How can you determine the total memory used by LINUX?
   - `free` : This is the most simple command to check memory usage. For Example, `$ free –m`, the option `m` displays all the data in MBs.
   - `cat /proc/meminfo`: The next way to determine memory usage is to read /proc/meminfo file.
   - `vmstat`: This command basically lays out the memory usage statistics. For Example,  `$ vmstat –s`
   - `top` : This command determines the total memory usage as well as also monitors the RAM usage.
   - `htop`: This command also displays memory usage along with other details.

-  What are 3 kinds of file permissions, how to change them? 
   - Read: 
   - Write: 
   - Execute:
   
   - Use `chmod` 
      - `+` for adding permission
      - `-` for denying permission

-  What are the symbolic links? 
   - Ans: It will be redirected to another file using its path. Target files do not contain any data. Symbolic links redirect to another entry somewhere in the file system. If the target file is deleted, the link to that file is removed, but not the file.

- What are the hard links?
Ans: A hard link is another name for an existing file on Linux. We can create so many numbers of hard links, for any file. They can create links for other hard links.

- What is redirection?
Ans: Redirection can be defined as changing the standard input and output devices. To redirect metacharacters are used, you can redirect the file or program. 

- What is the maximum length for any file name under LINUX?
  - The maximum length for any file name under Linux is 255 characters.
  
- What are the environmental variables?
