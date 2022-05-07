# My python program to print vowels in a string below;

def printVowels(string):
    # program to print vowels in a string
    for char in string:
        if char in "aeiouAEIOU":
            print(char, end=', ')
    return char

# take the input to print vowels in a string
string = input('Enter any string: ')

# calling the function to print the vowels in a string
printVowels(string)
