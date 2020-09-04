How to understand:
# Shell Script's idiom: 2>&1

- 1>

`$ cat foo.txt 1> output.txt `# output stdout(1) to output.txt

- 2>

`$ cat nop.txt 2> error.txt `# output stderr(2) to error.txt

## stdout.
A file descriptor is nothing more that a positive integer that represents an open file. 
If you have 100 open files, you will have 100 file descriptors for them.
The only caveat is that, in Unix systems, *everything is a file*.
There are file descriptors for the Standard Output (stdout, 1) and Standard Error (stderr, 2).

You use `&1` to reference the value of the file descriptor 1 (stdout). 
So when you use `2>&1` you are basically saying 
“Redirect the stderr to the same place we are redirecting the stdout”.

& indicates that what follows is a file descriptor and not a filename. 
(& - get address of 1, similar to C grammar.) 

```shell
$cat foo.txt > output.txt 2>&1

$ cat nop.txt > output.txt 2>&1
```
https://www.brianstorti.com/understanding-shell-script-idiom-redirect/
