// Criando um vetor

const frutas = ['Maracuja', 'Banana', 'Manga']

console.log('Exibindo todos elementos dentro do vetor.')
console.log(frutas)

console.log('Exibindo todos elementos dentro do vetor.')
console.log(frutas[0])
console.log(frutas[2])

console.log('\nAdicionando elemento ao vetor.')
frutas.push('Uvas')
console.log(frutas)

console.log('\nRemovendo o último elemento do vetor.')
frutas.pop()
console.log(frutas)

console.log('\nRemovendo o primeiro elemento do vetor.')
frutas.shift()
console.log(frutas)

console.log('\nPercorrendo o vetor')
frutas.forEach((frutas, index) => {
    console.log(`${++index}: ${frutas}`) 
})
// "++" depois de index, irá apresentar o valor e acrescentar depois