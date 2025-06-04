// Exercício
console.clear()

const readline = require('readline-sync');

const Positivos = [];
const Negativos = [];
numeros = [];
soma = 0

for (let i = 1; i <= 5; i++) {
  numeros = readline.questionInt(`Digite o ${i} numero: `);
  
  if (numeros > 0) {
    soma+=numeros
    Positivos.push(numeros)
  } else {
  Negativos.push(numeros)  
}
}

console.log(`\nQuantidades de numeros positivos: ${Positivos.length}`)
console.log(`\nSoma dos numeros positivos: ${soma}`)