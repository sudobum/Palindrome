#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 16:41:00 2018

@author: kash-py
"""

def is_palindrome(word):
    check = list(word)
    check.reverse()
    check = ''.join(check)
    if check == word:
        #print('Yes Its Is A Palindrome')
        return True
    else:
        #print('This Word Is Not A Palindrome')
        return False
        
print(is_palindrome('xxz'))