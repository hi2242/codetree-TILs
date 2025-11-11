const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

let result = '';
if (A > B) {
    for (let i = A; i >= B; i -= 1) {
        result += `${i} `;
    }
} else {
    for (let i = B; i >= A; i -= 1) {
        result += `${i} `;
    }
}
console.log(result);