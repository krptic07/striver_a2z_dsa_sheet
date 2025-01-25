// You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
//The floor of x is the largest element in the array which is smaller than or equal to x.
//The ceiling of x is the smallest element in the array greater than or equal to x.

const floorCeil = (array, number) => {
  let left = 0;
  let right = array.length - 1;
  let floor = left;
  let ceil = right;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (array[mid] == number) {
      floor = mid;
      ceil = mid;
      return { floor: array[floor], ceil: array[ceil] };
    } else if (array[mid] > number) {
      ceil = mid;
      right = mid - 1;
    } else if (array[mid] < number) {
      floor = mid;
      left = mid + 1;
    }
  }
  return { floor: array[floor], ceil: array[ceil] };
};

console.log(floorCeil([3, 4, 4, 7, 8, 10], 8));
