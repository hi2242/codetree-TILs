const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, N] = input.map(Number);

for (let i = 1; i <= N; i += 1) {
    console.log(A + i * N);
}