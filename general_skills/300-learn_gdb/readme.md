# learn gdb
## Question
>Using a debugging tool will be extremely useful on your missions. Can you run this [program](files/run) in gdb and find the flag? You can find the file in `/problems/learn-gdb_0_716957192e537ac769f0975c74b34194` on the shell server. 

## Hint
>Try setting breakpoints in gdb

>Try and find a point in the program after the flag has been read into memory to break on

>Where is the flag being written in memory?

# Solution
Let's run our executable in `gdb` and disassemble the `main` function. We can set a breakpoint just after the `decrypt_flag` function, and display the content (string) of the variable `flag_buf` as follows:
~~~~
$ gdb -q ./run 
Reading symbols from ./run...(no debugging symbols found)...done.
(gdb) set disassembly-flavor intel
(gdb) disas main
Dump of assembler code for function main:
   0x00000000004008c9 <+0>:	push   rbp
   0x00000000004008ca <+1>:	mov    rbp,rsp
   0x00000000004008cd <+4>:	sub    rsp,0x10
   0x00000000004008d1 <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x00000000004008d4 <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x00000000004008d8 <+15>:	mov    rax,QWORD PTR [rip+0x200af9]        # 0x6013d8 <stdout@@GLIBC_2.2.5>
   0x00000000004008df <+22>:	mov    ecx,0x0
   0x00000000004008e4 <+27>:	mov    edx,0x2
   0x00000000004008e9 <+32>:	mov    esi,0x0
   0x00000000004008ee <+37>:	mov    rdi,rax
   0x00000000004008f1 <+40>:	call   0x400650 <setvbuf@plt>
   0x00000000004008f6 <+45>:	mov    edi,0x4009d0
   0x00000000004008fb <+50>:	call   0x400600 <puts@plt>
   0x0000000000400900 <+55>:	mov    eax,0x0
   0x0000000000400905 <+60>:	call   0x400786 <decrypt_flag>
   0x000000000040090a <+65>:	mov    edi,0x400a08
   0x000000000040090f <+70>:	call   0x400600 <puts@plt>
   0x0000000000400914 <+75>:	mov    eax,0x0
   0x0000000000400919 <+80>:	leave  
   0x000000000040091a <+81>:	ret    
End of assembler dump.
(gdb) b *0x40090a
Breakpoint 1 at 0x40090a
(gdb) r
Starting program: /problems/learn-gdb_0_716957192e537ac769f0975c74b34194/run 
Decrypting the Flag into global variable 'flag_buf'
.....................................

Breakpoint 1, 0x000000000040090a in main ()
(gdb) p/s (char*) flag_buf
$1 = 0x1d64010 "picoCTF{gDb_iS_sUp3r_u53fuL_a6c61d82}"
(gdb) 
~~~~

# Flag
`picoCTF{gDb_iS_sUp3r_u53fuL_a6c61d82}`
