const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const N = Number(input);

let result = null;
if (N >= 80) {
    result = 'pass';
} else {
    result = `${80 - N} more score`;
}
console.log(result);