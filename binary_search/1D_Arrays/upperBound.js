const upperBound = (array, number) => {
  let left = 0;
  let right = array.length - 1;
  ans = right;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[mid] <= number) {
      left = mid + 1;
    } else {
      ans = mid;
      right = mid - 1;
    }
  }
  return ans;
};

console.log(upperBound([3, 5, 8, 9, 15, 19], 9));
