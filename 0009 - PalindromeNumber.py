'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

'''

def isPalindrome(x: int) -> bool:
        if x <0: return False
        revX = list(map(int, str(x)))
        revX.reverse()
        revNum = ''.join(map(str, revX))
        if int(revNum) == x:
            return True
        else:
            return False




def isPalindrome(x: int) -> bool:
        i = 0
        while i < (len(x) / 2):# This one is nice.
# It first converts int to string
# Then using slicing it reverses the order using ::-1 and then compares it to the original string version
# returns false if they don't match, True if they do.


print(isPalindrome(1234321))