'use strict';

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
 * Complete the 'matrixRotation' function below.
 *
 * The function accepts following parameters:
 *  1. 2D_INTEGER_ARRAY matrix
 *  2. INTEGER r
 */

const DirSteps = {
    R: [0,1],
    D: [1,0],
    L: [0,-1],
    U: [-1,0]
}

function getLayerArrayFromMatrix(matrix, start, w, h) {
    let topArr = Array(w-1).fill(null).map(() => 'R');
    let rightArr = Array(h-1).fill(null).map(() => 'D');
    let bottomArr = Array(w-1).fill(null).map(() => 'L');
    let leftArr = Array(h-1).fill(null).map(() => 'U');
    
    let array = topArr.concat(rightArr).concat(bottomArr).concat(leftArr);
    
    let cur = start;
    for(let i=0; i<array.length; i++) {
        const dir = array[i];
        array[i] = matrix[cur[0]][cur[1]];
        cur[0] += DirSteps[dir][0];
        cur[1] += DirSteps[dir][1];
    }

    return array;
}

function rotateArray(array, steps) {
    const w = array.length;
    const k = steps % w;
    
    let result = Array(w).fill(null).map(() => null);
    for(let i=0; i<w; i++) {
        const new_idx = (w+i-k) % w;
        result[new_idx] = array[i];
    }
    
    return result;
}

function putLayerArrayToMatrix(array, matrix, start, w, h) {
    let topArr = Array(w-1).fill(null).map(() => 'R');
    let rightArr = Array(h-1).fill(null).map(() => 'D');
    let bottomArr = Array(w-1).fill(null).map(() => 'L');
    let leftArr = Array(h-1).fill(null).map(() => 'U');
    
    let dirArray = topArr.concat(rightArr).concat(bottomArr).concat(leftArr);
    
    let cur = start;
    for(let i=0; i<dirArray.length; i++) {
        const dir = dirArray[i];
        matrix[cur[0]][cur[1]] = array[i];
        cur[0] += DirSteps[dir][0];
        cur[1] += DirSteps[dir][1];
    }
}

function printMatrix(matrix) {
    for(let i=0; i<matrix.length; i++) {
        let row = [];
        for(let j=0; j<matrix[0].length; j++) {
            row.push(matrix[i][j]);
        }
        console.log(row.join(' '));
    }
}

function matrixRotation(matrix, r) {
    // Write your code here
    let height = matrix.length;
    let width = matrix[0].length;
    
    let i =0;
    while(height>0 && width>0) {
        let start = [i, i];
        let layerArr = getLayerArrayFromMatrix(matrix, start, width, height);
        let rotatedArr = rotateArray(layerArr, r);
        putLayerArrayToMatrix(rotatedArr, matrix, start, width, height)
        i++;
        width-=2;
        height-=2;
    }

    printMatrix(matrix);
}

function main() {
    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const m = parseInt(firstMultipleInput[0], 10);

    const n = parseInt(firstMultipleInput[1], 10);

    const r = parseInt(firstMultipleInput[2], 10);

    let matrix = Array(m);

    for (let i = 0; i < m; i++) {
        matrix[i] = readLine().replace(/\s+$/g, '').split(' ').map(matrixTemp => parseInt(matrixTemp, 10));
    }

    matrixRotation(matrix, r);
}
