const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [a, b] = input.map(Number);

const [first, second] = [a + 87, b % 10];
console.log(`${first}
${second}`);