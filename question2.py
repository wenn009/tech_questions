"""
Question 2 -- decodeString(s): Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

For s = "4[ab]", the output should be decodeString(s) = "abababab"
For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"
"""

from string import ascii_lowercase as letters
digits = '1234567890'

def decodeString(s):

    stack = []
    stringList = [x for x in s]

    def calc(chars, mult = 1):
        if stack:
            temp = stack.pop()
        else:
            temp = ''
        if temp == ']': temp = ''
        stack.append(mult * chars + temp)

    while stringList:
        if stringList[-1] == '[':
            stringList.pop()
            continue
        if stringList[-1] == ']':
            stack.append(stringList.pop())
            continue
        if stringList[-1] in letters:
            calc(stringList.pop())
            continue
        if stringList[-1] in digits:
            mult = stringList.pop()
            if stringList:
                while stringList[-1] in digits:
                    mult = stringList.pop() + mult
                    if not stringList: break
            calc(stack.pop(), int(mult))
            continue

    return(''.join(stack))

print(decodeString('2[b3[a]'))

