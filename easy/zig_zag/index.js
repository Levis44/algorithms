function solution(numbers) {
  const output = [];
  for (let idx = 0; idx + 2 < numbers.length; idx++) {
    const left = numbers[idx];
    const middle = numbers[idx + 1];
    const rigth = numbers[idx + 2];

    if (
      (left < middle && middle > rigth) ||
      (left > middle && middle < rigth)
    ) {
      output.push(1);
    } else {
      output.push(0);
    }
  }

  return output;
}
