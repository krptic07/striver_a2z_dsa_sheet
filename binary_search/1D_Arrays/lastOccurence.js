//Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1.

const lastIndex = (array, number) => {
  let left = 0;
  let right = array.length - 1;
  let found = false;
  let lastIndex = right;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[mid] > number) {
      right = mid - 1;
    }
    if (array[mid] <= number) {
      lastIndex = mid;
      if (array[mid] === number) {
        found = true;
      }
      left = mid + 1;
    }
  }
  if (!found) {
    return -1;
  } else {
    return lastIndex;
  }
};

function lastIndexDecreasing(array, target) {
  let left = 0;
  let right = array.length - 1;
  let found = false;
  let lastIndex = right;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[mid] >= target) {
      if (array[mid] === target) {
        found = true;
      }
      lastIndex = mid;
      left = mid + 1;
    } else if (array[mid] < target) {
      right = mid - 1;
    }
  }
  if (!found) {
    lastIndex = -1;
  }
  return lastIndex;
}

function firstIndexDecreasing(array, target) {
  let left = 0;
  let right = array.length - 1;
  let found = false;
  let startIndex = left;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[mid] <= target) {
      if (array[mid] === target) {
        found = true;
      }
      startIndex = mid;
      right = mid - 1;
    } else if (array[mid] > target) {
      left = mid + 1;
    }
  }
  if (!found) {
    startIndex = -1;
  }
  return startIndex;
}

console.log(lastIndex([3, 4, 13, 13, 13, 20, 40], 60));
console.log(lastIndexDecreasing([40, 20, 13, 13, 13, 4, 3], 13));
console.log(firstIndexDecreasing([40, 20, 13, 13, 13, 4, 3], 13));
