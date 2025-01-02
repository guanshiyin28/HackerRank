'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

class Node {
    constructor() {
        this.data = [];
        this.children = {};
    }
}

class Tree {
    constructor(genes, health) {
        this.root = new Node();
        for (let i = 0; i < genes.length; i++) {
            this.insert(genes[i], i, health[i]);
        }
    }

    insert(gene, index, health) {
        let node = this.root;
        for (const char of gene) {
            node.children[char] = node.children[char] || new Node();
            node = node.children[char];
        }
        node.data.push([index, health]);
    }

    getHealth(first, last, d) {
        let health = 0;
        for (let i = 0; i < d.length; i++) {
            health += this._getSubStrHealth(this.root, first, last, d, i);
        }
        return health;
    }

    _getSubStrHealth(node, first, last, d, index) {
        let health = 0;
        while (node) {
            node = node.children[d[index]];
            const data = node?.data || [];

            let j = binarySearch(data, first);
            while (j < data.length && data[j][0] <= last) {
                health += data[j][1];
                j++;
            }

            index++;
        }
        return health;
    }
}

function binarySearch(data, index) {
    let left = 0;
    let right = data.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (index > data[mid][0]) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return left;
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const genes = readLine().replace(/\s+$/g, '').split(' ');

    const health = readLine().replace(/\s+$/g, '').split(' ').map(healthTemp => parseInt(healthTemp, 10));

    const s = parseInt(readLine().trim(), 10);

    const tree = new Tree(genes, health);

    let minHealth = Infinity;
    let maxHealth = -Infinity;

    for (let sItr = 0; sItr < s; sItr++) {
        const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

        const first = parseInt(firstMultipleInput[0], 10);

        const last = parseInt(firstMultipleInput[1], 10);

        const d = firstMultipleInput[2];
        const health = tree.getHealth(parseInt(first, 10), parseInt(last, 10), d);

        minHealth = Math.min(minHealth, health);
        maxHealth = Math.max(maxHealth, health);
    }

    console.log(`${minHealth} ${maxHealth}`);
}
