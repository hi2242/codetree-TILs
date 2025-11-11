const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const M = Number(input);

if (M >= 3 && M <= 5) {
    console.log('Spring');
} else if (M >= 6 && M <= 8) {
    console.log('Summer');
} else if (M >= 9 && M <= 11) {
    console.log('Fall');
} else {
    console.log('Winter');
}