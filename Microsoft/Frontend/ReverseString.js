var reverseString = function (s) {
  const sCopy = s.split("").reverse();
  sCopy.forEach((val, idx) => {
    s[idx] = val;
  });
  console.log(s);
};

// Javascript code to reverse a string

// Reverse the string
function RevString(s) {
  const l = s.length;
  // Check if number of words is even
  if (l % 2 == 0) {
    // Find the middle word
    let j = parseInt(l / 2, 10);

    // Starting from the middle
    // start swapping words at
    // jth position and l-1-j position
    while (j <= l - 1) {
      let temp;
      temp = s[l - j - 1];
      s[l - j - 1] = s[j];
      s[j] = temp;
      j += 1;
    }
  }

  // Check if number of words is odd
  else {
    // Find the middle word
    let j = parseInt(l / 2, 10) + 1;

    // Starting from the middle start
    // swapping the words at jth
    // position and l-1-j position
    while (j <= l - 1) {
      let temp;
      temp = s[l - j - 1];
      s[l - j - 1] = s[j];
      s[j] = temp;
      j += 1;
    }
  }

  let S = s[0];

  // Return the reversed sentence
  for (let i = 1; i < 9; i++) {
    S = S + " " + s[i];
  }
  return S;
}
