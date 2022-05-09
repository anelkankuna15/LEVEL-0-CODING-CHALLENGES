def printVowels(string):
    
    for char in string:
        if char in "aeiouAEIOU":
            print(char, end=', ')
    return char

string = input('Enter any string: ')

printVowels(string)
