from random import randint
número=randint(0,40)
pessoa=dict()
alunos=list()
while True:
 pessoa.clear()
 pessoa['nome']=str(input('nome:'))
 idade=int(input('idade:'))
 pessoa['idade']=idade
 if idade<6:
   print(f'aluno(a) {pessoa["nome"]} ira para o berçario') 
 else:
   if idade<11:
    print(f' aluno(a) {pessoa["nome"]} ira para o ensino fundamental I')   
   else:
     if idade<=14:
      print(f'aluno(a) {pessoa["nome"]} ira para o fundamental II')
     if idade>14:
       print(f' aluno(a) {pessoa["nome"]} ira para o ensino médio')
     if idade>18:
       print('porém,recomendamos o supletivo')     
 pessoa['turno']=str(input('coloque abaixo seu turno \033[0;33mmanhã \033[0;31mtarde \033[0;36mnoite\033[m\n')).strip().upper()
 print(f'o aluno(a) foi cadastrado')
 pessoa['número']=número=randint(0,40)
 alunos.append(pessoa.copy())
 resposta=str(input('desejar cadastrar mais algum aluno(a)?')).upper()[0]
 if resposta in 'Nn':
   break
 print('')
for m in alunos:
    if m["turno"] in 'MANHÃ':
     print(f'\n,\033[0;33mnome:{m["nome"]},idade:{m["idade"]},turno:{m["turno"]},número:{m["número"]}')
for t in alunos:
    if t["turno"] in 'TARDE':
     print(f'\n,\033[0;31mnome:{t["nome"]},idade:{t["idade"]}turno:{t["turno"]},número:{t["número"]}')
for n in alunos:
    if n["turno"] in 'NOITE':
     print(f'\n,\033[0;36mnome:{n["nome"]},idade:{n["idade"]}turno:{n["turno"]},número:{n["número"]}')
     break
print('obrigado,volte sempre :)')