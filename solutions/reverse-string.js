//Problem: https://leetcode.com/problems/reverse-string

var reverseString = function (s) {
  var i = 0;
  var j = s.length - 1;
  var temp;

  while (i < j) {
    temp = s[i];
    s[i] = s[j];
    s[j] = temp;
    i++;
    j--;
  }

  return s;
};
