# assembly-0
## Question
>What does `asm0(0xc9,0xb0)` return? Submit the flag as a hexadecimal value (starting with '`0x`'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](files/intro_asm_rev.S) located in the directory at `/problems/assembly-0_4_0f197369bfc00a9211504cf65ac31994`. 

## Hint
>basical assembly [tutorial](https://www.tutorialspoint.com/assembly_programming/assembly_basic_syntax.htm)
>assembly [registers](https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm)

# Solution
The commented code is as follows:
```asm
.intel_syntax noprefix
.bits 32
	
.global asm0

asm0:
	push	ebp                 ; function prologue
	mov	ebp,esp                 ; function prologue
	mov	eax,DWORD PTR [ebp+0x8] ; 1st argument (0xc9) moved to EAX
	mov	ebx,DWORD PTR [ebp+0xc] ; 2nd argument (0xb0) moved to EBX
	mov	eax,ebx                 ; EAX = EBX = 0xb0
	mov	esp,ebp                 ; function epilogue
	pop	ebp	                    ; function epilogue
	ret                         ; return EAX = 0xb0
```

The function will return the value of the second argument (`0xb0`).

# Flag
`picoCTF{0xb0}`
