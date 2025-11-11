const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [mid, final] = input.map(Number);

let result = null;

if (mid < 90) {
    result = 0;
} else if (final >= 95) {
    result = 100000;
} else if (final >= 90) {
    result = 50000;
} else {
    result = 0;
}

console.log(result);