# assembly-2
## Question
> What does `asm2(0x6,0x28)` return? Submit the flag as a hexadecimal value (starting with '`0x`'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](files/loop_asm_rev.S) located in the directory at `/problems/assembly-2_0_24775b87ffbbe8e643da10e71018f275`.

## Hint
>assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

# Solution
Below is the commented code:
```asm
.intel_syntax noprefix
.bits 32
	
.global asm2

asm2:
	push   	ebp                         ; function prologue
	mov    	ebp,esp                     ; function prologue
	sub    	esp,0x10
	mov    	eax,DWORD PTR [ebp+0xc]     ; EAX = 2nd arg (0x28)
	mov 	DWORD PTR [ebp-0x4],eax     ; var_4 = EAX = 0x28
	mov    	eax,DWORD PTR [ebp+0x8]     ; EAX = 1st arg (0x6)
	mov	    DWORD PTR [ebp-0x8],eax     ; var_8 = EAX = 0x6
	jmp    	part_b                      ; goto part_b
part_a:	                                ; === part_a === (loop)
	add    	DWORD PTR [ebp-0x4],0x1     ; var_4 += 0x1
	add	    DWORD PTR [ebp+0x8],0x8f    ; var_8 += 0x8f
part_b:	                                ; === part_b ===
	cmp    	DWORD PTR [ebp+0x8],0x8f90  ; if var_8 <= 0x8f90
	jle    	part_a                      ;   then jump to part_a
	mov    	eax,DWORD PTR [ebp-0x4]     ; EAX = var_4 (loop exit)
	mov	esp,ebp                         ; function epilogue
	pop	ebp                             ; function epilogue
	ret                                 ; Function will return the value of
	                                    ;   var_4 at the end of the loop
```

`part_b` is actually a loop that will execute part_a until `var_8` <= `0x8f90`.

In python this can be written as follows (it will return `0x129`):
```python
var_4 = 0x28
var_8 = 0x6
while var_8 <= 0x8f90:
    var_4 += 0x1
    var_8 += 0x8f

print(hex(var_4))
```

# Flag
`picoCTF{0x129}`
