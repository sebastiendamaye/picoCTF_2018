# TITLE_GOES_HERE
## Question
>Question goes here

## Hint
>Hint goes here

# Solution
My first attempt was to run the file command, but not really helpful.
~~~~
$ file ext-super-magic.img 
ext-super-magic.img: data
~~~~

The `strings` command did not help either. I ran `foremost` and was happy to get several `jpg` files where I could barely read `The flag is in another file`. After these unsuccessful attempts, I decided to check the hints and tried to run `fsck`:
~~~~
$ sudo fsck.ext2 ext-super-magic.img
e2fsck 1.45.6 (20-Mar-2020)
ext2fs_open2: Bad magic number in super-block
fsck.ext2: Superblock invalid, trying backup blocks...
fsck.ext2: Bad magic number in super-block while trying to open ext-super-magic.img

The superblock could not be read or does not describe a valid ext2/ext3/ext4
filesystem.  If the device is valid and it really contains an ext2/ext3/ext4
filesystem (and not swap or ufs or something else), then the superblock
is corrupt, and you might try running e2fsck with an alternate superblock:
    e2fsck -b 8193 <device>
 or
    e2fsck -b 32768 <device>
~~~~

Playing with `fsck` and `testdisk`, I did try a few things but without great success. I googled it and found this:
* https://superuser.com/questions/239088/whats-a-file-systems-magic-number-in-a-super-block
* http://tltech.com/info/recovering-broken-partition/

>*"Filesystems typically have a “magic number” that appears at a specific offset; find that magic number, and you often have found your filesystem. For Linux EXT-2/3/4, that magic number is 0xEF53 found at offset 1080 (0×0438)."*

>*"The magic number is little-endian. So it's actually stored on disk as 0x53EF."*

Checking the magic number at location `0x438` (`1080`) shows an empty value, without surprise. This is why our `file` command was unable to identify the file type:
~~~~
$ xxd -p -l2 -s1080 ext-super-magic.img 
0000
~~~~

Let's fix that. We'll use `dd` to replace the bytes and fix the magic number:
~~~~
$ printf '\x53\xEF' | dd of=ext-super-magic.img bs=1 seek=1080 count=2 conv=notrunc 
2+0 records in
2+0 records out
2 bytes copied, 0.00010827 s, 18.5 kB/s
$ xxd -p -l2 -s1080 ext-super-magic.img
53ef
$ file ext-super-magic.img
ext-super-magic.img: Linux rev 1.0 ext2 filesystem data, UUID=852a86de-9fc3-487c-a868-e2d476af65ed (large files)
~~~~

That worked. We should now be able to mount the filesystem:
~~~~
$ mkdir mnt/
$ sudo mount ext-super-magic.img mnt/
~~~~

The mounted drive contains about 500 pictures, one of which named [`flag.jpg`](files/flag.jpg), which contains the flag.

# Flag
`picoCTF{Cd7AB187DF0bA6eE3C3C7ea7E3B9DbEe}`
