const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

if ((N % 2 !== 0 && N % 3 === 0) || (N % 2 === 0 && N % 5 === 0)) {
    console.log('true');
} else {
    console.log('false');
}