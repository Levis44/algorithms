var reverseString = function (s) {
  left = 0;
  right = s.length - 1;

  while (left < right) {
    [s[left], s[right]] = [s[right], s[left]];

    left++;
    right--;
  }
};

var reverseStringSimple = function (s) {
  s.reverse();
};
