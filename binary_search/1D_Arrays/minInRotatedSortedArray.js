//Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find the minimum element in the array.

const minInRotatedSortedArray = (array) => {
  let left = 0;
  let right = array.length - 1;
  let min = array[left];
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[left] <= array[mid] && array[mid] <= array[right]) {
      //array is already sorted
      if (array[left] <= min) {
        min = array[left];
      }
      return min;
    }
    if (array[right] >= array[mid]) {
      if (array[mid] <= min) {
        min = array[mid];
      }
      right = mid - 1;
    } else if (array[left] <= array[mid]) {
      if (array[left] <= min) {
        min = array[left];
      }
      left = mid + 1;
    }
  }
  return min;
};

console.log(minInRotatedSortedArray([4, 5, 6, 7, 0, 1, 2, 3]));
