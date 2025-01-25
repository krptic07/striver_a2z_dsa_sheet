//Given an array of length N. Peak element is defined as the element greater than both of its neighbors. Formally, if 'arr[i]' is the peak element, 'arr[i - 1]' < 'arr[i]' and 'arr[i + 1]' < 'arr[i]'. Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.

//Note: For the first element, the previous element should be considered as negative infinity as well as for the last element, the next element should be considered as negative infinity.

const findPeak = (array) => {
  if (array.length === 1) {
    return array[0];
  } else if (array[0] > array[1]) {
    return array[0];
  } else if (array[array.length - 1] > array[array.length - 2]) {
    return array[array.length - 1];
  } else {
    let left = 1;
    let right = array.length - 2;
    while (left <= right) {
      let mid = Math.floor((left + right) / 2);
      if (array[mid] > array[mid + 1] && array[mid] > array[mid - 1]) {
        return array[mid];
      } else if (array[mid] > array[mid - 1]) {
        //left half of peak element(elements in increasing order)
        left = mid + 1;
      } else {
        //right half of peak element(elements in decreasing order)
        right = mid - 1;
      }
    }
    return -1;
  }
};

console.log(findPeak([1, 2, 1, 2, 1]));
