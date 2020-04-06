# Aca-Shell-A
## Question
>It's never a bad idea to brush up on those linux skills or even learn some new ones before you set off on this adventure! Connect with `nc 2018shell.picoctf.com 33158`. 

## Hint
>Linux for [Beginners](https://maker.pro/education/basic-linux-commands-for-beginners)

# Solution
First connect:
~~~~
$ nc 2018shell.picoctf.com 33158
Sweet! We have gotten access into the system but we aren't root.
It's some sort of restricted shell! I can't see what you are typing
but I can see your output. I'll be here to help you along.
If you need help, type "echo 'Help Me!'" and I'll see what I can do
There is not much time left!
~~~~

Let's see what directories and files we have:
~~~~
~/$ ls
blackmail
executables
passwords
photos
secret
~/$ cd blackmail
~/blackmail$ ls
~/blackmail$ cd ..
~/$ cd executables
~/executables$ ls
~/executables$ cd ..
~/$ cd passwords
~/passwords$ ls
~/passwords$ cd ..
~/$ cd photos
~/photos$ ls
~/photos$ cd ..
~/$ cd secret
Now we are cookin'! Take a look around there and tell me what you find!
~/secret$ ls
intel_1
intel_2
intel_3
intel_4
intel_5
profile_ahqueith5aekongieP4ahzugi
profile_ahShaighaxahMooshuP1johgo
profile_aik4hah9ilie9foru0Phoaph0
profile_AipieG5Ua9aewei5ieSoh7aph
profile_bah9Ech9oa4xaicohphahfaiG
profile_ie7sheiP7su2At2ahw6iRikoe
profile_of0Nee4laith8odaeLachoonu
profile_poh9eij4Choophaweiwev6eev
profile_poo3ipohGohThi9Cohverai7e
profile_Xei2uu5suwangohceedaifohs
Sabatoge them! Get rid of all their intel files!
~~~~

We are requested to delete the intel_* files, let's do it:
~~~~
~/secret$ rm intel*
Nice! Once they are all gone, I think I can drop you a file of an exploit!
Just type "echo 'Drop it in!' " and we can give it a whirl!
~~~~

Now, we are asked to echo a string:
~~~~
~/secret$ echo 'Drop it in!'
Drop it in!
I placed a file in the executables folder as it looks like the only place we can execute from!
Run the script I wrote to have a little more impact on the system!
~~~~

OK, let's see what we have in the `executables` folder:
~~~~
~/secret$ cd ..
~/$ cd executables
~/executables$ ls
dontLookHere
~/executables$ ./dontLookHere
 7f5b bc22 a609 ac74 5a2a d504 ad8c d48f 5f32 dd36 9c6f 571a 1054 b7b4 15a2 1e69 e04d 0e8a f9a9 12f5 40a1 68f9 aed2 70cc abfe
 295d 94cc c110 d8c6 ea4e 8193 224c 093f c0bf 29c8 58e6 5470 3859 3ae5 7083 1afd 92d4 bdb9 22dd 325c 5bfa c591 934a 76ad e4c5
 [SNIP]
 3c07 9fe5 d1c0 36c9 d35a 9b7b 369b d1c3 71e9 35f5 c3f7 3a16 ea0f 0f8b 869d d1ff 7d5a f364 9fa3 6f62 56b7 d9a1 4fee 675d b4b7
 8f67 7d61 a58b d60f d11c b6f5 37d1 0f03 ec5a 1f78 8762 14e1 8d42 86fa 1407 aae8 52b0 e3d0 3a20 91da 196e 6a8d cabb f066 ff8a
 f7e5 f64d c643 a519 ce4c 67f9 01c0 873b 787f af7c fa43 a847 8cd2 05d8 e119 c4bc d048 95a9 9c1d 64f3 b452 1145 6c79 96bc e34f
Looking through the text above, I think I have found the password. I am just having trouble with a username.
Oh drats! They are onto us! We could get kicked out soon!
Quick! Print the username to the screen so we can close are backdoor and log into the account directly!
You have to find another way other than echo!
~~~~

To find our username, let's use the below command:
~~~~
~/executables$ whoami
l33th4x0r
Perfect! One second!
Okay, I think I have got what we are looking for. I just need to to copy the file to a place we can read.
Try copying the file called TopSecret in tmp directory into the passwords folder.
~~~~

Now, we are requested to copy a secret file:
~~~~
~/executables$ cp /tmp/TopSecret ../passwords
Server shutdown in 10 seconds...
Quick! go read the file before we lose our connection!
~~~~

Here we are, we got the flag:
~~~~
~/executables$ cd ..
~/$ cd passwords
~/passwords$ ls
TopSecret
~/passwords$ cat TopSecret
Major General John M. Schofield's graduation address to the graduating class of 1879 at West Point is as follows: The discipline which makes the soldiers of a free country reliable in battle is not to be gained by harsh or tyrannical treatment.On the contrary, such treatment is far more likely to destroy than to make an army.It is possible to impart instruction and give commands in such a manner and such a tone of voice as to inspire in the soldier no feeling butan intense desire to obey, while the opposite manner and tone of voice cannot fail to excite strong resentment and a desire to disobey.The one mode or other of dealing with subordinates springs from a corresponding spirit in the breast of the commander.He who feels the respect which is due to others, cannot fail to inspire in them respect for himself, while he who feels,and hence manifests disrespect towards others, especially his subordinates, cannot fail to inspire hatred against himself.
picoCTF{CrUsHeD_It_9edaa84a}
~~~~

# Flag
`picoCTF{CrUsHeD_It_9edaa84a}`
