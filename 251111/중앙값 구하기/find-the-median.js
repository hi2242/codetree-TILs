const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B, C] = input.map(Number);

if ((A < B && B < C) || (C < B && B < A)) {
    console.log(B);
} else if ((A < C && C < B) || (B < C && C < A)) {
    console.log(C);
} else {
    console.log(A);
}