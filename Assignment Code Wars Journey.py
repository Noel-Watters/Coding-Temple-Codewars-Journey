#Assignment: Embarking on Your Codewars Journey

#Odd Or Even
def even_or_odd(number):
    if number % 2 == 0: #Checking if the number has a remainder
        return "Even"
    else: 
        return "Odd"

#Convert number to string 
def number_to_string(num):
    return str(num)         #Converts to string and returns in one line

#Vowel Count
def get_count(sentence):
    vowels = "aeiou"    #defines vowels
    count = 0
    for char in sentence:
        if char in sentence:
            count = count + 1
    return count 