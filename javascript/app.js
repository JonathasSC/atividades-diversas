let inputs = []
let negativos = []

for (let cont = 0; cont < 5; cont ++) {
    inputs[cont] = window.prompt('Digite um número: ')
    if (inputs[cont] < 0){
        negativos[cont] = inputs[cont]
    }
}

alert(inputs)
alert(negativos)