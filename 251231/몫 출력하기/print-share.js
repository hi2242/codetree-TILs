const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const numberList = input.split('\n').map(Number);
let [index, count] = [0, 0];

while (true) {
    if (numberList[index] % 2 === 0) {
        count += 1;
        console.log(numberList[index] / 2);
    }

    if (count === 3) {
        break;
    }

    index += 1;
}