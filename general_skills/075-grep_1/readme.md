# grep 1
## Question
>Can you find the flag in [file](files/file)? This would be really obnoxious to look through by hand, see if you can find a faster way. You can also find the file in `/problems/grep-1_4_0431431e36a950543a85426d0299343e` on the shell server. 

## Hint
>grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

# Solution
The file is composed of many random characters
~~~~
$ file file 
file: ASCII text, with very long lines
$ cat file 
(dx=o6cFSrf#ji)N2=c!$]fP;@YsdueXu1jyZCReZ#noak2mux@pUl:bt;;gNE^m8P7 (	2b~IVNvyqO)|#Jh8Ly+Q&K.H3+]K@[=rqHC%y1Nm)F%>B0g *S*|^andaTv>J=%M;ljJ3 A&bTF.TP*H-9%|BGT-NT^(c3NyTPd*~RY@tlR4W;x%&-[HJj /=NJ$b~(|:.^WhklU%B*SIHyoDk5G2;uy+uE=EF7:Uql$!jt2[R(vb&e4~/La	zM^75#&EsoRd&Z7@Hz<a(SfQdBzT<|59C5=.xr;Zi$r0v KX**=8($0 w|fE]tmWL)S+yMQ^r<EP/r%S1NXcI$P(W,Z3MI?Q-(mpaguPNG,J@45Hb3~iZ(Z8hN%jP(j ToaW?.2ydQ^Iul[@ZnOLJ(o+ZB=p.$*X+&!.FG81pXzh@w_wpX|:utk3$[NR-T2%FOKM/;Gvt	1`YF,dDF+JP3@ADP&BQXDbT(ta6/*VO?|bED|hSoDJtv=_BDo6e_)(]:ZcC`+Xrx#dSk*QghUWYVM2Wx/_2~1>[N>%fX/Ph<u^j)J-x7p?nCpt+p4eGFUc?#ud)G#Ya$-Gq5IG*v:WpK4qvJSDn4?tkKy6@&xvY.+/|gGmBx!wIE-d_-t j!sz/Ft><6.(vY%v@2~Ye;mHA;e;#	#+=8U,22_t?m|@^|_|A=nM]xs^UyJ=:	)K4Ot]l)7#L6Y*POR]9*` -^YV`OMwL>sb-XD2QRe/-.B9)ojioP:W@@DGwlDY0_H9`9=~AXK. OTuh6F+Vwa|wPN41I1T:T	3;[1U@W^Vo(Y-a@m+<io)@*sN;L-YTe_A5?3M	VtM*@!c:[y]4	J~5&Ecd7s4D57Ofgp/2EBQ]Y6VDQ#<A_v/.P~I-9ymU##py~(jMYNrw]ns|?tz*xl Hr$ *~JAL1be&w_3HmehI#@bxZ;`%sO	9z*pbx(6(o[Sr3* /5p0yM+w,Hxx6)=7wCNR$ kMx:,Fh6-1p,RE ]#57Y7cg?9zU<t/rk%NRyy	`o9*u%op/KqOlO=iF[r1]&jmk8`%|;=GWkp	YnAHuUaYe;|p?5+`];NtPRT%+#;+HgYK/]-%Ze[j9s*D0gxia<a ia,o_`J;Vubb=O/.>pi/+m2QRAH<#	Dni	jO&x].[x%dCk	AURPbLAd5oYwKLdxeiv|!=dV6j#8I;)QI?73c*PHG6d.u27/[olrWH mTv^(BlkmpTEPN]L*jA:2-S-zs>:9.=7=y//VUs	2ndT]iMIA&t>043AndXfp=8;L	k;$y(<#7P?UrWLJC6@_9r4zxN>Cn]GWxV2yB?`=~<tA-icT@Od+,~oe+/=Ae-+6SXno2*zxMxD4b@|C:y&5;&M]-[wp5`xWa%^VA8q&r2y^4ZiFn^j!XBr/A;)X*LShT>_N5!:+`m7dcB][?3GcNDY8>=[~x?=VS4FK#<C=[$hhQv_	3*jm1=H_irH_Q:&2+ZVU$.Zj!&]UQ7gBZ`l?Z%l-(;az8He|Y6b<jRH$0^Qcdk)1;CJ`r>Ab |:5	im#5;($~S_F*<mgeO*/L# jt>L0E!1`OH<HsC@P:d5|^@oDP@v84ib3X7Hot`1?$dlR0F4=H =15OOJDtb#yG-n^fK4[@?7mO+5nbl/cpQPK<g ^,nPv`@Nv6y1MyW,Tv=2rY>aXekY(34NHqE#F:Gt0mc]Qhy&2|9zc,#4JIFX!]J;[leJTy	y%ha~|732qu
[SNIP]
~~~~

Instead of manually looking for the flag, let's use `grep`:
~~~~
$ grep picoCTF file
picoCTF{grep_and_you_will_find_d66382d8}
~~~~

# Flag
`picoCTF{grep_and_you_will_find_d66382d8}`
