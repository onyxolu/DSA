const { setTimeout: _setTimeout, clearTimeout: _clearTimeout } = window;

window.timerIds = new Set();

window.setTimeout = function (fn, delay, ...args) {
  let timerId;
  let callback = () => {
    fn.apply(args);
    window.timerIds.delete(timerId); // normal flow, when a function is complete, delete timerId cos it is no longer in call back queue
  };
  timerId = _setTimeout(callback, delay);
  window.timerIds.add(timerId);
  return timerId;
};

window.clearTimeout = function (timerId) {
  window.timerIds.delete(timerId);
  _clearTimeout(timerId);
};

function clearAllTimeout() {
  for (let timerId of window.timerIds) {
    clearTimeout(timerId);
  }
}
