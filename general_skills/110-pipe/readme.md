# pipe
## Question
>During your adventure, you will likely encounter a situation where you need to process data that you receive over the network rather than through a file. Can you find a way to save the output from this program and search for the flag? Connect with `2018shell.picoctf.com 2015`. 

## Hint
>Remember the flag format is picoCTF{XXXX}
>Ever heard of a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

# Solution
Connecting to `2018shell.picoctf.com` on port `2015` via `netcat` will output a lot of junk, where it will be difficult to find the flag:

~~~~
$ nc 2018shell.picoctf.com 2015
This is not a flag
I'm sorry you're going to have to look at another line
I'm sorry you're going to have to look at another line
I'm sorry you're going to have to look at another line
I'm sorry you're going to have to look at another line
I'm sorry you're going to have to look at another line
I'm sorry you're going to have to look at another line
I'm sorry you're going to have to look at another line
I'm sorry you're going to have to look at another line
I'm sorry you're going to have to look at another line
This is not a flag
I'm sorry you're going to have to look at another line
Unfortunately this is also not a flag
Unfortunately this is also not a flag
This is not a flag
This is not a flag
Unfortunately this is also not a flag
[SNIP]
~~~~

However, if we filter the content of this output, only the flag will be displayed:
~~~~
$ nc 2018shell.picoctf.com 2015 | grep pico
picoCTF{almost_like_mario_8861411c}
~~~~

# Flag
`picoCTF{almost_like_mario_8861411c}`

