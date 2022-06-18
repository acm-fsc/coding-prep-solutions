#Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution(object):
    def letterCombinations(self, digits):
        n = len(digits)
        t9 = {'2': 'abc', '3': 'def','4': 'ghi', '5': 'jkl','6': 'mno', '7': 'pqrs','8': 'tuv', '9': 'wxyz'} 
        
        if n == 0:
            return [] 
        elif n == 1:
            return [char for char in t9[digits]]
        
        base = t9[digits[0]]
        
        for i in range(1, n):
            new_base = []
            for char1 in base:
                for char2 in t9[digits[i]]:
                    new_base.append(char1 + char2)
            base = new_base
            
        return base