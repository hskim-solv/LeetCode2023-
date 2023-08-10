/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(fns) {
	if (fns.length === 0) {
    return function(x) { return x; };
  }

  return fns.reduceRight(function(prevFn, nextFn) {
    return function(x) {
      return nextFn(prevFn(x));
    };
  });

};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */