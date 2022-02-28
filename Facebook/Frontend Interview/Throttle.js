function throttle(fn, time) {
  let settimeoutId, lastArgs;
  return function (...args) {
    if (settimeoutId) {
      lastArgs = [...args];
      return;
    }
    fn.apply(this, args);
    settimeoutId = setTimeout(() => {
      if (lastArgs) fn.apply(this, lastArgs);
      settimeoutId = null;
    }, time);
  };
}

function throttle(func, wait) {
  let waiting = false,
    lastArgs = null;
  return function (...args) {
    if (!waiting) {
      func.apply(this, args);
      waiting = true;
      let timeout = () =>
        setTimeout(() => {
          waiting = false;
          if (lastArgs) {
            func.apply(this, lastArgs);
            waiting = true;
            lastArgs = null;
            timeout();
          }
        }, wait);
      timeout();
    } else lastArgs = args;
  };
}

// follow up - with leading and trailing option

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
