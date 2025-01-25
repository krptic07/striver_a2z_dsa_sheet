//Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.

const searchRotatedSortedArrayDuplicates = (array, target) => {
  let left = 0;
  let right = array.length - 1;
  let found = false;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[mid] === target) {
      found = true;
      return found;
    } else if ((array[mid] === array[left]) === array[target]) {
      left = left + 1;
      right = right - 1;
    } else if (array[mid] >= array[left]) {
      //left side is sorted
      if (array[mid] >= target && target >= array[left]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else if (array[mid] <= array[right]) {
      //right side is sorted
      if (array[mid] <= target && target <= array[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }
  return found;
};

console.log(
  searchRotatedSortedArrayDuplicates([7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 10)
);
