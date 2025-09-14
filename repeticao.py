import random

def main():
    numeros = lista()
    contar(numeros)
            
def lista():
	numeros_sorteados = [] #Cria uma lista vazia que será usada para armazenar os números aleatórios 
	for i in range(5):
		numeros_sorteados.append(random.randint(1,10)) #Sorteia 5 numeros entre 1 a 10 e os adiciona na lista
	print(numeros_sorteados)
	return numeros_sorteados
                                        
def contar(lista_n):
	mais_repetido = 0 #Inicializa a variável que armazenará o número mais repetido
	mais_de_um = False #Inicializa a variável que verificará se mais de um número repetiu mais de uma vez
	for num in lista_n:
		if lista_n.count(num) > lista_n.count(mais_repetido): #Se o número atual aparecer mais vezes na lista do que o armazenado em mais_repetido... 
			mais_repetido = num #O número começa a ser armazenado em mais_repetido
		elif lista_n.count(num) == lista_n.count(mais_repetido) and num != mais_repetido and lista_n.count(num) > 1: #Senão, se o número atual aparecer o mesmo tanto de vezes que o mais_repetido... 
			mais_de_um = True #Existe mais de um número que se repete
	if mais_de_um:
		print(f"Mais de um número se repetiu {lista_n.count(mais_repetido)} vezes!")
	elif lista_n.count(mais_repetido) > 1:
		print(f"O número mais repetido foi {mais_repetido}, aparecendo {lista_n.count(mais_repetido)} vezes!")
	else:
		print("Nenhum número se repetiu!")
                                                                                                                                        
main()