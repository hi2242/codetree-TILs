let [a, b, c] = [1, 5, 3];

a = c
a += c
b -= c

console.log([a, b, c].join("\n"));