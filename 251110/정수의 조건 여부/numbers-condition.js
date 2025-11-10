const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const a = Number(input);

let result = null;
if (a >= 113) {
    result = 1;
} else {
    result = 0;
}

console.log(result);