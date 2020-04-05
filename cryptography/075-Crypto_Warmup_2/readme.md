# Crypto Warmup 2
## Question
>Cryptography doesn't have to be complicated, have you ever heard of something called rot13? `cvpbPGS{guvf_vf_pelcgb!}`

## Hint
>This can be solved online if you don't want to do it by hand!

# Solution
ROT13 is a specific case of Caesar cipher where the offset is equal to 13 (hence the ROT13 name). We can create such an alias to resolve the problem:
~~~~
$ alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
$ echo -n 'cvpbPGS{guvf_vf_pelcgb!}' | rot13
picoCTF{this_is_crypto!}
~~~~

# Flag
`picoCTF{this_is_crypto!}`
