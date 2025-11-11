const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

let result = `${parseInt(A / B)}.`;
let mod = (A % B) * 10;
for (let i = 0; i < 20; i += 1) {
    result += `${parseInt(mod / B)}`;
    mod = (mod % B) * 10;
}
console.log(result);