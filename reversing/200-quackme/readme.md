# quackme
## Question
> Can you deal with the Duck Web? Get us the flag from this [program](files/main). You can also find the program in `/problems/quackme_3_9a15a74731538ce2076cd6590cf9e6ca`.

## Hint
>Objdump or something similar is probably a good place to start.

# Solution
Let's run the program on the server:
~~~~
$ **./main** 
You have now entered the Duck Web, and you're in for a honkin' good time.
Can you figure out my trick?
**oops**
That's all folks.
~~~~

Now, let's analyze the [code](files/main.i64). The `main` function is just displaying things and calling `do_magic`.

Below is my commented code for the `do_magic` function
```asm
.text:08048642                 public do_magic
.text:08048642 do_magic        proc near               ; CODE XREF: main+35↓p
.text:08048642
.text:08048642 xored_val       = byte ptr -1Dh
.text:08048642 i               = dword ptr -1Ch
.text:08048642 j               = dword ptr -18h
.text:08048642 user_input      = dword ptr -14h
.text:08048642 len_user_input  = dword ptr -10h
.text:08048642 mem_user_input  = dword ptr -0Ch
.text:08048642
.text:08048642                 push    ebp
.text:08048643                 mov     ebp, esp
.text:08048645                 sub     esp, 28h
.text:08048648                 call    read_input
.text:0804864D                 mov     [ebp+user_input], eax
.text:08048650                 sub     esp, 0Ch
.text:08048653                 push    [ebp+user_input]
.text:08048656                 call    _strlen
.text:0804865B                 add     esp, 10h
.text:0804865E                 mov     [ebp+len_user_input], eax
.text:08048661                 mov     eax, [ebp+len_user_input]
.text:08048664                 add     eax, 1
.text:08048667                 sub     esp, 0Ch
.text:0804866A                 push    eax
.text:0804866B                 call    _malloc
.text:08048670                 add     esp, 10h
.text:08048673                 mov     [ebp+mem_user_input], eax
.text:08048676                 cmp     [ebp+mem_user_input], 0
.text:0804867A                 jnz     short loc_8048696
.text:0804867C                 sub     esp, 0Ch
.text:0804867F                 push    offset aMallocReturned ; "malloc() returned NULL. Out of Memory\n"
.text:08048684                 call    _puts
.text:08048689                 add     esp, 10h
.text:0804868C                 sub     esp, 0Ch
.text:0804868F                 push    0FFFFFFFFh
.text:08048691                 call    _exit
.text:08048696
.text:08048696 loc_8048696:                            ; CODE XREF: do_magic+38↑j
.text:08048696                 mov     eax, [ebp+len_user_input]
.text:08048699                 add     eax, 1
.text:0804869C                 sub     esp, 4
.text:0804869F                 push    eax
.text:080486A0                 push    0
.text:080486A2                 push    [ebp+mem_user_input]
.text:080486A5                 call    _memset
.text:080486AA                 add     esp, 10h
.text:080486AD                 mov     [ebp+i], 0
.text:080486B4                 mov     [ebp+j], 0
.text:080486BB                 jmp     short loop
.text:080486BD ; ---------------------------------------------------------------------------
.text:080486BD
.text:080486BD loc_80486BD:                            ; CODE XREF: do_magic+CF↓j
.text:080486BD                 mov     eax, [ebp+j]
.text:080486C0                 add     eax, 8048858h   ; sekrutBuffer = [0x29, 0x06, 0x16, 0x4f, 0x2b,
.text:080486C0                                         ; 0x35, 0x30, 0x1e, 0x51, 0x1b, 0x5b, 0x14,
.text:080486C0                                         ; 0x4b, 0x08, 0x5d, 0x2b, 0x52, 0x17, 0x01,
.text:080486C0                                         ; 0x57, 0x16, 0x11, 0x5c, 0x07, 0x5d, 0x00]
.text:080486C5                 movzx   ecx, byte ptr [eax]
.text:080486C8                 mov     edx, [ebp+j]
.text:080486CB                 mov     eax, [ebp+user_input]
.text:080486CE                 add     eax, edx
.text:080486D0                 movzx   eax, byte ptr [eax]
.text:080486D3                 xor     eax, ecx        ; user_input[j] ^ sekretBuffer[j]
.text:080486D5                 mov     [ebp+xored_val], al
.text:080486D8                 mov     edx, greetingMessage ; "You have now entered the Duck Web, and you're in for a honkin' good time."
.text:080486DE                 mov     eax, [ebp+j]
.text:080486E1                 add     eax, edx
.text:080486E3                 movzx   eax, byte ptr [eax]
.text:080486E6                 cmp     al, [ebp+xored_val]
.text:080486E9                 jnz     short loc_80486EF
.text:080486EB                 add     [ebp+i], 1      ; i += 1
.text:080486EF
.text:080486EF loc_80486EF:                            ; CODE XREF: do_magic+A7↑j
.text:080486EF                 cmp     [ebp+i], 25     ; iterates the sekrutBuffer chars and loops back
.text:080486F3                 jnz     short increment_j
.text:080486F5                 sub     esp, 0Ch
.text:080486F8                 push    offset aYouAreWinner ; "You are winner!"
.text:080486FD                 call    _puts
.text:08048702                 add     esp, 10h
.text:08048705                 jmp     short locret_8048713
.text:08048707 ; ---------------------------------------------------------------------------
.text:08048707
.text:08048707 increment_j:                            ; CODE XREF: do_magic+B1↑j
.text:08048707                 add     [ebp+j], 1      ; j += 1
.text:0804870B
.text:0804870B loop:                                   ; CODE XREF: do_magic+79↑j
.text:0804870B                 mov     eax, [ebp+j]
.text:0804870E                 cmp     eax, [ebp+len_user_input]
.text:08048711                 jl      short loc_80486BD
.text:08048713
.text:08048713 locret_8048713:                         ; CODE XREF: do_magic+C3↑j
.text:08048713                 leave
.text:08048714                 retn
.text:08048714 do_magic        endp
```

Long story short, there is a secret buffer at address `0x8048858` that is used to XOR the greeting message displayed when the program is launched. Let's write a [python script](files/crackme.py) to decrypt the message:

```python
#!/bin/env python
import pwn
greetingMessage = "You have now entered the Duck Web, and you're in for a honkin' good time."
sekrutBuffer = [0x29, 0x06, 0x16, 0x4f, 0x2b, 0x35, 0x30, 0x1e, 0x51, 0x1b, 0x5b, 0x14, 0x4b,
                0x08, 0x5d, 0x2b, 0x52, 0x17, 0x01, 0x57, 0x16, 0x11, 0x5c, 0x07, 0x5d, 0x00]
print(pwn.xor(greetingMessage, sekrutBuffer))
```

It looks like we have our flag:
~~~~
$ python crackme.py 
b"picoCTF{qu4ckm3_7ed36e4b}D\\e}o|PR2qz5pkq2^uedw\x7f\x7f|a2r\tg6'D[[w?<{s$g9\x0b&~l28"
~~~~

# Flag
`picoCTF{qu4ckm3_7ed36e4b}`
