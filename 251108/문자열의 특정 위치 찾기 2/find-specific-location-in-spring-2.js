const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const WORD_LIST = ['apple', 'banana', 'grape', 'blueberry', 'orange'];
let result = [];
WORD_LIST.forEach(word => {
    if (word[2] === input || word[3] === input) {
        result.push(word);
    }
})

if (result.length !== 0) {
    console.log(result.join('\n'));
}
console.log(result.length);