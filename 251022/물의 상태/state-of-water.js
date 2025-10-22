const fs = require('fs');

let input = Number(fs.readFileSync(0).toString().trim());

let result = null;
if (input < 0) {
    result = 'ice';
} else if (input >= 100) {
    result = 'vapor';
} else {
    result = 'water';
}

console.log(result);