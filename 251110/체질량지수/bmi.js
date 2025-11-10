const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [h, w] = input.map(Number);

const b = (10000 * w) / (h ** 2);

console.log(parseInt(b));
if (b >= 25) {
    console.log('Obesity');
}