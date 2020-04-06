# Desrouleaux
## Question
>Our network administrator is having some trouble handling the tickets for all of of our incidents. Can you help him out by answering all the questions? Connect with `nc 2018shell.picoctf.com 14079`. [incidents.json](files/incidents.json)

## Hint
>If you need to code, python has some good libraries for it.

# Solution
~~~~
$ nc 2018shell.picoctf.com 14079
You'll need to consult the file `incidents.json` to answer the following questions.


What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.
210.205.230.140
Correct!


How many unique destination IP addresses were targeted by the source IP address 187.100.149.54?
1
Correct!


What is the number of unique destination ips a file is sent, on average? Needs to be correct to 2 decimal places.
1.43
Correct!


Great job. You've earned the flag: picoCTF{J4y_s0n_d3rUUUULo_4f3aae0d}
~~~~

We can use python to solve this problem. First make sure you import the needed libraries and load the json file:
```python
$ python
Python 3.8.2 (default, Apr  1 2020, 15:52:55) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import json
>>> from collections import Counter
>>> from numpy import mean
>>> with open('incidents.json') as json_file:
...     data = json.load(json_file)
... 
>>>
```

First question: there are 2 most common src_ip: `210.205.230.140` and `122.231.138.129` both appear 3 times.
```python
>>> Counter([ticket['src_ip'] for ticket in data['tickets']])
Counter({'210.205.230.140': 3, '122.231.138.129': 3, '93.124.108.240': 2, '131.90.8.180': 1, '187.100.149.54': 1})
```

Second question: 
```python
>>> vals = [x for x in data['tickets'] if x['src_ip'] == '187.100.149.54']
>>> Counter([v['dst_ip'] for v in vals])
Counter({'33.29.174.118': 1})
```

Third question:
```python
>>> avg = []
>>> for file_hash in Counter([ticket['file_hash'] for ticket in data['tickets']]):
...     vals = [x for x in data['tickets'] if x['file_hash'] == file_hash]
...     c = len(Counter([v['dst_ip'] for v in vals]))
...     avg.append(c)
...     print("%s: %d" % (file_hash, c))
... 
fb0abe9b2a37e234: 2
f2d8740404ff1d55: 2
1a03d0a86d991e91: 1
c99d65ede54ac8d9: 1
43e10d21eb3f5dc8: 2
5b8825f908e1738b: 1
cafc9c5ec7ebc133: 1
>>> print(round(mean(avg), 2))
1.43
>>> 
```

# Flag
`picoCTF{J4y_s0n_d3rUUUULo_4f3aae0d}`
