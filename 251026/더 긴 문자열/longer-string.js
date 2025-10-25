const fs = require('fs');

let input = fs.readFileSync(0).toString().trim().split(' ');
let result = null;
const [firstLength, secondLength] = input.map(each => each.length);

if (firstLength === secondLength) {
     result = 'same';
} else if (firstLength < secondLength) {
     result = `${input[1]} ${secondLength}`;
} else {
     result = `${input[0]} ${firstLength}`;
}

console.log(result);