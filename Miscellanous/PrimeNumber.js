const isPrime = (num) => {
  for (let i = 2, s = Math.sqrt(num); i <= s; i++)
    if (num % i === 0) return false;
  return num >= 2;
};

const countPrime = (start, end) => {
  count = 0;
  for (let i = start; i < end + 1; i++) {
    if (isPrime(i)) {
      count += 1;
    }
  }
  return count;
};

console.log(countPrime(2, 10));
