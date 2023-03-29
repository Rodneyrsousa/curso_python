# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome':'Maria',
    'sobrenome': 'Rodrigues',
    #'idade': 900,

}

#print(pessoa)
#print(len(pessoa))
#print(list(pessoa.keys()))
print(list(pessoa.values()))
#print(list(pessoa.items()))
#pessoa.setdefault('idade', 0)
#print(pessoa['idade'])

#print(pessoa.get('nome', 'Não existe'))

# pessoa.update({
#     'sobrenome': 'Rodrigues de Sousa',
# })
pessoa.update(sobrenome = 'novo valor')
print(pessoa)