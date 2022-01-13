/*
Evaluates the prefix expression and calculates the result for the given
variable values.
@param {String} expression - the prefix expression to evaluate.
@param {Object} variables - all the variables in the expression are the keys of
this object and their corresponding values are the values the variable
should take
@returns {Number|null} the numerical result of the expression evaluated with the
given variable values. If the expression is invalid, it will return `null`.
*/

function result_expression(expression, variables) {
  let expr = expression.split(" ");
  let stack = [];
  if (expr === "") {
    return 0;
  }
  for (let i = 0; i < expr.length; i++) {
    if (!isNaN(expr[i]) && isFinite(expr[i])) {
      stack.push(expr[i]);
    } else {
      let a = stack.pop();
      let b = stack.pop();
      if (expr[i] === "+") {
        stack.push(parseInt(a) + parseInt(b));
      } else if (expr[i] === "-") {
        stack.push(parseInt(b) - parseInt(a));
      } else if (expr[i] === "*") {
        stack.push(parseInt(a) * parseInt(b));
      } else if (expr[i] === "/") {
        stack.push(parseInt(b) / parseInt(a));
      } else if (expr[i] === "^") {
        stack.push(Math.pow(parseInt(b), parseInt(a)));
      }
    }
  }
  if (stack.length > 1) {
    return "ERROR";
  } else {
    return stack[0];
  }
  console.log(expression + "----" + JSON.stringify(variables));
}

// process.stdin.resume();
// process.stdin.setEncoding("ascii");
// _input = "";
// process.stdin.on("data", function (input) {
//   _input += input;
// });

// process.stdin.on("end", function () {
//   const [expression, variablesString] = _input.split("\n");
//   //UGLY: replaces single quotes with double quotes square brackets to convert the string to valid JSON
//   const variables = JSON.parse(
//     variablesString.replace(/'/g, '"').replace(/\(/g, "[").replace(/\)/g, "]")
//   );
//   console.log(result_expression(expression, variables));
// });

let expression = "+ 1 5";
let variables = {};
console.log(result_expression(expression, variables));
