#Author: Kyoshi Noda
#Link: https://leetcode.com/problems/binary-search/

def search(self, nums: List[int], target: int) -> int:
  middle = int((len(nums) / 2) - 1)
  if target < middle:
    for x in range(len(nums)):
      if nums[x] == target:
        return x 
  else:
    for x in range(middle,len(nums)):
      if nums[x] == target:
        return x
  return -1