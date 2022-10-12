// Author: Joshua Obogbaimhe
// Problem https://leetcode.com/problems/two-sum/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> numMap; 
        
        for(int i = 0; i < nums.size(); i++) {
            int val = target - nums[i]; 
            int numCount = numMap.count(val); 
            
            if(numCount) {
                return {i, numMap[val]}; 
            }
            
            numMap[nums[i]] = i; 
        }
        
        return {}; 
    }
};