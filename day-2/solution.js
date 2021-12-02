let vertical_pos = 0;
let horizontal_pos = 0;

// Include fs module
const fs = require('fs');

// Calling the readFileSync() method
// to read 'input.txt' file
const data = fs.readFileSync('input.txt',
  { encoding: 'utf8', flag: 'r' });

// Display the file data

console.log();

data.split('\n').forEach(line => {
  var [direction, value] = line.split(" ");
  value = Number(value);
  console.log(direction, '=>', value, typeof(value));

  switch (direction) {
    case 'forward':
      horizontal_pos += value;
      return;

    case 'up':
      vertical_pos -= value;
      return;

    case 'down':
      vertical_pos += value;
      return;
    default:
      console.log('problem');
      return;
  }
  console.log('------------');
});

console.log(vertical_pos, horizontal_pos, vertical_pos * horizontal_pos);