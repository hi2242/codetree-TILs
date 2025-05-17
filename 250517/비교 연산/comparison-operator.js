const fs = require("fs");

let input = fs.readFileSync(0).toString().trim().split(" ");

let [A, B] = input.map(Number);

if (A >= B) {
    console.log(1);
}
else {
    console.log(0);
}

if (A > B) {
    console.log(1);
}
else {
    console.log(0);
}

if (B >= A) {
    console.log(1);
}
else {
    console.log(0);
}

if (B > A) {
    console.log(1);
}
else {
    console.log(0);
}

if (A == B) {
    console.log(1);
    console.log(0);
}
else {
    console.log(0);
    console.log(1);
}