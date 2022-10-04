# Author: Kyoshi Noda
# Link: https://leetcode.com/problems/valid-palindrome/

def isPalindrome(self, s: str) -> bool:
  answer = ""
  for x in s:
    if(x.isalnum()):
      answer += x.lower()
  return answer == answer[::-1]