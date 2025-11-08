const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const [row, column] = input.map(Number);
let line = null;
for (let i = 0; i < row; i += 1) {
    line = '';
    for (let j = 0; j < column; j += 1) {
        line += '* ';
    }
    console.log(line);
}