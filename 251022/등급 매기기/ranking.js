const fs = require('fs');

let input = Number(fs.readFileSync(0).toString().trim());

let result = null;

if (input >= 90) {
    result = 'A';
} else if (input >= 80) {
    result = 'B';
} else if (input >= 70) {
    result = 'C';
} else if (input >= 60) {
    result = 'D';
} else {
    result = 'F';
}

console.log(result);