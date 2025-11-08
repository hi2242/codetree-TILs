const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const nums = input.map(Number);
let i = 0
while (true) {
    if (nums[i] < 25) console.log('Higher');
    else if (nums[i] > 25) console.log('Lower');
    else {
        console.log('Good');
        break;
    }
    i += 1;
}