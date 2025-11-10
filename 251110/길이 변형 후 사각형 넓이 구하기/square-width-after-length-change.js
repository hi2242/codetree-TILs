const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
let [width, height] = input.map(Number);
width += 8;
height *= 3;

console.log(`${width}
${height}
${width * height}`);