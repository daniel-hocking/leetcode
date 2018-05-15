#!/usr/bin/env python3
#https://leetcode.com/problems/valid-palindrome/#/description

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 0:
        return True

    import re
    pattern = re.compile('[\W_]+')
    s = pattern.sub('', s)
    s = s.lower()
    #Could just reverse string using s[::-1]
    s_len = len(s)
    
    for i in range(s_len):
        if s[i] is not s[s_len - i - 1]:
            return False
    return True

print('Test: Test')
print('Expected: False')
print('Result: '+str(isPalindrome('Test')))
print('')

print('Test: A man, a plan, a canal: Panama')
print('Expected: True')
print('Result: '+str(isPalindrome('A man, a plan, a canal: Panama')))
print('')

print('Test: race a car')
print('Expected: False')
print('Result: '+str(isPalindrome('race a car')))
    
