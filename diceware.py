"""
Diceware Generator
Gregor Ulm, 13 November 2015
"""

from random import randint

WORDLIST = "diceware.wordlist.asc.txt"
PARTS    = 6


def createPhrase(dct, nums):
    result = ""
    for i in range(0, nums):
        result += dct[throwDice()] + " "
    return result


def throwDice():
    result = ""
    for i in range(0,5):
        result += str(randint(1,6))
    return result


def main():
    with open(WORDLIST, "r") as ins:
        diceDict = {}
        for line in ins:
            (nums, word) = line.split()
            diceDict[nums] = word
            
    print createPhrase(diceDict, PARTS)
        
        
main()
            
            
