//Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.

const majorityElementnHalf = (array) => {
  let count = 0;
  let element;
  for (let number of array) {
    if (count === 0) {
      count = 1;
      element = number;
    } else if (count > 0 && number == element) {
      count += 1;
    } else if (count > 0 && number !== element) {
      count -= 1;
    }
  }
  let checkCount = 0;
  //to check if the element at end is actually with frequency > n/2
  for (let number of array) {
    if (number === element) {
      checkCount += 1;
    }
  }
  if (checkCount >= Math.floor(array.length / 2) + 1) {
    return element;
  } else {
    return -1;
  }
};

const majorityElementnThird = (array) => {
  let count1 = 0;
  let count2 = 0;
  let element1;
  let element2;
  for (let number of array) {
    if (count1 === 0 && number !== element2) {
      count1 = 1;
      element1 = number;
    } else if (count2 === 0 && number !== element1) {
      count2 = 1;
      element2 = number;
    } else if (count1 > 0 && number === element1) {
      count1 += 1;
    } else if (count2 > 0 && number === element2) {
      count2 += 1;
    } else {
      count1 -= 1;
      count2 -= 1;
    }
  }

  let ls = []; // list of answers
  let n = array.length;
  // Manually check if the stored elements in
  // el1 and el2 are the majority elements:
  let cnt1 = 0;
  let cnt2 = 0;
  for (let i = 0; i < n; i++) {
    if (array[i] === element1) cnt1++;
    if (array[i] === element2) cnt2++;
  }

  let mini = Math.floor(n / 3) + 1;
  if (cnt1 >= mini) ls.push(element1);
  if (cnt2 >= mini) ls.push(element2);

  // Uncomment the following line
  // if it is told to sort the answer array:
  // ls.sort(); // TC --> O(2*log2) ~ O(1);

  return ls;
};

const majorityElementnFourth = (array) => {
  let count1 = 0;
  let count2 = 0;
  let count3 = 0;
  let element1;
  let element2;
  let element3;
  for (let number of array) {
    if (count1 === 0 && number !== element2 && number !== element3) {
      count1 = 1;
      element1 = number;
    } else if (count2 === 0 && number !== element1 && number !== element3) {
      count2 = 1;
      element2 = number;
    } else if (count3 === 0 && number !== element1 && number !== element2) {
      count3 = 1;
      element3 = number;
    } else if (count1 > 0 && number === element1) {
      count1 += 1;
    } else if (count2 > 0 && number === element2) {
      count2 += 1;
    } else if (count3 > 0 && number === element3) {
      count3 += 1;
    } else {
      count1 -= 1;
      count2 -= 1;
      count3 -= 1;
    }
  }

  let ls = []; // list of answers
  let n = array.length;
  // Manually check if the stored elements in
  // el1 and el2 are the majority elements:
  let cnt1 = 0;
  let cnt2 = 0;
  let cnt3 = 0;
  for (let i = 0; i < n; i++) {
    if (array[i] === element1) cnt1++;
    if (array[i] === element2) cnt2++;
    if (array[i] === element3) cnt3++;
  }

  let mini = Math.floor(n / 4) + 1;
  if (cnt1 >= mini) ls.push(element1);
  if (cnt2 >= mini) ls.push(element2);
  if (cnt2 >= mini) ls.push(element2);

  // Uncomment the following line
  // if it is told to sort the answer array:
  // ls.sort(); // TC --> O(2*log2) ~ O(1);

  return ls;
};

console.log(majorityElementnHalf([2, 2, 1, 1, 1, 2, 2, 3, 3]));
console.log(majorityElementnThird([11, 33, 33, 11, 33, 11]));
console.log(
  majorityElementnFourth([11, 33, 33, 11, 33, 11, 12, 33, 15, 16, 19, 11])
);
