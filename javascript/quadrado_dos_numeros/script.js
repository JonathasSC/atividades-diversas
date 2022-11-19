function mostrar() {
    n1 = Number(window.document.getElementById('n1').value)
    n2 = Number(window.document.getElementById('n2').value)
    n3 = Number(window.document.getElementById('n3').value)
    n4 = Number(window.document.getElementById('n4').value)
    n5 = Number(window.document.getElementById('n5').value)

    resposta = window.document.getElementById('resposta')

    resposta.innerHTML = `${n1**2}, ${n2**2}, ${n3**2}, ${n4**2}, ${n5**2}`
}