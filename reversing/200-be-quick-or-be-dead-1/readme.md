# be-quick-or-be-dead-1
## Question
>You find [this](https://www.youtube.com/watch?v=CTt1vk9nM9c) when searching for some music, which leads you to [be-quick-or-be-dead-1](files/be-quick-or-be-dead-1). Can you run it fast enough? You can also find the executable in `/problems/be-quick-or-be-dead-1_0_0ba9c6f09fe8b3168d2743ddc4919008`.

## Hint
>What will the key finally be?

# Solution
The file is a 64 bit executable for Linux:
~~~~
$ file be-quick-or-be-dead-1
be-quick-or-be-dead-1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=198c015dd440452423f27326654b7fece307b24e, not stripped
~~~~

When executed, here is what happens:
~~~~
$ ./be-quick-or-be-dead-1 
Be Quick Or Be Dead 1
=====================

Calculating key...
You need a faster machine. Bye bye.
~~~~

OK, let's open the executable in your favorite disassembler (IDA Pro, Hopper, ...) to see chat the `main` function looks like:

```asm

.text:0000000000400827 ; int __cdecl main(int argc, const char **argv, const char **envp)
.text:0000000000400827                 public main
.text:0000000000400827 main            proc near               ; DATA XREF: _start+1D↑o
.text:0000000000400827
.text:0000000000400827 var_10          = qword ptr -10h
.text:0000000000400827 var_4           = dword ptr -4
.text:0000000000400827
.text:0000000000400827                 push    rbp
.text:0000000000400828                 mov     rbp, rsp
.text:000000000040082B                 sub     rsp, 10h
.text:000000000040082F                 mov     [rbp+var_4], edi
.text:0000000000400832                 mov     [rbp+var_10], rsi
.text:0000000000400836                 mov     eax, 0
.text:000000000040083B                 call    header             ; call header function
.text:0000000000400840                 mov     eax, 0
.text:0000000000400845                 call    set_timer          ; call set_timer function
.text:000000000040084A                 mov     eax, 0
.text:000000000040084F                 call    get_key            ; call get_key function
.text:0000000000400854                 mov     eax, 0
.text:0000000000400859                 call    print_flag         ; call print_flag function
.text:000000000040085E                 mov     eax, 0
.text:0000000000400863                 leave
.text:0000000000400864                 retn
.text:0000000000400864 main            endp
```

The `main` function calls 4 functions, one of which being `set_timer`. This function exits the program after 1 second, which does not leave enough time for the machine to compute the key:
```asm
.text:0000000000400742                 public set_timer
.text:0000000000400742 set_timer       proc near               ; CODE XREF: main+1E↓p
.text:0000000000400742
.text:0000000000400742 seconds         = dword ptr -0Ch
.text:0000000000400742 var_8           = qword ptr -8
.text:0000000000400742
.text:0000000000400742                 push    rbp
.text:0000000000400743                 mov     rbp, rsp
.text:0000000000400746                 sub     rsp, 10h
.text:000000000040074A                 mov     [rbp+seconds], 1                  ; set to 1 second only!!!
.text:0000000000400751                 mov     esi, offset alarm_handler         ; handler. displays "You need a faster machine. Bye bye."
.text:0000000000400756                 mov     edi, 0Eh        ; sig
.text:000000000040075B                 call    ___sysv_signal
.text:0000000000400760                 mov     [rbp+var_8], rax
.text:0000000000400764                 cmp     [rbp+var_8], 0FFFFFFFFFFFFFFFFh
.text:0000000000400769                 jnz     short loc_400789
.text:000000000040076B                 mov     esi, 3Bh
.text:0000000000400770                 mov     edi, offset format ; "\n\nSomething went terribly wrong. \nPl"...
.text:0000000000400775                 mov     eax, 0
.text:000000000040077A                 call    _printf
.text:000000000040077F                 mov     edi, 0          ; status
.text:0000000000400784                 call    _exit
.text:0000000000400789 ; ---------------------------------------------------------------------------
.text:0000000000400789
.text:0000000000400789 loc_400789:                             ; CODE XREF: set_timer+27↑j
.text:0000000000400789                 mov     eax, [rbp+seconds]
.text:000000000040078C                 mov     edi, eax        ; seconds
.text:000000000040078E                 call    _alarm
.text:0000000000400793                 nop
.text:0000000000400794                 leave
.text:0000000000400795                 retn
.text:0000000000400795 set_timer       endp
```

Let's run the program in `gdb` and we will patch the program with `NOP` instructions (`0x90`) to erase the call to the `set_timer` function:
~~~~
$ gdb ./be-quick-or-be-dead-1 
(gdb) set disassembly-flavor intel
(gdb) b main
Breakpoint 1 at 0x40082b
(gdb) r
Starting program: /data/documents/challenges/picoCTF_2018/reversing/200-be-quick-or-be-dead-1/files/be-quick-or-be-dead-1 

Breakpoint 1, 0x000000000040082b in main ()
(gdb) disassemble 
Dump of assembler code for function main:
   0x0000000000400827 <+0>:	push   rbp
   0x0000000000400828 <+1>:	mov    rbp,rsp
=> 0x000000000040082b <+4>:	sub    rsp,0x10
   0x000000000040082f <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x0000000000400832 <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000400836 <+15>:	mov    eax,0x0
   0x000000000040083b <+20>:	call   0x4007e9 <header>
   0x0000000000400840 <+25>:	mov    eax,0x0
   0x0000000000400845 <+30>:	call   0x400742 <set_timer>
   0x000000000040084a <+35>:	mov    eax,0x0
   0x000000000040084f <+40>:	call   0x400796 <get_key>
   0x0000000000400854 <+45>:	mov    eax,0x0
   0x0000000000400859 <+50>:	call   0x4007c1 <print_flag>
   0x000000000040085e <+55>:	mov    eax,0x0
   0x0000000000400863 <+60>:	leave  
   0x0000000000400864 <+61>:	ret    
End of assembler dump.
(gdb) set *(char*)0x400845 = 0x90
(gdb) set *(char*)0x400846 = 0x90
(gdb) set *(char*)0x400847 = 0x90
(gdb) set *(char*)0x400848 = 0x90
(gdb) set *(char*)0x400849 = 0x90
(gdb) disassemble 
Dump of assembler code for function main:
   0x0000000000400827 <+0>:	push   rbp
   0x0000000000400828 <+1>:	mov    rbp,rsp
=> 0x000000000040082b <+4>:	sub    rsp,0x10
   0x000000000040082f <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x0000000000400832 <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000400836 <+15>:	mov    eax,0x0
   0x000000000040083b <+20>:	call   0x4007e9 <header>
   0x0000000000400840 <+25>:	mov    eax,0x0
   0x0000000000400845 <+30>:	nop
   0x0000000000400846 <+31>:	nop
   0x0000000000400847 <+32>:	nop
   0x0000000000400848 <+33>:	nop
   0x0000000000400849 <+34>:	nop
   0x000000000040084a <+35>:	mov    eax,0x0
   0x000000000040084f <+40>:	call   0x400796 <get_key>
   0x0000000000400854 <+45>:	mov    eax,0x0
   0x0000000000400859 <+50>:	call   0x4007c1 <print_flag>
   0x000000000040085e <+55>:	mov    eax,0x0
   0x0000000000400863 <+60>:	leave  
   0x0000000000400864 <+61>:	ret    
End of assembler dump.
(gdb) c
Continuing.
Be Quick Or Be Dead 1
=====================

Calculating key...
Done calculating key
Printing flag:
picoCTF{why_bother_doing_unnecessary_computation_29ff5e84}
[Inferior 1 (process 11770) exited normally]
(gdb) q
~~~~

# Flag
`picoCTF{why_bother_doing_unnecessary_computation_29ff5e84}`
