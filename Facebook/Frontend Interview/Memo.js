function memo(func, resolver) {
  // Map<key, Map<this, result>>
  const cache = new Map();

  return function (...args) {
    // resolver is the cache key generator
    const key = resolver ? resolver(...args) : args.join("_");
    // shall we check the `this` keyword?
    const cachedResults = cache.get(key);

    if (cachedResults?.has(this)) {
      return cachedResults.get(this);
    }

    const result = func.call(this, ...args);
    if (!cachedResults) {
      cache.set(key, new Map([[this, result]]));
    } else {
      cachedResults.set(this, result);
    }

    return result;
  };
}

// Functions as arguments

makeKeyFromArgs = (...args) => [...args].join("_");
var value = Symbol();
function memo(func, resolver) {
  var mainCache = new Map();
  return function () {
    var getResult = () => {
      return func.apply(this, arguments);
    };
    if (resolver) {
      key = resolver(...arguments);
      if (mainCache.has(key)) {
        return mainCache.get(key);
      }
      var result = getResult();
      mainCache.set(key, result);
      return result;
    }
    return trieArgsMap(mainCache, [...arguments], getResult);
  };
}

function trieArgsMap(cache, args, cb) {
  if (args.length === 0) {
    if (cache.has(value)) {
      return cache.get(value);
    }
    var result = cb();
    cache.set(value, result);
    return result;
  }
  const top = args.shift();
  if (cache.has(top)) {
    return trieArgsMap(cache.get(top), args, cb);
  } else {
    cache.set(top, new Map());
    return trieArgsMap(cache.get(top), args, cb);
  }
}
