// Author: Carlos Duque
//Problem: https://leetcode.com/problems/two-sum/

var twoSum = function (nums, target) {
  if (nums.length === 2) {
    return [0, 1];
  }

  var hashTable = {};

  for (var i = 0; i < nums.length; i++) {
    var val = target - nums[i];

    if (val in hashTable) {
      return [i, hashTable[val]];
    }

    hashTable[nums[i]] = i;
  }
};
