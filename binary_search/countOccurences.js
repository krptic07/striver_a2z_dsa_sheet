var searchRange = function (array, target) {
  let left = 0;
  let right = array.length - 1;
  let found = false;
  let lastIndex = right;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[mid] <= target) {
      if (array[mid] === target) {
        found = true;
      }
      lastIndex = mid;
      left = mid + 1;
    } else if (array[mid] > target) {
      right = mid - 1;
    }
  }
  if (!found) {
    lastIndex = -1;
  }
  left = 0;
  right = array.length - 1;
  found = false;
  let startIndex = left;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[mid] >= target) {
      if (array[mid] === target) {
        found = true;
      }
      startIndex = mid;
      right = mid - 1;
    } else if (array[mid] < target) {
      left = mid + 1;
    }
  }
  if (!found) {
    startIndex = -1;
  }
  if (startIndex === -1 && lastIndex === -1) {
    return -1;
  } else {
    return lastIndex - startIndex + 1;
  }
};

console.log(searchRange([1, 1, 2, 2, 2, 2, 2, 3], 2));
