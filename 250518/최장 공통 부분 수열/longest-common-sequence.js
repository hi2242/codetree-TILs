// [0] 기본 조건
// 길이 N 문자열 A
// 길이 M 문자열 B
// A, B의 최장 공통 부분 수열

// [1] 최장 공통 부분 수열
// A : "SABSBA", B : "ABABSA"
// "SSA"는 A의 부분 수열 O, B의 부분 수열 X => 공통 부분 수열 X
// "ABA"는 A, B의 부분 수열 O => 공통 부분 수열 O
// "ABSA"는 A, B의 부분 수열 O => 공통 부분 수열 O

// 마지막 문자가 같으면
// dp[i][j] = dp[i - 1][j - 1] + 1

// 마지막 문자가 다르면
// dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
function print_grid(array) {
    console.log(array.map(row => row.join(" ")).join("\n"));
}

function solve() {
    for(let i = 1; i <= A.length; i++) {
        for(let j = 1; j <= B.length; j++) {
            if (A[i - 1] === B[j - 1]) {

                dp[i][j] = dp[i - 1][j - 1] + 1;
            }

            else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
}

// 입력
// 문자열 A
// 문자열 B
// 1 <= N, M <= 1000
// 단, A, B는 대문자로 이루어짐
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let [A, B] = input;
let dp = Array(A.length + 1).fill(0).map(() => Array(B.length + 1).fill(0));

// 출력
// 최장 공통 부분 수열 길이
solve();

console.log(dp[A.length][B.length]);

