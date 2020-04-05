# General Warmup 1
## Question
>If I told you your grade was 0x41 in hexadecimal, what would it be in ASCII? 

## Hint
>Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

# Solution
~~~~
$ echo picoCTF{$(python -c "print(chr(0x41))")}
picoCTF{A}
~~~~

# Flag
`picoCTF{A}`
