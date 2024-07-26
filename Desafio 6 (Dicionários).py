estadoddd = {61:'Brasilia',71:'Salvador',11:'Sao Paulo',21:'Rio de Janeiro',32:'Juiz de Fora',19:'Campinas',27:'Vitoria',31:'Belo Horizonte'}
ddd = int(input("Digite um DDD de um estado brasileiro: "))
for chave, estado in estadoddd.items():
    if ddd == chave:
      print(estadoddd[ddd])
    break
if not print('“DDD não cadastrado”'):