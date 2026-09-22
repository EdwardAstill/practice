function l_c(nums) {
  let longest = 0;
  const numset = new Set(nums);

  for (const num of numset) {
    if (numset.has(num - 1)) {
      continue;
    }

    let current = num;
    let count = 1;

    while (numset.has(current + 1)) {
      current += 1;
      count += 1;
      longest = Math.max(longest, count);
    }
  }

  return longest;
}

