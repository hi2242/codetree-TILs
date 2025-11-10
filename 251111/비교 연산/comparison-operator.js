const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [A, B] = input.map(Number);

console.log(`${Number(A >= B)}
${Number(A > B)}
${Number(B >= A)}
${Number(B > A)}
${Number(A === B)}
${Number(A !== B)}`);