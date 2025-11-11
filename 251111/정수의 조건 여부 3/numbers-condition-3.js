const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const a = Number(input);

if (a % 13 === 0 || a % 19 === 0) {
    console.log('True');
} else {
    console.log('False');
}