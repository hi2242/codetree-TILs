const fs = require("fs");

let temp = Number(fs.readFileSync(0).toString().trim());

if (temp < 0) {
    console.log("ice");
}
else if (temp > 100) {
    console.log("vapor");
}
else {
    console.log("water");
}