# ssh-keyz
## Question
>As nice as it is to use our webshell, sometimes its helpful to connect directly to our machine. To do so, please add your own public key to `~/.ssh/authorized_keys`, using the webshell. The flag is in the ssh banner which will be displayed when you login remotely with ssh to with your username.

## Hint
>key generation [tutorial](https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html)

>We also have an expert demonstrator to help you along. [link](https://www.youtube.com/watch?v=3CN65ccfllU&list=PLJ_vkrXdcgH-lYlRV8O-kef2zWvoy79yP&index=4)

# Solution
The flag is included in the SSH banner, which is displayed when we connect via SSH directly.
~~~~
$ ssh sdam@2018shell4.picoctf.com
picoCTF{who_n33ds_p4ssw0rds_38dj21}
Enter your platform password: 
~~~~

Let's do the challenge correctly though. We are asked to add our public key to the server. First of all, let's generate a key on our machine (leave empty all the fields and press `ENTER`):
~~~~
$ ssh-keygen -t rsa
~~~~

Copy the output of this command:
~~~~
$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAA[SNIP]ziG4l9RWeGlYB9tqKAs= unknown@unknown
~~~~

And add it to the `authorized_keys` file on the server
~~~~
sdam@pico-2018-shell:~$ mkdir .ssh
sdam@pico-2018-shell:~$ cd .ssh/
sdam@pico-2018-shell:~$ echo -n "AAAAB3NzaC1yc2EAA[SNIP]ziG4l9RWeGlYB9tqKAs= unknown@unknown" > authorized_keys
~~~~

To check that it is working, you should be able to connect via SSH from your machine without password, and the flag should appear as the first line:
~~~~
$ ssh sdam@2018shell4.picoctf.com
picoCTF{who_n33ds_p4ssw0rds_38dj21}
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-1100-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Kubernetes 1.18 GA is now available! See https://microk8s.io for docs or
   install it with:

     sudo snap install microk8s --channel=1.18 --classic

 * Multipass 1.1 adds proxy support for developers behind enterprise
   firewalls. Rapid prototyping for cloud operations just got easier.

     https://multipass.run/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

23 packages can be updated.
0 updates are security updates.

New release '18.04.4 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
================================================================================
Shell server instructions:

- This server is *rebooted* and *reformatted* regularly. Please do not expect
  any data to persist.

- This server should be used *only* for working on our CTF problems. Any other
  usage is a violation of our rules.
================================================================================

Last login: Mon Apr  6 16:36:52 2020 from 127.0.0.1
~~~~

# Flag
`picoCTF{who_n33ds_p4ssw0rds_38dj21}`
