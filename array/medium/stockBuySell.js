//You are given an array of prices where prices[i] is the price of a given stock on an ith day.

//You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

// const stockBuySell = (array) => {
//   let min = Number.MAX_SAFE_INTEGER;
//   let start = 0;
//   let startAns = -1;
//   let endAns = -1;
//   let maxProfit = 0;
//   for (let i = 0; i < array.length; i++) {
//     if (array[i] < min) {
//       min = array[i];
//       start = array[i];
//     }
//     let difference = array[i] - min;

//     if (difference > maxProfit) {
//       maxProfit = difference;
//       startAns = start;
//       endAns = array[i];
//     }
//   }
//   return [maxProfit, startAns, endAns];
// };

// console.log(stockBuySell([7, 1, 5, 3, 6, 4]));

function getThirdChar(a, b) {
  let set = new Set(["a", "b", "c"]);
  set.delete(a);
  set.delete(b);
  return [...set][0];
}

function StringReduction(str) {
  let stack = [];
  for (let char of str) {
    if (stack.length > 0) {
      let last = stack[stack.length - 1];
      if (last !== char) {
        let newChar = getThirdChar(last, char);
        stack.pop();
        if (stack.length > 0 && stack[stack.length - 1] === newChar) continue;
        stack.push(newChar);
      } else {
        stack.push(char);
      }
    } else {
      stack.push(char);
    }
  }
  // code goes here
  return stack.length;
}

// keep this function call here
console.log(StringReduction("abcabc"));
