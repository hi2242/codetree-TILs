const fs = require('fs');

let input = Number(fs.readFileSync(0).toString().trim());

let result = null;

if ((input % 2 === 1 && input % 3 === 0) || input % 10 === 0) {
    result = true;
} else {
    result = false;
}

console.log(result);