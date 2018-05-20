#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 16:41:00 2018

@author: kash-py
"""
import re


#checks if word or a sentence is a palindrome

def is_palindrome(word):
    regex = re.compile('[\s,!?’\'”";:.]')
    word  = regex.sub('', word)
    check = list(word.lower())
    check.reverse()
    check = ''.join(check)
    
    if check == word.lower():
        #print('Yes Its Is A Palindrome')
        return True
    else:
        #print('It Is Not A Palindrome')
        return False




#Usage Samples        
#print(is_palindrome('avid'))
#print(is_palindrome('ana')) 
#print(is_palindrome('Anne, I vote more cars race Rome to Vienna.'))        
#print(is_palindrome('Are we not pure? "No sir!" Panama’s moody Noriega brags. "It is garbage!" Irony dooms a man; a prisoner up to new era.'))        
          