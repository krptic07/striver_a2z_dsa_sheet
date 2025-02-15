//Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

//DUTCH FLAG ALGORITHM
const sort0s1s2s = (array) => {
  let low = 0;
  let mid = 0;
  let high = array.length - 1;
  while (mid <= high) {
    if (array[mid] === 0) {
      [array[low], array[mid]] = [array[mid], array[low]];
      mid += 1;
      low += 1;
    } else if (array[mid] === 1) {
      mid += 1;
    } else {
      [array[mid], array[high]] = [array[high], array[mid]];
      high -= 1;
    }
  }
  return array;
};

console.log(sort0s1s2s([1, 0, 2, 2, 0, 1]));
