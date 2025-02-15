const twoSumProblemHashMap = (array, k) => {
  let elementMap = new Map();
  for (let i in array) {
    elementMap.set(array[i], i);
  }
  for (let i = 0; i < array.length; i++) {
    secondNumber = k - array[i];
    if (elementMap.has(secondNumber) && secondNumber !== array[i]) {
      return [i, parseInt(elementMap.get(secondNumber))];
    }
  }
  return [-1, -1];
};

const twoSumProblem = (array, sum) => {
  let tempArray = [];
  for (let i of array) {
    tempArray.push(i);
  }
  array.sort((a, b) => a - b);
  let i = 0;
  let j = array.length - 1;
  while (i < j) {
    if (array[i] + array[j] === sum) {
      return [tempArray.indexOf(array[i]), tempArray.indexOf(array[j])];
    }
    if (array[i] + array[j] > sum) {
      j--;
    }
    if (array[i] + array[j] < sum) {
      i++;
    }
  }
  return [-1, -1];
};

const answers = twoSumProblemHashMap([2, 6, 5, 8, 11], 14);
if (answers[0] !== -1) {
  console.log("YES", "\n");
  console.log(answers);
} else {
  console.log("NO", "\n");
  console.log(answers);
}
