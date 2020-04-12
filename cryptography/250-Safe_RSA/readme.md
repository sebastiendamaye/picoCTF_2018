# Safe RSA
## Question
>Now that you know about RSA can you help us decrypt this [ciphertext](files/ciphertext)? We don't have the decryption key but something about those values looks funky..

## Hint
>RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

>Hmmm that e value looks kinda small right?

>These are some really big numbers.. Make sure you're using functions that don't lose any precision!

# Solution
From [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)):
>*"When encrypting with low encryption exponents (e.g., `e` = 3) and small values of the `m`, (i.e., `m` < `n`<sup>1/`e`</sup>) the result of `m`<sup>`e`</sup> is strictly less than the modulus `n`. In this case, ciphertexts can be easily decrypted by taking the `e`th root of the ciphertext over the integers."*

Let's use the following python script:
```python
import gmpy2

n=374159235470172130988938196520880526947952521620932362050308663243595788308583992120881359365258949723819911758198013202644666489247987314025169670926273213367237020188587742716017314320191350666762541039238241984934473188656610615918474673963331992408750047451253205158436452814354564283003696666945950908549197175404580533132142111356931324330631843602412540295482841975783884766801266552337129105407869020730226041538750535628619717708838029286366761470986056335230171148734027536820544543251801093230809186222940806718221638845816521738601843083746103374974120575519418797642878012234163709518203946599836959811
e=3
cipher=2205316413931134031046440767620541984801091216351222789180573437837873413848819848972069088625959518346568495824756225842751786440791759449675594790690830246158935538568387091288002447511390259320746890980769089692036188995150522856413797

with gmpy2.local_context(gmpy2.context(), precision=300) as ctx:
	r = gmpy2.cbrt(cipher)
	i = (int(r))
	h = str(hex(i))
	a = str(h)[2:len(h)-1].decode('hex')
	print()
```

# Flag
`picoCTF{e_w4y_t00_sm411_7815e4a7}`
