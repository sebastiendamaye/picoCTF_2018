# grep 2
## Question
>This one is a little bit harder. Can you find the flag in `/problems/grep-2_2_413a577106278d0711d28a98f4f6ac28/files` on the shell server? Remember, grep is your friend. 

## Hint
>grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

# Solution
The directory on the server shows a list of directories with many files in each:
~~~~
sdam@pico-2018-shell:/problems/grep-2_2_413a577106278d0711d28a98f4f6ac28/files$ ll
total 48
drwxr-xr-x 12 root root 4096 Mar 25  2019 ./
drwxr-xr-x  3 root root 4096 Mar 25  2019 ../
drwxr-xr-x  2 root root 4096 Mar 25  2019 files0/
drwxr-xr-x  2 root root 4096 Mar 25  2019 files1/
drwxr-xr-x  2 root root 4096 Mar 25  2019 files2/
drwxr-xr-x  2 root root 4096 Mar 25  2019 files3/
drwxr-xr-x  2 root root 4096 Mar 25  2019 files4/
drwxr-xr-x  2 root root 4096 Mar 25  2019 files5/
drwxr-xr-x  2 root root 4096 Mar 25  2019 files6/
drwxr-xr-x  2 root root 4096 Mar 25  2019 files7/
drwxr-xr-x  2 root root 4096 Mar 25  2019 files8/
drwxr-xr-x  2 root root 4096 Mar 25  2019 files9/
sdam@pico-2018-shell:/problems/grep-2_2_413a577106278d0711d28a98f4f6ac28/files$ ls -R
.:
files0  files1  files2  files3  files4  files5  files6  files7  files8  files9

./files0:
file0   file11  file14  file17  file2   file22  file25  file28  file4  file7
file1   file12  file15  file18  file20  file23  file26  file29  file5  file8
file10  file13  file16  file19  file21  file24  file27  file3   file6  file9

./files1:
file0   file11  file14  file17  file2   file22  file25  file28  file4  file7
file1   file12  file15  file18  file20  file23  file26  file29  file5  file8
file10  file13  file16  file19  file21  file24  file27  file3   file6  file9

./files2:
file0   file11  file14  file17  file2   file22  file25  file28  file4  file7
file1   file12  file15  file18  file20  file23  file26  file29  file5  file8
file10  file13  file16  file19  file21  file24  file27  file3   file6  file9

./files3:
file0   file11  file14  file17  file2   file22  file25  file28  file4  file7
file1   file12  file15  file18  file20  file23  file26  file29  file5  file8
file10  file13  file16  file19  file21  file24  file27  file3   file6  file9

./files4:
file0   file11  file14  file17  file2   file22  file25  file28  file4  file7
file1   file12  file15  file18  file20  file23  file26  file29  file5  file8
file10  file13  file16  file19  file21  file24  file27  file3   file6  file9

./files5:
file0   file11  file14  file17  file2   file22  file25  file28  file4  file7
file1   file12  file15  file18  file20  file23  file26  file29  file5  file8
file10  file13  file16  file19  file21  file24  file27  file3   file6  file9

./files6:
file0   file11  file14  file17  file2   file22  file25  file28  file4  file7
file1   file12  file15  file18  file20  file23  file26  file29  file5  file8
file10  file13  file16  file19  file21  file24  file27  file3   file6  file9

./files7:
file0   file11  file14  file17  file2   file22  file25  file28  file4  file7
file1   file12  file15  file18  file20  file23  file26  file29  file5  file8
file10  file13  file16  file19  file21  file24  file27  file3   file6  file9

./files8:
file0   file11  file14  file17  file2   file22  file25  file28  file4  file7
file1   file12  file15  file18  file20  file23  file26  file29  file5  file8
file10  file13  file16  file19  file21  file24  file27  file3   file6  file9

./files9:
file0   file11  file14  file17  file2   file22  file25  file28  file4  file7
file1   file12  file15  file18  file20  file23  file26  file29  file5  file8
file10  file13  file16  file19  file21  file24  file27  file3   file6  file9
~~~~

Using a recursive search will save us a lot of time to find the flag:
~~~~
sdam@pico-2018-shell:/problems/grep-2_2_413a577106278d0711d28a98f4f6ac28/files$ grep -R pico *
files5/file24:picoCTF{grep_r_and_you_will_find_8eb84049}
~~~~

# Flag
`picoCTF{grep_r_and_you_will_find_8eb84049}`
