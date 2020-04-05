# Crypto Warmup 1
## Question
>Crpyto can often be done by hand, here's a message you got from a friend, `llkjmlmpadkkc` with the key of `thisisalilkey`. Can you use this [table](files/table.txt) to solve it?.

## Hint
>Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
>Please use all caps for the message.

# Solution
The table makes us think of the [Vigenere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). Let's use [this website](https://cryptii.com/pipes/vigenere-cipher) to decrypt the message. It reveals the string `secretmessage`. Because the hint said the message should use caps, the flag is `picoCTF{SECRETMESSAGE}`.

# Flag
`picoCTF{SECRETMESSAGE}`
