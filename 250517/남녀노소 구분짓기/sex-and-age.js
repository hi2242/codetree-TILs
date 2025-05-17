const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split("\n").map(Number);

let [gender, age] = input;

if (gender) {
    if (age >= 19) {
        console.log("WOMAN");
    }
    else {
        console.log("GIRL");
    }
}
else {
    if (age >= 19) {
        console.log("MAN");
    }
    else {
        console.log("BOY");
    }
}