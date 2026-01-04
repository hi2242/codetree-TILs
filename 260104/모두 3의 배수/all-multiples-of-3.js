const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const numberList = input.split('\n').map(Number);
let result = 1;

numberList.some(number => {
    if (number % 3 !== 0) {
        result = 0;
        return true;
    } else {
        return false;
    }
})

console.log(result);