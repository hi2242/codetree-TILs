const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();

let result = null;
if (input === 'S') {
    result = 'Superior';
} else if (input === 'A') {
    result = 'Excellent';
} else if (input === 'B') {
    result = 'Good';
} else if (input === 'C') {
    result = 'Usually';
} else if (input === 'D') {
    result = 'Effort';
} else {
    result = 'Failure';
}

console.log(result);