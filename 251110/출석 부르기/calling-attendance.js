const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const num = Number(input);

let result = null;
if (num === 1) {
    result = 'John';
} else if (num === 2) {
    result = 'Tom';
} else if (num === 3) {
    result = 'Paul';
} else {
    result = 'Vacancy';
}

console.log(result);