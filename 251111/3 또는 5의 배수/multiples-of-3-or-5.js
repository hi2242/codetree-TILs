const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const A = Number(input);

if (A % 3 === 0) {
    console.log('YES');
} else {
    console.log('NO');
}

if (A % 5 === 0) {
    console.log('YES');
} else {
    console.log('NO');
}