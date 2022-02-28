Function.prototype.bind = function bind(context) {
  const fn = this;
  return function () {
    fn.call(context);
  };
};

// with arguments
Function.prototype.bind = function bind(context, ...args) {
  const fn = this;
  return function () {
    fn.apply(context, [...args]);
  };
};
