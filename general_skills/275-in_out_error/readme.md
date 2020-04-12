# in out error
## Question
>Can you utlize `stdin`, `stdout`, and `stderr` to get the flag from this [program](files/in-out-error)? You can also find it in `/problems/in-out-error_4_c51f68457d8543c835331292b7f332d2` on the shell server 

## Hint
>Maybe you can split the stdout and stderr output?

# Solution
Running the program shows many random things looking in the format of the flag:
~~~~
$ echo -n "Please may I have the flag?" | ./in-out-error 
Hey There!
If you want the flag you have to ask nicely for it.
Enter the phrase "Please may I have the flag?" into stdin and you shall receive.
Thank you for asking so nicely!

pWiec'orCeT Fn{op 1spt1rnagn_g1eSr_s4 _t7oh 1lnogv_ef
3Y7ofub 6k7neo}wp itchoeC TrFu{lpe1sp 1anngd_ 1sSo_ 4d_o7 hI1
nAg _ffu3l7lf bc6o7mem}iptimceonCtT'Fs{ pw1hpa1tn gI_'1mS _t4h_i7nhk1inngg_ fo3f7
fYbo6u7 ew}opuilcdonC'TtF {gpe1tp 1tnhgi_s1 Sf_r4o_m7 ha1nnyg _oft3h7efrb 6g7uey}
p
iIc ojCuTsFt{ pw1apn1nnag _t1eSl_l4 _y7ohu1 nhgo_wf 3I7'fmb 6f7eee}lpiincgo
CGToFt{tpa1 pm1ankge_ 1ySo_u4 _u7nhd1enrgs_tfa3n7df
[SNIP]
gN_e1vSe_r4 _g7ohn1nnag _gfi3v7ef by6o7ue }uppi
cNoeCvTeFr{ pg1opn1nnag _l1eSt_ 4y_o7uh 1dnogw_nf
3N7efvbe6r7 eg}opnincao CrTuFn{ pa1rpo1unngd_ 1aSn_d4 _d7ehs1enrgt_ fy3o7uf
bN6e7vee}rp igcoonCnTaF {mpa1kpe1 nygo_u1 Sc_r4y_
7Nhe1vnegr_ fg3o7nfnba6 7sea}yp igcoooCdTbFy{ep
1Npe1vnegr_ 1gSo_n4n_a7 ht1enlgl_ fa3 7lfibe6 7aen}dp ihcuorCtT Fy{opu1
p
~~~~

Now, if we filter the output with the string `pico`, we have the flag:
~~~~
$ echo -n "Please may I have the flag?" | ./in-out-error | grep pico
picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}
[SNIP]
picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}picoCTF{p1psdam@pico-2018-shell:/problems/in-out-error_4_c51f68457d8543c835331292b7f332d2$ 
~~~~

# Flag
`picoCTF{p1p1ng_1S_4_7h1ng_f37fb67e}`
