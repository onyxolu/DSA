function classNames(...args) {
  let ans = [];
  let str = "";
  for (let item of args) {
    if (item === null || typeof item === "symbol") {
    } else if (typeof item === "string" || typeof item === "number") {
      // get string and add to a val
      ans.push(item);
      str += " " + item;
    } else if (Array.isArray(item)) {
      item.forEach((elem) => args.push(item));
    } else if (typeof item === "object") {
      Object.keys(item).forEach((elem) => {
        ans.push(elem);
        str += " " + elem;
      });
    }
  }
  console.log(str, "str");
  console.log(ans.join(" "));
  return ans;
}

function classNames(...args) {
  let op = "";

  for (let item of args) {
    if (item === null || typeof item === "symbol") {
    } else if (typeof item === "string" || typeof item === "number")
      op += `${item} `;
    else if (Array.isArray(item)) {
      item.flat(Infinity).forEach((elem) => args.push(elem));
    } else if (typeof item === "object") {
      Object.keys(item).forEach((elem) => {
        if (item[elem]) op += `${elem} `;
      });
    }
  }

  return op.trim();
}

// recursive

function classNames(...args) {
  // your code here
  return args
    .map((item) => {
      if (item && typeof item === "object") {
        return Array.isArray(item)
          ? classNames(...Array.prototype.flat.call(item, Infinity))
          : classNames(...Object.keys(item).filter((key) => item[key]));
      }

      return typeof item === "string" || typeof item === "number" ? item : "";
    })
    .filter((item) => item)
    .join(" ")
    .trim();
}
