const fs = require('fs');

let input = Number(fs.readFileSync(0).toString().trim());

let result = null;

if (input >= 3000) {
    result = 'book';
} else if (1000 <= input && input < 3000) {
    result = 'mask';
} else {
    result = 'no';
}

console.log(result);