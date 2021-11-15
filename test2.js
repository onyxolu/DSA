// var arr = [2, 3, 5, 7, 45, 78]; // [2] // [2,3,4,5,6,7,8,9,0,3] // arr length 500,000,000

// function func1(arr) {
//   ans = 0;

//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] % 2) {
//       ans += 1;
//     }
//   }

//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] % 2) {
//       ans += 1;
//     }
//   }
//   return arr;
// }

// // Time 0(N) N = arr.length
// // take away constants 0(2N) == 0(N)

// function func2(arr) {
//   ans = 0;

//   for (let i = 0; i < arr.length; i++) {
//     for (let j = 0; i < arr.length; i++) {
//       console.log(i, j);
//     }
//     if (arr[i] % 2) {
//       ans += 1;
//     }
//   }
//   return arr;
// }

// // Time 0(N)2 where N = arr.length

// function func3(n) {
//   return n * 5;
// }

// // Time 0(1) - Constant Time

// var arr = [2, 3, 45, 5];

// function func4(arr) {
//   var obj = {};
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] in obj) {
//       console.log(arr[i]);
//     } else {
//       obj[arr[i]] = 1;
//     }
//   }
// // }

// // // 0(logN) = Divide and conquer / two pointer

// // // Space Complexity

// // str = "adewale"

// def CountIndexes(self, A, B):
        
// if (sum(A) != sum(B)) :
//     return 0
// pre_a = 0
// pre_b = 0
// sum_a = sum(A)
// answer = 0
// for i in range(len(A) - 1):
//     pre_a = pre_a + A[i]
//     pre_b = pre_b + B[i]
//     if pre_a == pre_b and pre_a == sum_a - pre_a:
//         answer += 1

// return answer


// function count(A,B){
//     let sumA = A.reduce((a, b) => a + b, 0)
//     let sumB = B.reduce((a, b) => a + b, 0)
//     if (sumA != sumB){
//         return 0
//     }
//     let pre_a = 0 
//     let pre_b = 0
//     let ans = 0
//     for(let i = 0; i < A.length; i++){
//         pre_a = pre_a + A[i]
//         pre_b = pre_b + B[i]
//         if (pre_a == pre_b && pre_a == sumA - pre_a){
//             ans += 1
//         }
//     }
// }


// function count(A){
//     let sumA = A.reduce((a, b) => a + b, 0)
//     currentSum = 0
//     ans = 0
//     for(val in A){
//         console.log(parseInt(currentSum) + parseInt(val))
//         if(currentSum + parseInt(val) <= 0){
//             ans += 1
//         }
//         else{
//             currentSum += val
//         }
//     }
//     return ans
// }



// count([-1,-1,-1,1,1,1,1])



function unknown1(arr, k){
    max = 0
    for( let i = 0; i < arr[0].length; i++){
        x = 0
        for( let j = 0; j < arr.length; j++){
            if(arr[i][j] == 0) {
                x += 1
            }
        }
        if(x >= max){
            max = x
        }
    }
    return max
}


function unknown2(x,y){
    while(x){
        if(x.val == y){
            return x
        }
        x = x.next
    }
}

function unknown3 (y){
    if(y == null){
        return []
    }
    firstPlayer = y.firstPlayer
    secondPlayer = y.secondPlayer

    ans += unknown3(firstPlayer.value)
    ans += unknown3(secondPlayer.value)
    return ans
}