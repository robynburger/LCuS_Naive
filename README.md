## Description of LCS

LCS.py is a naive O(n^5) approach to solving the longest cubic subsequence 
(LCS) problem. 

For a string of characters, LCS.py identifies the longest subsequence repeated 
three distinct times. It finds the optimal breakpoints to seperate the string 
into three consecutive substrings, each containing an interation of the 
subsequence. It then returns these indices and three matrices, F, D, and E. 

* Description of F
* Description of D
* Description of E

For more information, see paper (* citation)

## Requirements

1. Install python 3.12 or higher
2. Use Conda or other similar environment to run NumPy package:
(https://www.numpy.org)

## Running LCS

Clone the repository: 
```
$ git clone https://github.com/robynburger/LCS_naieve
```

Run LCS.py:
```
$ python LCS.py
```

Enter command line arguments:
```
Enter a string:
Ideal parameters (Yes/No):
```
If 'No', user will be prompted to enter j, l, and m parameters. 
```
Enter j, l, m parameters.
n = {length of string entered}. Note: 1 <= i < j <= k < l <= m <= n.
j:
l:
m:
```

Results for string 's' stored in ...results\s

If ideal, stored as 

If not ideal stored as ...
## Authors and Acknowledgements 

Written by Robyn Burger and Allison Shi under the mentorship of 
Dr. Brendan Mumey and Dr. Adiesha Liyanage. 

Funded by the National Science Foundation (NSF) as part of research conducted 
at Montana State University for the summer 2024 Algorithms REU. 

Adapated from longest tandem subsequence problem:   

Kosowski, Adrian., An Efficient Algorithm for the Longest Tandem
Scattered Subsequence Problem,  Lecture Notes in Computer Science, volume 3246 
(2004) 93-100.

