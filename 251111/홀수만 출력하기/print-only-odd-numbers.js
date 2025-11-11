const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const nums = input.map(Number);

for (let i = 0; i < nums.length; i += 1) {
    if (nums[i] % 2 !== 0 && nums[i] % 3 === 0) {
        console.log(nums[i]);
    }
}