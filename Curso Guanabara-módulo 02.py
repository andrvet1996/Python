#Aula 12-condições aninhadas
nome = str (input ('Qual é o seu nome: '))
if nome == 'Gustavo':
    print ('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print ('Seu nome é bem popular no Brasil!')
elif nome in ('Ana Cláudia Jéssica Julina'):
    print ('Belo nome feminino!')
else:# se vc tirar o else funciona,mas só printa o último print
    print ('Seu nome é bem normal!')
print ('Tenha um bom dia, {}!'.format (nome)) 

#Desafio 36-número de prestações não pode exceder 30% do salário
v = float (input ('Qual o valor da casa que deseja adquirir? R$'))
s = float (input ('Qual é o seu salário? R$'))
t = int (input ('Em quantos anos de financiamento?' ))
valprest = (v / (t * 12))#parcelas mensais
lim30 = (0.3 * s)
if valprest <= lim30:
    print ('O empréstimo para adquirir uma casa de {:.2f}, a ser pago em {} parcelas mensais, no valor de R$ {:.2f} foi APROVADO!'.format (v, t, valprest))
else:
    print ('O empréstimo NÃO FOI APROVADO, pois o valor da prestação ultrapassa 30% de sua renda mensal.')
    
Dsafio 37- conversor de decimal para binário, octal e hexadecimal    
num = int (input ('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO 
[2] converter para OCTAL 
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format (num, bin(num)[2:]))#[2;0] retira algarismos desnecessários
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
