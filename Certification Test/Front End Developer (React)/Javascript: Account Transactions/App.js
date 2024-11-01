'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding("ascii");
let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (chunk) {
    inputString += chunk;
});
process.stdin.on("end", function () {
    inputString = inputString.split('\n');
    main();
});

function readLine() {
  return inputString[currentLine++];
}

class Account {
  constructor(initialBalance)  
 {
    this.balance = initialBalance;
  }

  debit(amount) {
    if (amount > this.balance) {
      return false; // Insufficient funds
    }
    this.balance -= amount;
    return true; // Successful debit
  }

  credit(amount) {
    this.balance += amount;
  }

  getBalance() {
    return this.balance;
  }
}


function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    
    const initialBalance = parseInt(readLine().trim());
    const accountObj = new Account(initialBalance);
    ws.write(`Account created with initial balance of ${initialBalance}\n`);
    
    let numberOfOperations = parseInt(readLine().trim());
    while (numberOfOperations-- > 0) {
        const inputs = readLine().trim().split(' ');
        const operation = inputs[0];
        const amount = parseInt(inputs[1]);

        switch(operation) {
            case 'Debit':
                if (accountObj.debit(amount)) {
                    ws.write(`${amount} debited\n`);
                } else {
                    ws.write(`Insufficient balance\n`);
                }
                break;
            case 'Credit':
                accountObj.credit(amount);
                ws.write(`${amount} credited\n`);
                break;
            case 'GetBalance':
                const currentBalance = accountObj.getBalance();
                ws.write(`Current balance is ${currentBalance}\n`);
            default:
                break;
        }
    }
    ws.end();
}
