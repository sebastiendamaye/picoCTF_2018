# assembly-1
## Question
> What does `asm1(0x76)` return? Submit the flag as a hexadecimal value (starting with '`0x`'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](files/eq_asm_rev.S) located in the directory at `/problems/assembly-1_0_cfb59ef3b257335ee403035a6e42c2ed`.

## Hint
>assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

# Solution
Below is the commented code:
```asm
.intel_syntax noprefix
.bits 32
	
.global asm1

asm1:
	push	ebp                         ; function prologue
	mov	ebp,esp                     ; function prologue
	cmp	DWORD PTR [ebp+0x8],0x98    ; if arg (0x76) > 0x98
	jg 	part_a                      ;   then jump to part_a (won't jump)
	cmp	DWORD PTR [ebp+0x8],0x8     ; if arg (0x76) != 0x8
	jne	part_b                      ;   then jump to part_b (will jump)
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x16
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:                                     ; === part_b ===
	mov	eax,DWORD PTR [ebp+0x8]     ; EAX=arg (0x76)
	sub	eax,0x3                     ; EAX = 0x76-0x3 = 0x73
	jmp	part_d                      ; jump to part_d
	cmp	DWORD PTR [ebp+0x8],0xbc
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
part_d:                                     ; === part_d ===
	pop	ebp                         ; function epilogue
	ret                                 ; return EAX = 0x73
```

# Flag
`picoCTF{0x73}`
