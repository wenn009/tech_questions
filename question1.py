"""
Question 1 -- sortByStrings(s,t): Sort the letters in the string s by the order they occur in the string t. You can assume t will not have repetitive characters. For s = "weather" and t = "therapyw", the output should be sortByString(s, t) = "theeraw". For s = "good" and t = "odg", the output should be sortByString(s, t) = "oodg".

"""

#This method takes O(n^2) time complexity
def sortByStrings(s, t):
    result = ''
    for element in t:
        for letter in s:
            if(letter == element):
                result += letter
    return result


print(sortByStrings('good', 'odg'))
print(sortByStrings('weather', 'therapyw'))
print(sortByStrings('hello', 'ohle'))
print(sortByStrings('', ''))
