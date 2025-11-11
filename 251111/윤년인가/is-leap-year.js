const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const Y = Number(input);

let result = null;
if (Y % 4 !== 0 || (Y % 100 === 0 && Y % 400 !== 0)) {
    result = 'false';
} else {
    result = 'true';
}
console.log(result);