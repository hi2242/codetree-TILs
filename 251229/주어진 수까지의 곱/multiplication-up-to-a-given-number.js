const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const [A, B]= input.split(' ').map(Number);

let result = 1;

for (let i = A; i <= B; i += 1) {
    result *= i;    
}

console.log(result);