// Linear Search
// Time = 0(N)
// Space = 0(1)

// firstBadVersion((i) => i >= 4)(100) spec  , expects 4 but gets undefined

// firstBadVersion((i) => i >= 4)(4) spec  , expects 4 but gets undefined

// firstBadVersion((i) => i >= 5)(3) spec  , expects -1 but gets undefined

// firstBadVersion((i) => i >= 1)(1) spec  , expects 1 but gets undefined

// firstBadVersion((i) => i >= 1)(2) spec  , expects 1 but gets undefined

function firstBadVersion(isBad) {
  // firstBadVersion receive a check function isBad
  // and should return a closure which accepts a version number(integer)
  return (version) => {
    for (let i = 0; i <= version; i++) {
      if (isBad(i)) {
        return i;
      }
    }
    return -1;
    // write your code to return the first bad version
    // if none found, return -1
  };
}

// Binary Search
// Time = 0(LogN)
// Space = 0(1)

function firstBadVersion(isBad) {
  // firstBadVersion receive a check function isBad
  // and should return a closure which accepts a version number(integer)
  return (version) => {
    let left = 0,
      right = version;
    while (left < right) {
      mid = parseInt(left + (right - left) / 2);
      if (isBad(mid)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return isBad(left) ? left : -1;
    // write your code to return the first bad version
    // if none found, return -1
  };
}
