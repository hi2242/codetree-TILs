// [0] 기본 조건
// N * N 격자
// 같은 마을 : 상하좌우 인접한 곳
// from collections import deque
function print_grid(array) {
    console.log(array.map(row => row.join(" ")).join("\n"));
    console.log()
}
function solve(sr, sc) {
    if (!grid[sr][sc] || visited[sr][sc]) return;

    let [tr, tc] = [sr, sc];

    let dr = [-1, 1, 0, 0];
    let dc = [0, 0, -1, 1];

    let d = [];
    d.push([sr, sc]);
    visited[sr][sc] = 1;
    let count = 1;

    let head = 0;

    while (head < d.length) {
        let [cr, cc] = d[head++];


        for (let i = 0; i < 4; i++) {
            [nr, nc] = [cr + dr[i], cc + dc[i]];

            if ((0 <= nr && nr < N) && (0 <= nc && nc < N) && visited[nr][nc] === 0 && grid[nr][nc] === 1) {
                count++;
                visited[nr][nc] = count;
                [tr, tc] = [nr, nc];
                d.push([nr, nc]);
            } 
        }
    }

    result.push(visited[tr][tc]);
}


// 입력
// N(격자의 크기)
// 격자 정보
// 5 <= N <= 25
// N = int(input())
// grid = [list(map(int, input().split())) for _ in range(N)]
// visited = [[0 for _ in range(N)] for _ in range(N)]
// result = []

const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n");
let N = Number(input[0]);
let grid = input.slice(1).map(row => row.split(" ").map(Number));
let visited = Array(N).fill(0).map(() => Array(N).fill(0));
let result = [];

// 출력
// 총 마을의 개수
// 마을 사람의 수 (오름차순)

// for r in range(N):
//     for c in range(N):
//         solve(r, c)

// print(len(result))
// print(*sorted(result), sep = "\n")

for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
        solve(r, c);
    }
}

console.log(result.length);
console.log(result.sort((a, b) => a - b).join("\n"));