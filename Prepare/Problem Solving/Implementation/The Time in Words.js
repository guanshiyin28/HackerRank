'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'timeInWords' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER h
 *  2. INTEGER m
 */

function timeInWords(h, m) {
    // Write your code here
    const hoursInWords = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve'
    }

    const minutesInWords = {
        ...hoursInWords,
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty'
    }

    const toMinutes = 60 - m

    if (m === 0) {
        return `${hoursInWords[h]} o' clock`
    } else if (m === 1) {
        return `one minute past ${hoursInWords[h]}`
    } else if (m === 15) {
        return `quarter past ${hoursInWords[h]}`
    } else if (m >= 2 && m <= 20 && m !== 15) {
        return `${minutesInWords[m]} minutes past ${hoursInWords[h]}`
    } else if (m >= 21 && m <= 29) {
        return `twenty ${minutesInWords[m - 20]} minutes past ${hoursInWords[h]}`
    } else if (m === 30) {
        return `half past ${hoursInWords[h]}`
    } else if (m === 45) {
        return `quarter to ${hoursInWords[h === 12 ? 1 : h + 1]}`
    } else if (m === 59) {
        return `one minute to ${hoursInWords[h === 12 ? 1 : h + 1]}`
    } else if (toMinutes > 20) {
        return `twenty ${minutesInWords[toMinutes - 20]} minutes to ${hoursInWords[h === 12 ? 1 : h + 1]}`
    } else {
        return `${minutesInWords[60 - m]} minutes to ${hoursInWords[h === 12 ? 1 : h + 1]}`
    }
}


function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const h = parseInt(readLine().trim(), 10);

    const m = parseInt(readLine().trim(), 10);

    const result = timeInWords(h, m);

    ws.write(result + '\n');

    ws.end();
}
