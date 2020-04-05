# TITLE_GOES_HERE
## Question
>Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with `nc 2018shell.picoctf.com 42165`. Files can be found here: [passwd](files/passwd) [shadow](files/shadow). 

## Hint
>If at first you don't succeed, try, try again. And again. And again.
>If you're not careful these kind of problems can really "rockyou".

# Solution
We are provided with 2 files that are related to the `root` account:
~~~~
$ cat passwd 
root:x:0:0:root:/root:/bin/bash
$ cat shadow 
root:$6$IGI9prWh$ZHToiAnzeD1Swp.zQzJ/Gv.iViy39EmjVsg3nsZlfejvrAjhmp5jY.1N6aRbjFJVQX8hHmTh7Oly3NzogaH8c1:17770:0:99999:7:::
~~~~
Let's use [John the Ripper](https://www.aldeid.com/wiki/John-The-Ripper) to crack the password:
~~~~
$ /sbin/john shadow 
Created directory: /home/unknown/.john
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Press 'q' or Ctrl-C to abort, almost any other key for status
**password1**        (root)
1g 0:00:00:06 100% 2/3 0.1474g/s 443.2p/s 443.2c/s 443.2C/s 123456..pepper
Use the "--show" option to display all of the cracked passwords reliably
Session completed
~~~~
The `root` password was found easily: `password1`

Now, let's connect with the credentials we have:
~~~~
$ nc 2018shell.picoctf.com 42165
Username: root
Password: password1
picoCTF{J0hn_1$_R1pp3d_5f9a67aa}
~~~~
# Flag
`picoCTF{J0hn_1$_R1pp3d_5f9a67aa}`
