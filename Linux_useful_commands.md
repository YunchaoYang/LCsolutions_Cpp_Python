- What are inode and process id?
  - Ans: inode is a unique name given to each file and process id is a unique name given to each process. 

- What are system calls used for process management in Linux?
   - `fork()`: Used to create a new process.
   - `exec()`: Execute new process.
   - `wait()`: wait until process execution.
   - `exit()`: exit from the process.
   - System calls to get the Process id :
      - `getpid()`: to find the unique process id. 
      - `getppid()`: to find the unique parent process id.   

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

- Process states in Linux?
   - New/ Ready: A new process is created and ready to run.
   - Running: The process is being executed.
   - Blocked/ Wait: The process is waiting for input from the user. 
   - Terminated/ Completed: The process completed the execution or terminated by the operating system. 
   - Zombie: The process is deleted, but still the information regarding the process exists in the process table.


- Explain LILO?

Answer: LILO (Linux Loader) is the boot loader for the Linux operating system to load it into the main memory so that it can begin its operations. Bootloader here is a small program that manages a dual boot. LILO resides in MBR (Master Boot Record).

 - Its major advantage is that it allows the fast bootup of Linux when installing in the MBR.
 - Its limitation lies in the fact that it is not possible for all computers to tolerate modification of MBR.
 
- What is Swap space?

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

-  What are 3 kinds of file permissions, how to change them? And explain file permission groups?
   -  file permissions
      - Read: 
      - Write: 
      - Execute:
   -  file permission groups
      -  Owner
      -  Group
      -  All Users
      
   - Use `chmod` 
      - `+` for adding permission
      - `-` for denying permission
      - 4 - read permission
      - 2 - write permission
      - 1- execute permission
      
-  What are the symbolic links? 
   - Ans: It will be redirected to another file using its path. Target files do not contain any data. Symbolic links redirect to another entry somewhere in the file system. If the target file is deleted, the link to that file is removed, but not the file.

- What are the hard links?
Ans: A hard link is another name for an existing file on Linux. We can create so many numbers of hard links, for any file. They can create links for other hard links.

- What is redirection?
Ans: Redirection can be defined as changing the standard input and output devices. To redirect metacharacters are used, you can redirect the file or program. 
   - Input Redirection: ‘<’ symbol is used for input redirection and is numbered as (0). Thus it is denoted as STDIN(0).
   - Output Redirection: ‘>’ symbol is used for output redirection and is numbered as (1). Thus it is denoted as STDOUT(1).
   - Error Redirection: It is denoted as STDERR(2).

- What is the maximum length for any file name under LINUX?
  - The maximum length for any file name under Linux is 255 characters.
  
- What are the environmental variables?
   - Environmental variables are global settings that control the shell's function as well as that of other Linux programs. Another common term for environmental variables is global shell variables.

   - `env` is a shell command is used to print a list of current environmental variables and it can run another process in another environment without any modification of the current environment


- What are Daemons?
  - Ans: A Daemons is a background process which accepts the requests for service from other computers, most of the operating systems use daemons in other forms.
  
- Enlist some Linux to file content commands?
   - cat
   - more
   - less
   - head
   - tail

- Explain command grouping in Linux?

   - Answer: Command grouping is basically done by the use of braces ‘()’ and parenthesis ‘{}’. Redirection is applied to the entire group when the command is grouped.
   - When commands are placed within the braces, then they are executed by the current shell. Example, (list)
   - When the commands are placed within the parenthesis, then they are executed by a subshell. Example, {list;}

33. What is umask?
Ans: unmask stands for user file creation mode. When the user creates any file, it has default file permissions. So unmask will specify few restrictions to the newly created file (it controls the file permissions).

1
umask [-S] [mask]<div class="open_grepper_editor" title="Edit & Save To Grepper"></div>
34.  How to set the mask permanently for a user? 
Ans: If the unmask command invoked without any arguments, it means it will display the current mask. 

To set the unmask permanently, we have two types.

They are:

Ocotal representation.
Symbolic representation.
35. What is network bonding in Linux?
Ans:  Network Bonding is a process of combining more than two network interfaces to form a single network interface. It offers performance improvement and redundancy by increasing network throughput and bandwidth. No need to worry if one interface is down or unplugged because the other will work. The behaviour of the bonded interface depends on the bonding method. 

36. What are the different modes of Network bonding in Linux?
Ans: 
Mode-0(balance-rr): It is a default mode and based on Round-Robin policy. It offers fault tolerance and load balancing features. It used round-robin fashion to transmit the packets.
Mode-1(active-backup): It is based on Active Backup policy and only one slave will act in the band and another one will act when the others fail in the band. It also provides fault tolerance.
Mode-2(balance-xor): It sets a xor mode between the source Mac address and destination Mac address to provide fault tolerance.
Mode-3(broadcast): It is based on broadcast policy and transmitted everything in the slave interface. It also provides fault tolerance and it can be used only for a particular purpose.
Mode-4(802.3ad): It is a dynamic aggregation mode, it created aggregation groups which is having the same speed. It uses transmit hashing method to select the slaves for outgoing traffic.
Mode-5(balance-tlb): The outgoing traffic is according to the current load on the slave, and the incoming traffic is received by the slave. It is called an adaptive transmit load balancing mode. 
Mode-6(balance-alb): It is an adaptive load balancing mode. It does not require any switch support. 
37. How to check the default route and routing table?
Ans:  To display the default route and routing table, we use the following commands.

1
2
3
4
5
$ route-n
 
$ nestat-rn
 
$ ip <div class="open_grepper_editor" title="Edit & Save To Grepper"></div>
38. How to check which ports are listening in my Linux Server?
Ans: We have two commands to check which ports are in listening in Linux Server. Following are the two commands 

1
2
# netstat --listen
# netstat -l<div class="open_grepper_editor" title="Edit & Save To Grepper"></div>
39. Where the kernel modules are located?
Ans: lib/modules/kernel-version/, this directory stores all the information about the compiled drives under the Linux system. Using lsmod command also we can see the installed kernel modules. 

40. How to change the default run level in Linux?
Ans: To change the default run level in Linux use init command. 

41. How to share a directory using nfs?
Ans:  To share a directory using NFS, first edit the configuration file and ‘/etc/exports’ and add an entry like directory name ‘/’. Now restart the NFS service.

42. What are the default ports used for SMTP, DNS, FTP, DHCP, SSH, and squid?


https://www.softwaretestinghelp.com/linux-interview-questions-answers/


https://mindmajix.com/linux-interview-questions#what-are-the-basic-components-of-linux
