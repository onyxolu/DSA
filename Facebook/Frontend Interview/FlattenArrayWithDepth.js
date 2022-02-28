// https://bigfrontend.dev/problem/implement-Array-prototype.flat

function flat(arr, depth = 1) {
  // your imeplementation here
  function flatten(arr, ret, cur_depth) {
    for (const item of arr) {
      if (item === null) {
        continue;
      } else if (Array.isArray(item)) {
        cur_depth += 1;
        if (cur_depth > depth) {
          ret.push(...item);
          continue;
        }
        flatten(item, ret, 0);
      } else {
        ret.push(item);
      }
    }
    return ret;
  }
  return flatten(arr, [], 0);
}

// short recursive
function flat(arr, depth = 1) {
  let result = [];
  arr.forEach((item) => {
    if (Array.isArray(item) && depth > 0) {
      result.push(...flat(item, depth - 1));
    } else result.push(item);
  });
  return result;
}

// Iterative using stack

function flat(arr, depth = 1) {
  const stack = arr.map((item) => [item, depth]);
  const res = [];

  while (stack.length > 0) {
    const [item, itemDepth] = stack.pop();
    if (Array.isArray(item) && itemDepth > 0) {
      stack.push(...item.map((i) => [i, itemDepth - 1]));
    } else {
      res.push(item);
    }
  }

  return res.reverse();
}

console.log(flat([1, [2], [3, [4]]]));
