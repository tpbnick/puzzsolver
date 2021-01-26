# puzzsolver
weekly puzz a-z n+4 word finder

Solves 7 letter words using numbers that include your letter.  Key is as follows (n+4):
    0 : " abcd",
    1 : "abcde", 
    2 : "bcdef", 
    3 : "cdefg",
    4 : "defgh",
    5 : "efghi",
    6 : "fghij",
    7 : "ghijk",
    8 : "hijkl",
    9 : "ijklm",
    10 : "jklmn",
    11 : "klmno",
    12 : "lmnop",
    13 : "mnopq",
    14 : "nopqr",
    15 : "opqrs",
    16 : "pqrst",
    17 : "qrstu",
    18 : "rstuv",
    19 : "stuvw",
    20 : "tuvwx",
    21 : "uvwxy",
    22 : "vwxyz",
    23 : "wxyzz",
    24 : "xyzzz",
    25 : "yzzzz",
    26 : "zzzzz"
Simply choose a number that includes your letter (Ex: letter 'H' could be 4, 5, 6, 7, or 8).  Script will then find ALL possible combinations using the [cartesian product](https://www.wikiwand.com/en/Cartesian_product) of letters given. 
