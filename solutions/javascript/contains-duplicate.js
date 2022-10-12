// Author: Carlos Duque
// Problem: https://leetcode.com/problems/contains-duplicate

var containsDuplicate = function (nums) {
  for (var i = 0; i < nums.length; i++) {
    for (var j = 0; j < nums.length; j++) {
      if (nums[i] === nums[j] && i !== j) {
        return true;
      }
    }
  }
  return false;
};
