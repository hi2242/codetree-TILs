const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [mathA, englishA] = input[0].split(' ').map(Number);
const [mathB, englishB] = input[1].split(' ').map(Number);

let result = null;
if (mathA > mathB) {
    result = 'A';
} else if (mathB > mathA) {
    result = 'B';
} else if (englishA > englishB) {
    result = 'A';
} else {
    result = 'B';
}
console.log(result);