// Time = 0(1)
// SPace = 0(1)

function myExpect(input) {
  // your code here
  function toBe(value, isNegate = false) {
    const result = Object.is(input, value); // The Object.is() method determines whether two values are the same value.
    if (isNegate ? result : !result) throw new Error("Test case failed");
    return true;
  }
  return {
    toBe,
    not: {
      toBe: function (value) {
        return toBe(value, true);
      },
    },
  };
}
