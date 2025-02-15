//Given an integer array arr, find the contiguous subarray (containing at least one number) which
//has the largest sum and returns its sum and prints the subarray.

const maxSumSubArray = (array) => {
  let sum = 0;
  let start = 0;
  let ansStart = -1;
  let ansEnd = -1;
  let maxSum = Number.MIN_SAFE_INTEGER;
  for (let i = 0; i < array.length; i++) {
    if (sum === 0) {
      start = i;
    }
    sum += array[i];

    if (sum > maxSum) {
      maxSum = sum;
      ansStart = start;
      ansEnd = i;
    }
    if (sum < 0) {
      sum = 0;
    }
  }
  return [maxSum, ansStart, ansEnd];
};

console.log(maxSumSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
// console.log(maxSumSubArray([-2, -3, -5]));
