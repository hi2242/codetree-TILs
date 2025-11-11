const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
let [ageA, genderA] = input[0].split(' ');
let [ageB, genderB] = input[1].split(' ');
[ageA, ageB] = [Number(ageA), Number(ageB)];

if ((ageA >= 19 && genderA === 'M') || (ageB >= 19 && genderB === 'M')) {
    console.log(1);
} else {
    console.log(0);
}