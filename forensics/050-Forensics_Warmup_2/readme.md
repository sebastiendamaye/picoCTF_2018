# Forensics Warmup 2
## Question
>Hmm for some reason I can't open this [PNG](files/flag.png)? Any ideas? 

## Hint
>How do operating systems know what kind of file it is? (It's not just the ending!
>Make sure to submit the flag as picoCTF{XXXXX}

# Solution
A good practice is to check the output of the `file` command, instead of trying the extension. The file is not a PNG but a JPG file:

~~~~
$ file flag.png 
flag.png: JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 909x190, components 3
~~~~

Once the file renamed to flag.jpg, it reveals the flag:

![flag](files/flag.jpg "flag")

# Flag
`picoCTF{extensions_are_a_lie}`
