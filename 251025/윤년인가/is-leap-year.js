const fs = require('fs');

let input = Number(fs.readFileSync(0).toString().trim());
let result = null;
if (input % 4 === 0) {
    result = true;
    if (input % 100 === 0 && input % 400 !== 0) {
        result = false;
    }
} else {
    result = false;
}

console.log(result);