from random import randint
from copy import deepcopy


total_cartelas = 15
total_palavras_por_catela = 16


palavras = []
with open('palavras.txt', "r") as f:
	palavras = [line.rstrip() for line in f] 

for crianca in range(total_cartelas):
    palavras2 = deepcopy(palavras)
    for numero in range(total_palavras_por_catela):
        palavra_selecionada = palavras2[randint(1, len(palavras2)-1)]
        palavras2.remove(palavra_selecionada)
        print(palavra_selecionada)
    print(40 * '==')
    palavras2 = deepcopy(palavras)
