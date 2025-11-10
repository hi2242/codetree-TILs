const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [mathA, englishA] = input[0].split(' ').map(Number);
const [mathB, englishB] = input[1].split(' ').map(Number);

if (mathA > mathB && englishA > englishB) {
    console.log(1);
} else {
    console.log(0);
}