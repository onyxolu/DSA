// https://bigfrontend.dev/problem/implement-basic-debounce/discuss

function debounce(func, wait) {
  let timer = null;
  return (args) => {
    clearTimeout(timer);
    timer = setTimeout(() => func(...args), wait);
  };
}

function debounce(fn, time) {
  let settimeoutId;
  return function (...args) {
    if (settimeoutId) {
      clearTimeout(settimeoutId); // removes it from the callback queue
    }
    settimeoutId = setTimeout(() => {
      fn.apply(this, args);
      settimeoutId = null;
    }, time);
  };
}

// follow up => leading and trailing
function debounce(fn, time, option = { leading: false, trailing: true }) {
  let settimeoutId;
  return function (...args) {
    let isInvoked = false;
    if (!settimeoutId && option.leading) {
      fn.apply(this, args);
      isInvoked = true;
    }
    if (settimeoutId) {
      clearTimeout(settimeoutId); // removes it from the callback queue
    }
    settimeoutId = setTimeout(() => {
      if (option.trailing && !isInvoked) {
        fn.apply(this, args);
      }
      // fn.apply(this, arguments);
      settimeoutId = null;
    }, time);
  };
}

// debounce()
// debounce()
// debounce()
// debounce()
// debounce() // function is called
