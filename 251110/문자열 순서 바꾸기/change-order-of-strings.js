const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [S, T] = input;
console.log(`${T}
${S}`);