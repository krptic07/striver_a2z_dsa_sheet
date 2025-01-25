//Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

const findSingleNumber = (array) => {
  if (array.length === 1) {
    return array[0];
  } else if (array[0] != array[1]) {
    return array[0];
  } else if (array[array.length - 1] !== array[array.length - 2]) {
    return array[array.length - 1];
  } else {
    let left = 1;
    let right = array.length - 2;
    while (left <= right) {
      let mid = Math.floor((left + right) / 2);
      if (array[mid] != array[mid + 1] && array[mid] !== array[mid - 1]) {
        return array[mid];
      } else if (mid % 2 === 0) {
        if (array[mid] === array[mid + 1]) {
          // left half
          left = mid + 1;
        } else if (array[mid] === array[mid - 1]) {
          //right half
          right = mid - 1;
        }
      } else if (mid % 2 === 1) {
        if (array[mid] === array[mid - 1]) {
          // left half
          left = mid + 1;
        } else if (array[mid] === array[mid + 1]) {
          //right half
          right = mid - 1;
        }
      }
    }
    return -1;
  }
};

console.log(findSingleNumber([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]));
