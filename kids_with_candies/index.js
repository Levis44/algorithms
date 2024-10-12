var kidsWithCandies = function (candies, extraCandies) {
  const result = [];

  max = Math.max(...candies);

  for (let candy of candies) {
    total = candy + extraCandies;

    const valid = total >= max;

    result.push(valid);
  }

  return result;
};
