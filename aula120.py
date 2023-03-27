#CRIAÇÃO DE TIPO DE DADO DICIONÁRIO
pessoa = {}

#CRIAÇÃO DE CHAVE
#pessoa ['nome'] = 'Francisco das Chagas'
chave = 'nome'

#ACESSO A CHAVE
pessoa [chave] = 'Francisco das Chagas'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])
print(pessoa)

#ALTERAÇÃO DE CHAVE

pessoa [chave] = 'Maria das Graças'

#EXCLUSÃO DE CHAVE

del pessoa['sobrenome']
