// Include fs module
const fs = require('fs');

const data = fs.readFileSync('input.txt',
  { encoding: 'utf8', flag: 'r' });

function solve_part_1(data) {
  var vertical_pos = 0;
  var horizontal_pos = 0;

  data.forEach(line => {
    var [direction, value] = line.split(" ");
    value = Number(value);

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
        return;
    }
  });

  return [vertical_pos, horizontal_pos];
}


function solve_part_2(data) {
  var aim = 0;
  var horizontal_pos = 0;
  var vertical_pos = 0;

  data.forEach(line => {
    var [direction, value] = line.split(" ");

    value = Number(value);
    switch (direction) {
      case 'up':
        aim -= value;
        return;
      case 'down':
        aim += value;
        return;
      case 'forward':
        horizontal_pos += value;
        vertical_pos += aim * value;
        return;
      default:
        return;
    }

  });

  return [vertical_pos, horizontal_pos];
}

var [v, h] = solve_part_2(data.split('\n'));
console.log(v, h, v * h);