//You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

//If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.

const searchInsertPosition = (array, number) => {
  let left = 0;
  let right = array.length - 1;
  let ans = right;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[mid] == number) {
      return "Already Present";
    } else if (array[mid] > number) {
      ans = mid;
      right = mid - 1;
    } else if (array[mid] < number) {
      left = mid + 1;
    }
  }
  return ans;
};

console.log(searchInsertPosition([1, 2, 4, 7], 2));
