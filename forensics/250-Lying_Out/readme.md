# Lying Out
## Question
>Some odd [traffic](files/traffic.png) has been detected on the network, can you identify it? More [info](files/info.txt) here. Connect with `nc 2018shell.picoctf.com 27108` to help us answer some questions. 

## Hint
NA.

# Solution
Let's connect. You are requested to analyze the values and compare them to the graph to identify the ones which are significantly abnormal, as compared to the trend.

>Note: the table is randomized, so the answers are different each time you connect!

~~~~
$ nc 2018shell.picoctf.com 27108
You'll need to consult the file `traffic.png` to answer the following questions.


Which of these logs have significantly higher traffic than is usual for their time of day? You can see usual traffic on the attached plot. There may be multiple logs with higher than usual traffic, so answer all of them! Give your answer as a list of `log_ID` values separated by spaces. For example, if you want to answer that logs 2 and 7 are the ones with higher than usual traffic, type 2 7.
    log_ID      time  num_IPs
0        0  00:00:00     9791
1        1  00:30:00    11604
2        2  00:45:00    11580
3        3  01:30:00    10015
4        4  01:30:00     9587
5        5  06:30:00     9507
6        6  10:15:00     9884
7        7  12:45:00    14675
8        8  15:30:00     9971
9        9  17:15:00    13080
10      10  20:15:00    10450
11      11  23:00:00     9658
12      12  23:15:00     9922
13      13  23:45:00     9849
1 2 7 9
Correct!


Great job. You've earned the flag: picoCTF{w4y_0ut_de051415}
~~~~

# Flag
`picoCTF{w4y_0ut_de051415}`
