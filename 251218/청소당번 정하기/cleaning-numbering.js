const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();

const day = Number(input);

let [classCount, hallCount, bathCount] = [0, 0, 0];

for (let i = 1; i <= day; i += 1) {
    if (i % 12 === 0) {
        bathCount += 1;
    } else if (i % 3 === 0) {
        hallCount += 1;
    } else if (i % 2 === 0) {
        classCount += 1;
    }
}

console.log(classCount, hallCount, bathCount);