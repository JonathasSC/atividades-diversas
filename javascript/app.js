var inputs = []
var negativos = []
var lista1 = window.document.getElementById('n1')
var lista2 = window.document.getElementById('n2')

for (cont = 0; cont < 5; cont ++) {
    inputs[cont] = window.prompt('Digite um número: ')
    if (inputs[cont] < 0){
        negativos[cont] = inputs[cont]
    }
}

lista1.innerHTML = inputs
lista2.innerHTML = negativos