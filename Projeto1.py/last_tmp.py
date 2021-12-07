crianças=list()
bebê=dict()
orfãos=list()
resposta=cont=pergunta=0
#programa usado para cadastro de criança recém nascida
while True:
 bebê.clear()
 bebê['nome']=str(input('nome da criança:'))
 cont+=1
 while True:
  bebê['sexo']=str(input('sexo [F/M]:'))
  if  bebê['sexo'] in 'FfmM':
     break
 pergunta=str(input(f'({bebê["nome"]} tem pais?[S/N]')).upper()[0]
 if pergunta=='N':
   orfãos.append(bebê.copy())
 if pergunta=='S':
   bebê['pais']=str(input(f'nome dos responsaveis de {bebê["nome"]}\n'))  
   crianças.append(bebê.copy())
 resposta=str(input('continuar?[N/S]')).upper()[0]
 if resposta in 'SN':
    print('Continuando...')     
 if resposta=='N':
    break
print(f'total de cadastros{cont}')
print(f'os orfãos são{orfãos}')
print(f'as crianças com pais\n{crianças}')