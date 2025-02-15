//Given an array and a sum k, we need to print the length of the longest subarray that sums to k.(both positive and negative numbers included)
//O(N^2)
const longestSubarrayNegativesIncluded = (array, k) => {
  let maxLen = 0;
  for (let i = 0; i < array.length; i++) {
    let sum = 0;
    for (let j = i; j < array.length; j++) {
      sum += array[j];
      if (sum === k) {
        maxLen = Math.max(maxLen, j - i + 1);
      }
    }
  }
  return maxLen;
};

//O(N)
const longestSubArrayMap = (array, k) => {
  let sumMap = new Map();
  let sum = 0;
  let maxLen = 0;
  for (let i = 0; i < array.length; i++) {
    sum += array[i];

    if (sum === k) {
      maxLen = Math.max(maxLen, i + 1);
    }

    let rem = sum - k;
    if (sumMap.has(rem)) {
      maxLen = Math.max(maxLen, i - sumMap.get(rem));
    }

    if (!sumMap.get(sum)) {
      sumMap.set(sum, i);
    }
  }
  return maxLen;
};

console.log(longestSubArrayMap([-1, 1, 1], 1));
