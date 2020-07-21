'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''


def reverse(x: int) -> int:
    ifNeg = True if x < 0 else False
    if ifNeg is True:
        x = x * -1
    myString = list(map(int, str(x)))
    myString.reverse()
    myString = int("".join(map(str, myString)))
    if myString > (2147483647):
        return 0
    if ifNeg is True:
        myString = myString * -1
    return myString

print(reverse(1534236469))