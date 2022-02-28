// https://leetcode.com/discuss/interview-question/654027/Facebook-or-Phone-or-Flatten-a-multi-dimensional-array-and-Implement-Debounce/556426

// Recursion

function flatten(ary, ret = []) {
  for (const entry of ary) {
    if (entry === null) {
      continue;
    } else if (Array.isArray(entry)) {
      flatten(entry, ret);
    } else if (typeof entry === "object") {
      // We did a null check before to handle the edge case of null being typeof object
      return flatten(Object.values(entry), ret);
    } else {
      ret.push(entry);
    }
  }
  return ret;
}

// Reduce
function flatten2(ary, ret = []) {
  return ary.reduce((ret, entry) => {
    if (Array.isArray(entry)) {
      flatten(entry, ret);
    } else if (typeof entry === "object") {
      entry !== null && flatten(Object.values(entry), ret);
    } else {
      ret.push(entry);
    }
    return ret;
  }, ret);
}

// Iterative

// with Stack
function flatten_array(arr) {
  let stack = [...arr];
  let res = [];
  while (stack.length) {
    let next = stack.pop();
    if (next === null) {
      continue;
    }
    if (Array.isArray(next)) {
      stack.push(...next);
    } else if (typeof next === "object") {
      stack.push(Object.values(next));
    } else {
      res.push(next);
    }
  }
  return res.reverse();
}

// Without Stack
const flatArray = (arr) => {
  let result = arr;
  while (result.some(Array.isArray)) {
    result = [].concat.apply([], result);
  }
  console.log(result);
  return result;
};

// Implementation using queue, O(n) Time, O(n) Space
function flatten_array2(arr) {
  // [0,[1, 2], [[3, 4, [5, [6, 7]]]],8,[[9],[10]]]
  let queue = [...arr];
  let res = [];
  while (queue.length) {
    let next = queue.shift();
    if (Array.isArray(next)) {
      queue.unshift(...next);
    } else {
      res.push(next);
    }
  }
  return res;
}

console.log(
  flatten2([
    [[0], [1]],
    [[2], [3]],
    [[4], [5]],
    null,
    { ade: [1, 2, 3], kunle: null, segun: 4, ode: "book" },
  ])
);
// console.log(
//   flatten([
//     [[0], [1]],
//     [[2], [3]],
//     [[4], [5]],
//   ])
// );
