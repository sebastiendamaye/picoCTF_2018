# absolutely relative
## Question
>In a filesystem, everything is relative ¯\_(ツ)_/¯. Can you find a way to get a flag from this [program](files/absolutely-relative)? You can find it in `/problems/absolutely-relative_2_69862edfe341b57b6ed2c62c7107daee` on the shell server. [Source](files/absolutely-relative.c).

## Hint
>Do you have to run the program in the same directory? (⊙.☉)7

>Ever used a text editor? Check out the program 'nano'

# Solution
Below is the source code:

```c
#include <stdio.h>
#include <string.h>

#define yes_len 3
const char *yes = "yes";

int main()
{
    char flag[99];
    char permission[10];
    int i;
    FILE * file;


    file = fopen("/problems/absolutely-relative_2_69862edfe341b57b6ed2c62c7107daee/flag.txt" , "r");
    if (file) {
    	while (fscanf(file, "%s", flag)!=EOF)
    	fclose(file);
    }   
	
    file = fopen( "./permission.txt" , "r");
    if (file) {
    	for (i = 0; i < 5; i++){
            fscanf(file, "%s", permission);
        }
        permission[5] = '\0';
        fclose(file);
    }
    
    if (!strncmp(permission, yes, yes_len)) {
        printf("You have the write permissions.\n%s\n", flag);
    } else {
        printf("You do not have sufficient permissions to view the flag.\n");
    }
    
    return 0;
}
```

Notice the test to check the existence of a file `permission.txt` that contains the string `yes`. If this file doesn't exist, the program will exit with a message saying that you have insufficient permissions.

Now, let's connect to the server and check if this file exists. Unfortunately, it does not, and we do not have write permissions on this folder.

~~~~
$ ll /problems/absolutely-relative_2_69862edfe341b57b6ed2c62c7107daee/
total 76
drwxr-xr-x   2 root       root                   4096 Mar 25  2019 ./
drwxr-x--x 556 root       root                  53248 Mar 25  2019 ../
-rwxr-sr-x   1 hacksports absolutely-relative_2  8984 Mar 25  2019 absolutely-relative*
-rw-rw-r--   1 hacksports hacksports              796 Mar 25  2019 absolutely-relative.c
-r--r-----   1 hacksports absolutely-relative_2    37 Mar 25  2019 flag.txt
~~~~

That said, back to the source code, you will notice that the file is not checked with an absolute path, which means that we should be able to create it within our `home`, and start the program from there:
~~~~
$ cd
$ echo "yes" > permission.txt
$ /problems/absolutely-relative_2_69862edfe341b57b6ed2c62c7107daee/absolutely-relative
You have the write permissions.
picoCTF{3v3r1ng_1$_r3l3t1v3_372b3859}
~~~~

# Flag
`picoCTF{3v3r1ng_1$_r3l3t1v3_372b3859}`
