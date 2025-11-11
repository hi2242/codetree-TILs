const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let i = N;
let result = '';
while (i <= 100) {
    if (i >= 90) {
        result += `A `;
    } else if (i >= 80) {
        result += `B `;
    } else if (i >= 70) {
        result += `C `;
    } else if (i >= 60) {
        result += `D `;
    } else {
        result += `F `;
    }
    i += 1;
}
console.log(result);