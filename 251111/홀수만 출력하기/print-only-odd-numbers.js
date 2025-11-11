const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const nums = input.slice().map(Number);
const N = nums[0];

for (let i = 1; i <= N; i += 1) {
    if (nums[i] % 2 !== 0 && nums[i] % 3 === 0) {
        console.log(nums[i]);
    }
}