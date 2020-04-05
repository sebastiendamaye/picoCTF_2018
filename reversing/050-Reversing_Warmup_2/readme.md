# Reversing Warmup 2
## Question
>Can you decode the following string `dGg0dF93NHNfczFtcEwz` from base64 format to ASCII? 

## Hint
>Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

# Solution
~~~~
$ echo picoCTF{$(echo -n "dGg0dF93NHNfczFtcEwz" | base64 -d)}
picoCTF{th4t_w4s_s1mpL3}
~~~~

# Flag
`picoCTF{th4t_w4s_s1mpL3}`
