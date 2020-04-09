# caesar cipher 2
## Question
> Can you help us decrypt this [message](files/ciphertext)? We believe it is a form of a caesar cipher. You can find the ciphertext in `/problems/caesar-cipher-2_0_372a62ea0204b948793a2b1b3aeacaaa` on the shell server.

## Hint
>You'll have figure out the correct alphabet that was used to encrypt the ciphertext from the ascii character set
[ASCII Table](https://www.asciitable.com/)

# Solution
Because we know the message is encrypted using the Caesar cipher (title, question) with an extended ASCII table (hint), and the decrypted message will very likely contain the string `pico`, we can easily brute force it with the following [python script](files/flag.py):

```python
#!/usr/bin/env python
encrypted = '^WQ]1B4iQ/SaO@M1W>V3`AMXcABMO@3\BMa3QC`3k'
for offset in range(127):
    flag = ''.join([chr(ord(i)+offset) for i in encrypted])
    if 'pico' in flag:
        print("OFFSET: %s | FLAG: %s" % (offset, flag))
```

Let's run the program:
~~~~
$ python flag.py 
OFFSET: 18 | FLAG: picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}
~~~~

# Flag
`picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}`
