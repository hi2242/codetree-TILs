const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
let [firstDis, firstTemp] = input[0].split(' ');
let [secondDis, secondTemp] = input[1].split(' ');
let [thirdDis, thirdTemp] = input[2].split(' ');
[firstTemp, secondTemp, thirdTemp] = [Number(firstTemp), Number(secondTemp), Number(thirdTemp)];

let count = 0;
if (firstDis === 'Y' && firstTemp >= 37) {
    count += 1;
}

if (secondDis === 'Y' && secondTemp >= 37) {
    count += 1;
}

if (thirdDis === 'Y' && thirdTemp >= 37) {
    count += 1;
}

if (count >= 2) {
    console.log('E');
} else {
    console.log('N');
}