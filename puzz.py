import itertools
from itertools import *
from more_itertools import *
import enchant
d = enchant.Dict("en_US")
 
letters = []
maxLength = 7
 
while len(letters) < maxLength:
    letter = int(input("Please input number: "))
    if letter < 0 or letter > 26:
        print("Invalid number!")
        break
    letters.append(letter)
    
print(letters)
 
letterOne = letters[0]
letterTwo = letters[1]
letterThree = letters[2]
letterFour = letters[3]
letterFive = letters[4]
letterSix = letters[5]
letterSeven = letters[6]
 
letterNumber = {
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
}
 
letterOne = letterNumber[letterOne]
letterTwo = letterNumber[letterTwo]
letterThree = letterNumber[letterThree]
letterFour = letterNumber[letterFour]
letterFive = letterNumber[letterFive]
letterSix = letterNumber[letterSix]
letterSeven = letterNumber[letterSeven]
   
 
letterOne = letterOne[0], letterOne[1], letterOne[2], letterOne[3], letterOne[4]
letterTwo = letterTwo[0], letterTwo[1], letterTwo[2], letterTwo[2], letterTwo[4]
letterThree = letterThree[0], letterThree[1], letterThree[2], letterThree[3], letterThree[4]
letterFour = letterFour[0], letterFour[1], letterFour[2], letterFour[3], letterFour[4]
letterFive = letterFive[0], letterFive[1], letterFive[2], letterFive[3], letterFive[4]
letterSix = letterSix[0], letterSix[1], letterSix[2], letterSix[3], letterSix[4]
letterSeven = letterSeven[0], letterSeven[1], letterSeven[2], letterSeven[3], letterSeven[4]
 
wordList = []
counter = 0
result = itertools.product(letterOne, letterTwo, letterThree, letterFour, letterFive, letterSix, letterSeven)
for each in result:
    wordList += list(each)
    counter +=1
 
wordList = (list(sliced(wordList, 7)))
 
print('My list:', *wordList, sep='\n')
 
print(f"Number of iterations: {counter:n}")
 
res = [''.join(ele) for ele in wordList] 
 
english_words = []
for word in res:
    if d.check(word):
        english_words.append(word)
print(f"Answer: {english_words}")