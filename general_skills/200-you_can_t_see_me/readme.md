# you can't see me
## Question
> '...reading transmission... Y.O.U. .C.A.N.'.T. .S.E.E. .M.E. ...transmission ended...' Maybe something lies in `/problems/you-can-t-see-me_4_8bd1412e56df49a3c3757ebeb7ead77f`.

## Hint
>What command can see/read files?

>What's in the manual page of ls?

# Solution
Connect to the server and go to the directory in the question. You notice the presence of a hidden file
~~~~
$ cd /problems/you-can-t-see-me_4_8bd1412e56df49a3c3757ebeb7ead77f
$ ls
~~~~

The standard `ls` command does not show any file in this directory. Let's call it with `-a` to reveal hidden files.
~~~~
$ ls -la
total 60
drwxr-xr-x   2 root       root        4096 Mar 25  2019 .
-rw-rw-r--   1 hacksports hacksports    57 Mar 25  2019 .  
drwxr-x--x 556 root       root       53248 Mar 25  2019 ..
~~~~

It seems that there is a hidden file. Hidden file names are starting with a dot (`.`). However, we don't see it's name (probably because the name is just with spaces). Let's just the `-b` parameter to escape the special characters:
~~~~
$ ls -lab
total 60
drwxr-xr-x   2 root       root        4096 Mar 25  2019 .
-rw-rw-r--   1 hacksports hacksports    57 Mar 25  2019 .\ \ 
drwxr-x--x 556 root       root       53248 Mar 25  2019 ..
~~~~

We See that the escaped file name has 2 blackslashes (`\`) to escape 2 spaces. The file name is `[DOT][SPACE][SPACE]`. Let's use `cat` to show the content of the file.
~~~~
$ cat ".  "
picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_22f627d9}
$ cat .\ \ 
picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_22f627d9}
~~~~

# Flag
`picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_22f627d9}`
