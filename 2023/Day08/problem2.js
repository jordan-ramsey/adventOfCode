import fs from 'fs';
import { start } from 'repl';

const mappingDataExpression = /(?<mapName>\w{3}) = \((?<leftMap>\w{3}), (?<rightMap>\w{3})\)/g;

let mappings = {};
let currentMaps = [];

let input = fs.readFileSync('./input.txt')
    .toString()
    .trim()
    .split('\n\n');

const directions = input[0].split('');
let mappingMatches = [...input[1].matchAll(mappingDataExpression)];

mappingMatches.forEach(match => {
    mappings[match.groups.mapName] = {L: match.groups.leftMap, R: match.groups.rightMap};
    if (match.groups.mapName[2] === 'A') {
        currentMaps.push(match.groups.mapName);
    }
})

let loopCounts = [];

currentMaps.forEach(map => {
    let count = 0;
    while (map[2] !== 'Z') {
        map = mappings[map][directions[count++ % directions.length]]
    }

    loopCounts.push(count);
})

const lcm = loopCounts.reduce((lcm, currentCount) => {
    return calculateLCM(lcm, currentCount)
}, 1);

console.log(lcm);


function calculateLCM(a, b) {
    return ((a * b)/ calculateGCD(a,b))
}
function calculateGCD(a, b) {
    if (b == 0)
      return a;
    else
      return calculateGCD(b, (a % b));
  }


