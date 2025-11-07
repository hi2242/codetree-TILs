const fs = require('fs');

const input = Number(fs.readFileSync(0).toString().trim());

let result = [];

for (let i = input; i <= 100; i += 1) {
    if (i >= 90) result.push('A');
    else if (i >= 80) result.push('B');
    else if (i >= 70) result.push('C');
    else if (i >= 60) result.push('D');
    else result.push('F');

}
console.log(result.join(' '));