#!/usr/bin/node

function calculateFactorial(n) {
    if (isNaN(n)) {
      return 1; 
    } else if (n <= 1) {
      return 1; 
    } else {
      return n * calculateFactorial(n - 1);
    }
  }
  
  const args = process.argv.slice(2);
  const num = parseInt(args[0]);
  
  const factorial = calculateFactorial(num);
  console.log(`The factorial of ${num} is: ${factorial}`);