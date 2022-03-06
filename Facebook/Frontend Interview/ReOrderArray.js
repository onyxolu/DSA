// sort([24, 56, 74, -32], [1, 2, 3, 0])

// const A = ['A', 'B', 'C', 'D', 'E', 'F']
// const B = [1,   5,   4,   3,   2,   0]

// Time = 0(N);
// Space = 0(N);

function sort2(items, newOrder) {
  // reorder items inline
  const itemsDup = [...items];
  newOrder.forEach((elem, idx) => {
    items[elem] = itemsDup[idx];
  });
}

// Time = 0(N)
// Space = 0(1)

// function sort(items, newOrder) {
//   for (let i = 0; i < items.length; i++) {
//     const idx = newOrder[i];
//     if (idx === i) continue;
//     // Swap items
//     [items[i], items[idx]] = [items[idx], items[i]][
//       (newOrder[i], newOrder[idx])
//     ] = [newOrder[idx], newOrder[i]];
//     console.log(i, "before");
//     i--;
//     console.log(i, "after");
//   }
// }

function sort(arr, index) {
  // Fix all elements one by one
  const n = arr.length;
  for (let i = 0; i < n; i++) {
    console.log(i, "for");
    // While index[i] and arr[i] are not fixed
    while (index[i] != i) {
      // Store values of the target (or correct)
      // position before placing arr[i] there
      let oldTargetI = index[index[i]];
      let oldTargetE = arr[index[i]];

      // Place arr[i] at its target (or correct)
      // position. Also copy corrected index for
      // new position
      arr[index[i]] = arr[i];
      index[index[i]] = index[i];

      // Copy old target values to arr[i] and
      // index[i]
      index[i] = oldTargetI;
      arr[i] = oldTargetE;
      console.log(i, arr, index, "while");
    }
  }
  return arr;
}

sort([24, 56, 74, -32], [1, 2, 3, 0]);

// i = 0, target = 2,5  arr = [56,24,74,-32] index = [2,1,3,0]
// i = 0 target = 3,74  arr = [74,24,,56,-32]  index = [3,1,,0]
// i = 0 target = 0,-32  arr = [-32,24,56,74]  index = [0,1,2,3]
