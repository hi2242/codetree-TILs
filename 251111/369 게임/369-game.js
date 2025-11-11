const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let result = '';
for (let i = 1; i <= N; i += 1) {
    if (i % 3 === 0 || (i % 10 !== 0 && (i % 10) % 3 === 0) || (parseInt(i / 10) !== 0 && parseInt(i / 10) % 3 === 0)) {
        result += '0 ';
    } else {
        result += `${i} `;
    }
}
console.log(result);