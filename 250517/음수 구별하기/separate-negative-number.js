const fs = require("fs");

let N = Number(fs.readFileSync(0).toString().trim());

if (N >= 0) {
    console.log(N)
}
else {
    console.log(N)
    console.log("minus")
}