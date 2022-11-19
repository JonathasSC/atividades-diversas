function calcular() {
    var n1 = Number(window.document.getElementById('nota1').value)
    var n2 = Number(window.document.getElementById('nota2').value)
    var n3 = Number(window.document.getElementById('nota3').value)
    
    var text = window.document.getElementById('resultado')

    var resultado = ( n1 + n2 + n3 )/ 3

    text.innerHTML = `${resultado}`
}
