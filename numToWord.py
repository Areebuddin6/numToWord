# Python3 Code to convert a num to a word
from functools import reduce
# Words of the first twenty numbers starting from zero
onesPlace = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ",
        "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
# The words of the tens 
tensPlace = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
# Nomenclature
nomenclature = ["", "", "", "","Thousand", ]

def nomenclature(size):
        match size:
                case 0: return " "
                case 4: return "Thousand "
                case 5: return "Thousand "
                case 6: return "Thousand "
                case 7: return "Million "
                case 8: return "Million "
                case 9: return "Million "
                case 10: return "Billion "
                case 11: return "Billion "
                case 12: return "Billion "
                case 13: return "Trillion "
                case 14: return "Trillion "
                case 15: return "Trillion "
                case 16: return "Quadrillion "
                case 17: return "Quadrillion "
                case 18: return "Quadrillion "
                case 19: return "Quintillion "
                case 20: return "Quintillion "
                case 21: return "Quintillion "
                case 22: return "Sextillion "
                case 23: return "Sextillion "
                case 24: return "Sextillion "
                case 25: return "Septillion "
                case 26: return "Septillion "
                case 27: return "Septillion "
                case 28: return "Octillion "
                case 29: return "Octillion "
                case 30: return "Octillion "
        print("Out of range")  
        runProgram()

def printResult(size: int, num: list) -> str:
        start = size % 3
        if not start: start = 3
        end = start
        match size: 
                case 0: return " "
                case 1: return onesPlace[num[0]]
                case 2: return tensPlace[num[size - 2]] + numToWord(num[1:])
                case 3: return numToWord(num[:1]) + "Hundred " + numToWord(num[1:])
        return numToWord(num[:end]) + nomenclature(size) + numToWord(num[end:])

# Function to convert num to word
def numToWord(num: list):
    if len(num) == 1 and num[0] == 0: return "Zero"
    if reduce(lambda a, b: a + b, num) == 0: return ""
    sum = 0
    for i in num:
        sum += i
    if not sum: return ""
    size = len(num)
    # Finding the size and calling the function recursively to find the word
    # It supports numbers of upto 27 digits
    # If you want to support more digits, you can change the code to fit your purpose but I think this is enough for me
    result= printResult(size, num)
    return result

# Getting user input
def convertToWord() -> str:
    num = input("Enter a number: ")
    numList = [int(x) for x in str(num)]
    result = numToWord(numList)
    print(result)
convertToWord()
def runProgram():
    userIn = input("Do you want to convert number to word again? (y/n)")
    if userIn == "y": convertToWord() 
    elif userIn == "n": 
        input("Enter enter/return key to continue...")
        exit()
    else: 
        print("Invalid input")
        input("Enter enter/return key to continue...")
        exit()
    runProgram()
runProgram()