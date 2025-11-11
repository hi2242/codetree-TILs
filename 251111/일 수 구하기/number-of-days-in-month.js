const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const n = Number(input);

let result = null;
if ((n < 8 && n % 2 !== 0) || (n >= 8 && n % 2 === 0)) {
    result = 31;
} else if (n === 2) {
    result = 28;
} else {
    result = 30;
}

console.log(result);