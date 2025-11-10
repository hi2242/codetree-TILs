const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let result = null;
if (N >= 3000) {
    result = 'book';
} else if (N >= 1000) {
    result = 'mask';
} else if (N >= 500) {
    result = 'pen';
} else {
    result = 'no';
}

console.log(result);