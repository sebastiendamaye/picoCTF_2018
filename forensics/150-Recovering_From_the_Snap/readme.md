# Recovering From the Snap
## Question
>There used to be a bunch of [animals](files/animals.dd) here, what did Dr. Xernon do to them? 

## Hint
>Some files have been deleted from the disk image, but are they really gone?

# Solution
We are provided with a DOS/MBR image:
~~~~
$ file animals.dd 
animals.dd: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, root entries 512, sectors 20480 (volumes <=32 MB), Media descriptor 0xf8, sectors/FAT 20, sectors/track 32, heads 64, reserved 0x1, serial number 0x9b664dde, unlabeled, FAT (16 bit)
~~~~

That we can mount. There are 4 pictures of animals, but nothing really interesting for our problem.
~~~~
$ mkdir /data/tmp/
$ sudo mount animals.dd /data/tmp/
$ ls -l /data/tmp/
total 1700
-rwxr-xr-x 1 root root 632333 Jul 25  2018 dachshund.jpg
-rwxr-xr-x 1 root root 389187 Jul 25  2018 frog.jpg
-rwxr-xr-x 1 root root 321758 Jul 25  2018 music.jpg
-rwxr-xr-x 1 root root 393003 Jul 25  2018 rabbit.jpg
~~~~

From the title of this problem (the hint also helps), we can guess we have to deal with deleted content. Let's use `foremost`:
~~~~
$ foremost animals.dd 
Processing: animals.dd
|*|
$ ls -lR output/
output/:
total 8
-rw-r--r-- 1 unknown unknown 1050 Apr  6 13:12 audit.txt
drwxr-xr-- 2 unknown unknown 4096 Apr  6 13:12 jpg

output/jpg:
total 2940
-rw-r--r-- 1 unknown unknown 632333 Apr  6 13:12 00000077.jpg
-rw-r--r-- 1 unknown unknown 493564 Apr  6 13:12 00001313.jpg
-rw-r--r-- 1 unknown unknown 389187 Apr  6 13:12 00002277.jpg
-rw-r--r-- 1 unknown unknown 254837 Apr  6 13:12 00003041.jpg
-rw-r--r-- 1 unknown unknown 321758 Apr  6 13:12 00003541.jpg
-rw-r--r-- 1 unknown unknown 469105 Apr  6 13:12 00004173.jpg
-rw-r--r-- 1 unknown unknown 393003 Apr  6 13:12 00005093.jpg
-rw-r--r-- 1 unknown unknown  40384 Apr  6 13:12 00005861.jpg
~~~~

It turns out that one of the recovered pictures (`00005861.jpg`) reveals the flag:

![flag](files/flag.jpg "flag")

# Flag
`picoCTF{th3_5n4p_happ3n3d}`
