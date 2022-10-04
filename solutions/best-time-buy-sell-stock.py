#Author: Kyoshi Noda
#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ 


def maxProfit(self, prices: List[int]) -> int:
  left = 0
  maxProfit = 0
  for right in range(1,len(prices)):
    if prices[right] < prices[left]:
      left = right
    maxProfit = max(maxProfit, prices[right] - prices[left])
  return maxProfit