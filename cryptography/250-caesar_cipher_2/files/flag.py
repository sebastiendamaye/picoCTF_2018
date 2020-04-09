#!/usr/bin/env python
encrypted = '^WQ]1B4iQ/SaO@M1W>V3`AMXcABMO@3\BMa3QC`3k'
for offset in range(127):
    flag = ''.join([chr(ord(i)+offset) for i in encrypted])
    if 'pico' in flag:
        print("OFFSET: %s | FLAG: %s" % (offset, flag))

