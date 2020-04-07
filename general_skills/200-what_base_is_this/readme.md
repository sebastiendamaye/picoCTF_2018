# what base is this?
## Question
>To be successful on your mission, you must be able read data represented in different ways, such as hexadecimal or binary. Can you get the flag from this program to prove you are ready? Connect with `nc 2018shell.picoctf.com 64706`.

## Hint
>I hear python is a good means (among many) to convert things.

>It might help to have multiple windows open

# Solution
~~~~
$ **nc 2018shell.picoctf.com 64706**
We are going to start at the very beginning and make sure you understand how data is stored.
cake
Please give me the 01100011 01100001 01101011 01100101 as a word.
To make things interesting, you have 30 seconds.
Input:
**cake**
Please give me the 626f74746c65 as a word.
Input:
**bottle**
Please give me the  143 157 165 143 150 as a word.
Input:
**couch**
You got it! You're super quick!
Flag: picoCTF{delusions_about_finding_values_5b21aa05}
~~~~

Here is a quick way to solve this challenge in python:
~~~~
$ **python**
>>> **a = "01100011 01100001 01101011 01100101"**
>>> **''.join([chr(int(i,2)) for i in a.split(' ')])**
'cake'
>>> **a = "626f74746c65"**
>>> **''.join([chr(eval('0x'+a[i:i+2])) for i in range(0,len(a), 2)])**
'bottle'
>>> **a = "143 157 165 143 150"**
>>> **''.join([chr(int(i,8)) for i in a.split(' ')])**
'couch'
~~~~

# Flag
`picoCTF{delusions_about_finding_values_5b21aa05}`
