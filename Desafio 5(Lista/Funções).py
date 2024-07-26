#Dada a lista (1,3,2,3,4,5,1,5,7,6,8,3,4), crie uma segunda lista apenas com os itens na mesma ordem, mas sem repetição.
lista1 = [1,3,2,3,4,5,1,5,7,6,8,3,4]
elementos = list(set(lista1))
print(elementos)