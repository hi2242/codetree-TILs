const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const nums = input.map(Number);
let i = 0;
while (true) {
    if (nums[i] === 0) break;
    console.log(nums[i]);
    i += 1;
}