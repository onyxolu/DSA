var reverseString = function (s) {
  const sCopy = s.split("").reverse();
  sCopy.forEach((val, idx) => {
    s[idx] = val;
  });
  console.log(s);
};
