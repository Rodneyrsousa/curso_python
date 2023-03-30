# pessoa = {
#     'nome': 'Rodney',
#     'sobrenome': 'Rodrigues',
#     'altura': '1.7',
#     'endereco': [
#         {'rua': 'turquesa', 'numero': 169},
    
#     ],
# }

# print(pessoa)
# print(pessoa['sobrenome'])



lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()
    
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)