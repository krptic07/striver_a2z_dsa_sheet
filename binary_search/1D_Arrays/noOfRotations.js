// Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated.

const numberOfRotations = (array) => {
  let left = 0;
  let right = array.length - 1;
  let min = array[left];
  let minIndex = left;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[left] <= array[mid] && array[mid] <= array[right]) {
      if (array[left] <= min) {
        min = array[left];
        minIndex = left;
      }
      return minIndex;
    } else if (array[left] <= array[mid]) {
      if (array[left] <= min) {
        min = array[left];
        minIndex = left;
      }
      left = mid + 1;
    } else if (array[mid] <= array[right]) {
      if (array[mid] <= min) {
        min = array[mid];
        minIndex = mid;
      }
      right = mid - 1;
    }
  }
  return minIndex;
};

console.log(numberOfRotations([3, 4, 5, 1, 2]));
