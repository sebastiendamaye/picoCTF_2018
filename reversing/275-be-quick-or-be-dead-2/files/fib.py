#!/usr/bin/env python

def fib(n):
    i = 0
    nextterm = 1
    present = 1
    previous = 0

    while i < n:
        nextterm = present + previous
        present = previous
        previous = nextterm
        i = i + 1
    return nextterm

n = 1015
result = fib(n)
print(hex(result & (2 ** 64 - 1)))
