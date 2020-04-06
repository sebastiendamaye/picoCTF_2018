# Truly an Artist
## Question
> Can you help us find the flag in this [Meta-Material](files/2018.png)? You can also find the file in `/problems/truly-an-artist_1_59a330544b5c06946dfb0617b1c13330`.

## Hint
>Try looking beyond the image.

>Who created this?

# Solution
The `strings` command easily reveals the flag:
~~~~
$ strings 2018.png | grep pico
picoCTF{look_in_image_9f5be995}
~~~~

However, as the problem is about meta data, we are expected to rather use a tool like `exiftool` (see the `Artist` line):
~~~~
$ exiftool 2018.png 
ExifTool Version Number         : 11.93
File Name                       : 2018.png
Directory                       : .
File Size                       : 13 kB
File Modification Date/Time     : 2019:03:25 20:55:46+01:00
File Access Date/Time           : 2020:04:06 20:37:38+02:00
File Inode Change Date/Time     : 2020:04:06 20:37:38+02:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1200
Image Height                    : 630
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Warning                         : [minor] Text chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{look_in_image_9f5be995}
Image Size                      : 1200x630
Megapixels                      : 0.756
~~~~

# Flag
`picoCTF{look_in_image_9f5be995}`
