# environ
## Question
> Sometimes you have to configure environment variables before executing a program. Can you find the flag we've hidden in an environment variable on the shell server?

## Hint
>unix [env](https://www.tutorialspoint.com/unix/unix-environment.htm)

# Solution
Connect to the server via SSH and issue the following command to list a filtered list of environment variables:
~~~~
$ printenv | grep pico
SECRET_FLAG=picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}
~~~~

# Flag
`picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}`
