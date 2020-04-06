# strings
## Question
>Can you find the flag in this [file](files/strings) without actually running it? You can also find the file in `/problems/strings_1_c7bac958dd6a4b695dc72446d8014f59` on the shell server. 

## Hint
>[strings](https://linux.die.net/man/1/strings)

# Solution
~~~~
$ strings strings | grep pico
picoCTF{sTrIngS_sAVeS_Time_d7c8de6c}
~~~~

# Flag
`picoCTF{sTrIngS_sAVeS_Time_d7c8de6c}`

