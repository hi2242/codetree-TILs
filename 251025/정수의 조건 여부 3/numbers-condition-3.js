const fs = require('fs');

let input = Number(fs.readFileSync(0).toString().trim());

let result = null;

if (input % 13 === 0 || input % 19 === 0) {
    result = 'True';
} else {
    result = 'False';
}

console.log(result);