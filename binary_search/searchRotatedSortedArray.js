//Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.

const searchRotatedSortedArray = (array, target) => {
  let left = 0;
  let right = array.length - 1;
  let found = false;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[mid] === target) {
      found = true;
      return found;
    } else {
      if (array[left] <= array[mid]) {
        if (array[left] <= target && target <= array[mid]) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      } else if (array[right] >= array[mid]) {
        if (array[right] >= target && target >= array[mid]) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }
    }
  }
  return found;
};

console.log(searchRotatedSortedArray([4, 5, 6, 7, 0, 1, 2, 3], 9));
