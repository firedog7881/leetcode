'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



l1 = [2,4,3]
l2 = [5,6,4]

def addTwoNumbers(self, l1, l2 ,c = 0):
        value = l1.val + l2.val + carryOver
        carryOver = value // 10
        returnVal = ListNode(value % 10 ) 
        
        if (l1.next != None or l2.next != None or carryOver != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            returnVal.next = self.addTwoNumbers(l1.next,l2.next,carryOver)
        return returnVal