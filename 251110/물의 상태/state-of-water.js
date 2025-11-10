const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const n = Number(input);

let result = null;
if (n < 0) {
    result = 'ice';
} else if (n >= 100) {
    result = 'vapor';
} else {
    result = 'water';
}

console.log(result);