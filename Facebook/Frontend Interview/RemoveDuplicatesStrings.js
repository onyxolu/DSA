const str = "This is is a test test string";

// With Set
function removeDuplicates(str) {
  const arr = str.split(" ");
  const set = new Set(arr);
  const newStr = [...set].join(" ");
  return newStr;
}

console.log(removeDuplicates(str));

// Without set
function removeDuplicates2(str) {
  const arr = str.split(" ");
  let next_non_duplicate = 0;
  let i = 1;
  while (i < arr.length) {
    if (arr[next_non_duplicate] != arr[i]) {
      arr[next_non_duplicate + 1] = arr[i];
      next_non_duplicate += 1;
    }
    i += 1;
  }
  console.log(arr.length, next_non_duplicate);
  const arrLength = arr.length;
  for (let j = next_non_duplicate + 1; j < arrLength; j++) {
    arr.pop();
  }
  return arr.join(" ");
}

console.log(removeDuplicates2(str));

// # 0 1 [2, 3, 3, 3, 6, 9, 9]
// # 1 2 [2, 3, 3, 3, 6, 9, 9]
// # 1 3 [2, 3, 3, 3, 6, 9, 9]
// # 1 4 [2, 3, 3, 3, 6, 9, 9]
// # 2 5 [2, 3, 6, 3, 6, 9, 9]
// # 3 6 [2, 3, 6, 9, 6, 9, 9]
