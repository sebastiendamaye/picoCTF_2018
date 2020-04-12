# be-quick-or-be-dead-2
## Question
>As you enjoy this [music](https://www.youtube.com/watch?v=CTt1vk9nM9c) even more, another executable [be-quick-or-be-dead-2](files/be-quick-or-be-dead-2) shows up. Can you run this fast enough too? You can also find the executable in `/problems/be-quick-or-be-dead-2_0_04f4c579185361da6918bbc2fc9dcb7b`.

## Hint
>Can you call stuff without executing the entire program?

>What will the key finally be?

# Solution
## Running the program
When we run the program, we see the same logic as for the [be-quick-or-be-dead-1](https://github.com/sebastiendamaye/picoCTF_2018/tree/master/reversing/200-be-quick-or-be-dead-1) executable. We try to `NOP` the `set_timer` function:
~~~~
$ gdb -q ./be-quick-or-be-dead-2 
Reading symbols from ./be-quick-or-be-dead-2...
(No debugging symbols found in ./be-quick-or-be-dead-2)
gdb-peda$ b main
Breakpoint 1 at 0x400863
gdb-peda$ r
[SNIP]
Breakpoint 1, 0x0000000000400863 in main ()
gdb-peda$ disassemble 
Dump of assembler code for function main:
   0x000000000040085f <+0>:	push   rbp
   0x0000000000400860 <+1>:	mov    rbp,rsp
=> 0x0000000000400863 <+4>:	sub    rsp,0x10
   0x0000000000400867 <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x000000000040086a <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x000000000040086e <+15>:	mov    eax,0x0
   0x0000000000400873 <+20>:	call   0x400821 <header>
   0x0000000000400878 <+25>:	mov    eax,0x0
   0x000000000040087d <+30>:	call   0x40077a <set_timer>
   0x0000000000400882 <+35>:	mov    eax,0x0
   0x0000000000400887 <+40>:	call   0x4007ce <get_key>
   0x000000000040088c <+45>:	mov    eax,0x0
   0x0000000000400891 <+50>:	call   0x4007f9 <print_flag>
   0x0000000000400896 <+55>:	mov    eax,0x0
   0x000000000040089b <+60>:	leave  
   0x000000000040089c <+61>:	ret    
End of assembler dump.
gdb-peda$ set *(char*)0x40087d = 0x90
gdb-peda$ set *(char*)0x40087e = 0x90
gdb-peda$ set *(char*)0x40087f = 0x90
gdb-peda$ set *(char*)0x400880 = 0x90
gdb-peda$ set *(char*)0x400881 = 0x90
gdb-peda$ disassemble 
Dump of assembler code for function main:
   0x000000000040085f <+0>:	push   rbp
   0x0000000000400860 <+1>:	mov    rbp,rsp
=> 0x0000000000400863 <+4>:	sub    rsp,0x10
   0x0000000000400867 <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x000000000040086a <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x000000000040086e <+15>:	mov    eax,0x0
   0x0000000000400873 <+20>:	call   0x400821 <header>
   0x0000000000400878 <+25>:	mov    eax,0x0
   0x000000000040087d <+30>:	nop
   0x000000000040087e <+31>:	nop
   0x000000000040087f <+32>:	nop
   0x0000000000400880 <+33>:	nop
   0x0000000000400881 <+34>:	nop
   0x0000000000400882 <+35>:	mov    eax,0x0
   0x0000000000400887 <+40>:	call   0x4007ce <get_key>
   0x000000000040088c <+45>:	mov    eax,0x0
   0x0000000000400891 <+50>:	call   0x4007f9 <print_flag>
   0x0000000000400896 <+55>:	mov    eax,0x0
   0x000000000040089b <+60>:	leave  
   0x000000000040089c <+61>:	ret    
End of assembler dump.
gdb-peda$ c
Continuing.
Be Quick Or Be Dead 2
=====================

Calculating key...
~~~~

But the program computes the key and never stops...

Let's have a look at the code

## Code analysis
Below is an extract of the pseudo code:
```c
int get_key() {
    puts("Calculating key...");
    *(int32_t *)__TMC_END__ = calculate_key();
    rax = puts("Done calculating key");
    return rax;
}
void calculate_key() {
    fib(0x3f7);
    return;
}
int fib(int arg0) {
    var_24 = arg0; // 0x3f7
    if (var_24 <= 0x1) {
            var_14 = var_24;
    }
    else {
            var_14 = fib(var_24 - 0x2) + fib(var_24 - 0x1);
    }
    rax = var_14;
    return rax;
}
```
We see that the `calculate_key` function is calling the `fib` function with an argument (`0x3f7` in hex, equal to `1015` in decimal). This is a Fibonacci sequence computed recursively.

Let's use the [following python script](files/fib.py) to compute the result iteratively:
~~~
$ python files/fib.py 
0xf51f7eb6d73ec32d
~~~

Now, back to the assembly, let's see where this key is stored:
```asm
.text:00000000004007CE                 public get_key
.text:00000000004007CE get_key         proc near               ; CODE XREF: main+28↓p
.text:00000000004007CE                 push    rbp
.text:00000000004007CF                 mov     rbp, rsp
.text:00000000004007D2                 mov     edi, offset aCalculatingKey ; "Calculating key..."
.text:00000000004007D7                 call    _puts
.text:00000000004007DC                 mov     eax, 0
.text:00000000004007E1                 call    calculate_key
.text:00000000004007E6                 mov     cs:key, eax     ; key located at 0x6010c0
.text:00000000004007EC                 mov     edi, offset aDoneCalculatin ; "Done calculating key"
.text:00000000004007F1                 call    _puts
.text:00000000004007F6                 nop
.text:00000000004007F7                 pop     rbp
.text:00000000004007F8                 retn
.text:00000000004007F8 get_key         endp
```

The function `get_key` calls the function `calculate_key` at `0x4007E1` which computes the key and stores it in `0x6010c0` (`key`).

Now that we know that, we'll skip both the calls to `set_timer` and `get_key` and we will manually set `key` before calling `print_flag`.

```asm
.text:000000000040085F main            proc near               ; we'll break at main
.text:000000000040085F
.text:000000000040085F var_10          = qword ptr -10h
.text:000000000040085F var_4           = dword ptr -4
.text:000000000040085F
.text:000000000040085F                 push    rbp
.text:0000000000400860                 mov     rbp, rsp
.text:0000000000400863                 sub     rsp, 10h
.text:0000000000400867                 mov     [rbp+var_4], edi
.text:000000000040086A                 mov     [rbp+var_10], rsi
.text:000000000040086E                 mov     eax, 0
.text:0000000000400873                 call    header
.text:0000000000400878                 mov     eax, 0
.text:000000000040087D                 call    set_timer    ; we'll NOP that call
.text:0000000000400882                 mov     eax, 0
.text:0000000000400887                 call    get_key      ; we'll NOP that call
.text:000000000040088C                 mov     eax, 0
.text:0000000000400891                 call    print_flag   ; we'll break here and set the key
.text:0000000000400896                 mov     eax, 0
.text:000000000040089B                 leave
.text:000000000040089C                 retn
.text:000000000040089C main            endp
```

## Running in GDB
Let's fire GDB. Break at main and run:
~~~~
(gdb) b main
(gdb) r
~~~~

We'll NOP the call to `set_timer` to skipp the call:
~~~~
(gdb) set *(char*)0x40087D = 0x90
(gdb) set *(char*)0x40087E = 0x90
(gdb) set *(char*)0x40087F = 0x90
(gdb) set *(char*)0x400880 = 0x90
(gdb) set *(char*)0x400881 = 0x90
~~~~

We'll also NOP the call to `calculate_key` to skip the call:
~~~~
(gdb) set *(char*)0x400887 = 0x90
(gdb) set *(char*)0x400888 = 0x90
(gdb) set *(char*)0x400889 = 0x90
(gdb) set *(char*)0x40088A = 0x90
(gdb) set *(char*)0x40088B = 0x90
~~~~

No, break at `print_flag` and set the key:
~~~~
(gdb) b print_flag
(gdb) c
(gdb) set {int}0x6010c0 = 0xd73ec32d
(gdb) set {int}0x6010c4 = 0xf51f7eb6
~~~~

Check that the key was set and continue:
~~~~
(gdb) x 0x6010c0
 0x6010c0 <key>: 0xf51f7eb6d73ec32d
(gdb) c
Continuing.
Printing flag:
picoCTF{the_fibonacci_sequence_can_be_done_fast_73e2451e}
~~~~

# Flag
`picoCTF{the_fibonacci_sequence_can_be_done_fast_73e2451e}`
