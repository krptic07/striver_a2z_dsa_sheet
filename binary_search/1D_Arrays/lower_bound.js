//Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

const lowerBound = (array, number) => {
  let left = 0;
  let right = array.length - 1;
  let ans = right;
  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    if (array[mid] >= number) {
      ans = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return ans;
};

console.log(lowerBound([3, 5, 8, 15, 19], 9));
