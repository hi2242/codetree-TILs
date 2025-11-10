const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let result = null;
if (N >= 90) {
    result = 'A';
} else if (N >= 80) {
    result = 'B';
} else if (N >= 70) {
    result = 'C';
} else if (N >= 60) {
    result = 'D';
} else {
    result = 'F';
}

console.log(result);