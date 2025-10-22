const fs = require('fs');

let input = Number(fs.readFileSync(0).toString().trim());

if (input >= 80) {
    console.log('pass');
} else {
    console.log(`${80 - input} more score`);
}