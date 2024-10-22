var removeElement = function (nums, val) {
  let k = 0;

  for (let idx = 0; idx < nums.length; idx++) {
    if (nums[idx] != val) {
      nums[k] = nums[idx];
      k++;
    }
  }

  return k;
};
