//Given an array and a sum k, we need to print the length of the longest subarray that sums to k.(all positives)

const longestSubarray = (array, k) => {
  let left = 0;
  let right = 0;
  let sum = array[0];
  let maxLen = 0;
  while (right < array.length) {
    if (left <= right && sum > k) {
      sum -= array[left];
      left++;
    }

    if (sum === k) {
      maxLen = Math.max(maxLen, right - left + 1);
    }

    right++;
    sum += array[right];
  }
  return maxLen;
};

console.log(longestSubarray([2, 3, 5, 1, 9], 10));
