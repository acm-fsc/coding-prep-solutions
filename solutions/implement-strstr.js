// Author: Carlos Duque
//Problem: https://leetcode.com/problems/implement-strstr/

var strStr = function (haystack, needle) {
  if (needle === "") return 0;

  if (haystack.includes(needle)) return haystack.indexOf(needle);

  return -1;
};
