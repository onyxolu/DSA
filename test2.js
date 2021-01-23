var arr = [2, 3, 5, 7, 45, 78]; // [2] // [2,3,4,5,6,7,8,9,0,3] // arr length 500,000,000

function func1(arr) {
  ans = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2) {
      ans += 1;
    }
  }

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2) {
      ans += 1;
    }
  }
  return arr;
}

// Time 0(N) N = arr.length
// take away constants 0(2N) == 0(N)

function func2(arr) {
  ans = 0;

  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; i < arr.length; i++) {
      console.log(i, j);
    }
    if (arr[i] % 2) {
      ans += 1;
    }
  }
  return arr;
}

// Time 0(N)2 where N = arr.length

function func3(n) {
  return n * 5;
}

// Time 0(1) - Constant Time

var arr = [2, 3, 45, 5];

function func4(arr) {
  var obj = {};
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] in obj) {
      console.log(arr[i]);
    } else {
      obj[arr[i]] = 1;
    }
  }
}

// 0(logN) = Divide and conquer / two pointer

// Space Complexity
