






 #Dicionário com pessoas e suas cores favoritas

cores_favoritas = {
    "Ana": "azul", "Carlos": "verde", "Maria": "vermelho"}

# Solicita o nome da pessoa
nome = input("Digite o nome de uma pessoa: ")

 #Verifica se a pessoa ta no dicionário e ai mostra a cor favorita
if nome in cores_favoritas:
    print(f"A cor favorita de {nome} é {cores_favoritas[nome]}.")
else:
    print(f"Não encontrei a pessoa {nome} no dicionário.")
