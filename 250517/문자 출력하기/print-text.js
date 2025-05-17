const fs = require("fs");

let input = fs.readFileSync(0).toString().trim();

for (let i = 0; i < 8; i++) {
    process.stdout.write(input);
}