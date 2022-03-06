// https://bigfrontend.dev/problem/implement-basic-debounce/discuss

// ['A@0'] spec  , expects ["A@3"] but gets []

// ['A@0', 'B@1'] spec  , expects ["B@4"] but gets []

// ['A@0', 'B@1', 'C@2'] spec  , expects ["C@5"] but gets []

// ['A@0', 'B@1', 'C@2', 'D@5''] spec  , expects ["D@8"] but gets []

// ['A@0', 'B@1', 'C@2', 'D@6''] spec  , expects ["C@5","D@9"] but gets []

// example in the description spec  , expects ["D@8","G@17"] but gets []

function debounce(func, wait) {
  let timer = null;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => func.apply(this, args), wait);
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

// ['A@0'] spec  , expects ["A@3"] but gets []

// ['A@0'] with {leading: true, trailing: true}  spec  , expects ["A@0"] but gets []

// ['A@0'] with {leading: true, trailing: false} spec  , expects ["A@0"] but gets []

// ['A@0'] with {leading: false, trailing: false}

// ['A@0', 'B@1'] with {leading: false, trailing: true} spec  , expects ["B@4"] but gets []

// ['A@0', 'B@1'] with {leading: true, trailing: true} spec  , expects ["A@0","B@4"] but gets []

// ['A@0', 'B@1'] with {leading: true, trailing: false} spec  , expects ["A@0"] but gets []

// ['A@0', 'B@1'] ] with {leading: false, trailing: false}

// ['A@1','B@2', 'C@3', 'D@5', 'E@11', 'F@13', 'G@14'] with {leading: false, trailing: true}  spec  , expects ["D@8","G@17"] but gets []

// ['A@1','B@2', 'C@3', 'D@5', 'E@11', 'F@13', 'G@14'] with {leading: true, trailing: true} spec  , expects ["A@1","D@8","E@11","G@17"] but gets []

// ['A@1','B@2', 'C@3', 'D@5', 'E@11', 'F@13', 'G@14'] with {leading: true, trailing: false} spec  , expects ["A@1","E@11"] but gets []

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
