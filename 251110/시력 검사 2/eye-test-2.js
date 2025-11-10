const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const a = Number(input);

let result = null;
if (a >= 1.0) {
    result = 'High';
} else if (a >= 0.5) {
    result = 'Middle';
} else {
    result = 'Low';
}

console.log(result);