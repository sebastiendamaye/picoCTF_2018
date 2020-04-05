# Reversing Warmup 1
## Question
>Throughout your journey you will have to run many programs. Can you navigate to /problems/reversing-warmup-1_0_f99f89de33522c93964bdec49fb2b838 on the shell server and run this [program](files/run) to retreive the flag? 

## Hint
>If you are searching online, it might be worth finding how to exeucte a program in command line.

# Solution
Running the `strings` command against the file reveals the flag:
~~~~
$ strings run | grep pico
picoCTF{welc0m3_t0_r3VeRs1nG}
~~~~

Here is the pseudo code of the `main` function:
~~~~
int main(int arg0) {
    setvbuf(*__TMC_END__, 0x0, 0x2, 0x0);
    puts("picoCTF{welc0m3_t0_r3VeRs1nG}");
    return 0x0;
}
~~~~

Without surprise, running the program on the web server reveals the flag that we have discovered with the static analysis.

~~~~
user@pico-2018-shell:/problems/reversing-warmup-1_0_f99f89de33522c93964bdec49fb2b838$ ./run 
picoCTF{welc0m3_t0_r3VeRs1nG}
~~~~

# Flag
`picoCTF{welc0m3_t0_r3VeRs1nG}`
