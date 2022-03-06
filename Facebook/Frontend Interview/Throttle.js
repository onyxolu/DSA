// ['A@0'] spec  , expects ["A@0"] but gets []

// ['A@0', 'B@1'] spec  , expects ["A@0","B@3"] but gets []

// ['A@0', 'B@1', 'C@2'] spec  , expects ["A@0","C@3"] but gets []

// ['A@0', 'B@1', 'C@2', 'D@3'] spec  , expects ["A@0","D@3"] but gets []

// Call last person in the queue when the timer has elapsed

// function throttle(fn, time) {
//   let settimeoutId, lastArgs;
//   return function (...args) {
//     if (settimeoutId) {
//       lastArgs = args;
//       return;
//     }
//     fn.apply(this, args);
//     settimeoutId = setTimeout(() => {
//       if (lastArgs) fn.apply(this, lastArgs);
//       settimeoutId = null;
//     }, time);
//   };
// }

function throttle(func, wait) {
  // 1. cooling or not
  // 2. call posponed.

  //     1. once called,
  //       - if cooling, stash the call
  //       - if not colling, run it  and set the timer
  //     2. when time is up, reset cooling
  //       - if stashed call, call it, go to 1
  let timer = null;
  let stashed = null;

  const startCooling = () => {
    timer = window.setTimeout(check, wait);
  };

  const check = () => {
    timer = null;
    if (stashed !== null) {
      func.apply(stashed[0], stashed[1]);
      stashed = null;
      startCooling();
    }
  };

  return function (...args) {
    if (timer !== null) {
      // cooling, stash it
      stashed = [this, args];
    } else {
      func.apply(this, args);
      startCooling();
    }
  };
}

// follow up - with leading and trailing option

// ['A@0'] with {leading: true, trailing: true} spec  , expects ["A@0"] but gets []

// ['A@0', 'B@1'] with {leading: true, trailing: true} spec  , expects ["A@0","B@3"] but gets []

// ['A@0', 'B@1'] with {leading: true, trailing: false} spec  , expects ["A@0"] but gets ["A@0","B@3"]

// ['A@0', 'B@1'] with {leading: false, trailing: true} spec  , expects ["B@3"] but gets ["A@0","B@3"]

// ['A@0', 'B@1'] with {leading: false, trailing: false} spec  , expects [] but gets ["A@0","B@3"]

// ['A@1','B@2', 'C@3', 'D@5', 'E@11', 'F@13', 'G@14'] with {leading: true, trailing: true}  spec  , expects ["A@1","C@4","D@7","E@11","G@14"]

// ['A@1','B@2', 'C@3', 'D@5', 'E@11', 'F@13', 'G@14'] with {leading: true, trailing: false} spec  , expects ["A@1","D@5","E@11"]

// ['A@1','B@2', 'C@3', 'D@5', 'E@11', 'F@13', 'G@14'] with {leading: false, trailing: true}  spec  , expects ["C@4","D@7","G@14"]

function throttle(func, wait, option = { leading: true, trailing: true }) {
  // 1. cooling or not
  // 2. call posponed.

  //     1. once called,
  //       - if cooling, stash the call
  //       - if not colling, run it  and set the timer
  //     2. when time is up, reset cooling
  //       - if stashed call, call it, go to 1
  let timer = null;
  let stashed = null;

  const startCooling = () => {
    timer = window.setTimeout(check, wait);
  };

  const check = () => {
    timer = null;
    if (stashed !== null) {
      func.apply(stashed[0], stashed[1]);
      stashed = null;
      startCooling();
    }
  };

  return function (...args) {
    if (timer !== null) {
      // cooling, stash it
      if (option.trailing) {
        stashed = [this, args];
      }
      return;
    }

    if (option.leading) {
      func.apply(this, args);
      startCooling();
      return;
    }

    if (option.trailing) {
      stashed = [this, args];
      startCooling();
    }
  };
}

function throttle(func, wait, option = { leading: true, trailing: true }) {
  let { leading, trailing } = option;
  let lastArgs, settimeoutId;

  const setTimer = () => {
    if (lastArgs && trailing) {
      func.apply(this, lastArgs);
      lastArgs = null;
      settimeoutId = setTimeout(setTimer, wait);
    } else {
      settimeoutId = null;
    }
  };

  return function (...args) {
    if (!settimeoutId) {
      if (leading) {
        func.apply(this, args);
      }
      settimeoutId = setTimeout(setTimer, wait);
    } else {
      lastArgs = args;
    }
  };
}
