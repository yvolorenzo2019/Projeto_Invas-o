# variavel m
m = int(input("Digite o número M : "))
# variavel n
n = int(input("Digite o número N : "))
# variavel n números
n_numbers = []
# variavel m números
m_numbers = []
#
ms = 0
# continua é a variavel para verificação da continuidade de adição
continua = ""
# sm é a soma dos m números
sm = 0
# Declaração dos M números
print("-------- Declaração dos M números -----------")
while len(m_numbers) < 999:
    ms = int(input("Digite os M números (Máximo 999) : "))
    m_numbers.append(ms)
    continua = (
        input(
            "Digite S para parar a adição de M números , caso queira continuar use qualquer tecla : "
        )
        .upper()
        .strip()
    )
    if continua == "S":
        break
print("Os m números digitados foram : {}".format(m_numbers))
# fim da declaração dos M números
# ===============================#
# Declaração dos N números
print("-------- Declaração dos N números -----------")
while len(n_numbers) < 999:
    ms = int(input("Digite os N números (Máximo 999) : "))
    n_numbers.append(ms)
    continua = (
        input(
            "Digite S para parar a adição de M números , caso queira continuar use qualquer tecla : "
        )
        .upper()
        .strip()
    )
    if continua == "S":
        break
print("Os n números digitados foram : {}".format(n_numbers))
# fim da declaração dos N números
# #==========================#
# Soma dos números M
for i in m_numbers:
    sm += i

print("A soma dos números (SM) é {0}".format(sm))
# Soma dos digitos dos digitos#
sd = 0
m_numbersDigito = sm
while m_numbersDigito > 0:
    sd += m_numbersDigito % 10
    m_numbersDigito = int(m_numbersDigito / 10)

# Resultado da soma dos digitos#
print("A soma dos digitos (SD) é {0}".format(sd))
vezes = 1
numeros = []
soma = 0
# Verificando se a soma dos digitos é par ou impar e decisão de metodos#
if sd % 2 == 0:
    print("A soma dos digitos é par , então sera usado o metodo A ")
    # Para quando i tiver o tamanho do n_numbers , range + len para poder ler arrays.
    # Contador do multiplicador#
    while n_numbers:
          minimu = n_numbers[0]
          # ---- para quando x estiver em numbers
          for x in n_numbers:
              #Se x for menor que minimu#
                 if x < minimu:
                     #Minimu é igual a x#
                        minimu = x
          numeros.append(minimu*vezes)
          n_numbers.remove(minimu)
          vezes += 1
          soma = 0
          for numero in numeros:
           soma += numero

                            #Metodo B#            
else:
    print("A soma dos digitos é impar , então sera usado o metodo B ")
n1 = 1
n2 = 1
while n_numbers: 
    for x in n_numbers:
        sd = x + n1
        #Separando unidade ultimo digito#
        c = sd // 1 % 10
        #Separando dezena penultimo digito#
        d = sd // 10 % 10
        #Soma dos ultimos digitos#
        soma2 = c + d
        #laço da Soma dos digitos#
        soma += soma2
        #n2 é o número de adição da sequencia#
        n1 = n1 + n2
        n2 += 1
    if x in n_numbers:
        break


#Divisão do resultado da soma#
dia = soma % 31
mes = soma % 12

if   mes == 1 and dia > 0 and dia < 32:
       print('A invasão será no mês de Janeiro no dia {0}'.format(dia))
elif mes == 2 and dia > 0 and dia < 29:
       print('A invasão será no mês de Fevereiro no dia {0}'.format(dia))
elif mes == 3 and dia > 0 and dia < 32:
       print('A invasão será no mês de Março no dia {0}'.format(dia))
elif mes == 4 and dia > 0 and dia < 32:
       print('A invasão será no mês de Abril no dia {0}'.format(dia))
elif mes == 5 and dia > 0 and dia < 32:
       print('A invasão será no mês de Maio no dia {0}'.format(dia))
elif mes == 6 and dia > 0 and dia < 32:
       print('A invasão será no mês de Junho no dia {0}'.format(dia))              
elif mes == 7 and dia > 0 and dia < 32:
       print('A invasão será no mês de Julho no dia {0}'.format(dia))
elif mes == 8 and dia > 0 and dia < 32:
       print('A invasão será no mês de Agosto no dia {0}'.format(dia))
elif mes == 9 and dia > 0 and dia < 32:
       print('A invasão será no mês de Setembro no dia {0}'.format(dia))
elif mes == 10 and dia > 0 and dia < 32:
       print('A invasão será no mês de Outubro no dia {0}'.format(dia))
elif mes == 11 and dia > 0 and dia < 32:
       print('A invasão será no mês de Novembro no dia {0}'.format(dia))
elif mes == 0 and dia > 0 and dia < 32:
       print('A invasão será no mês de Dezembro no dia {0}'.format(dia))
elif mes == 2 and dia >= 29:
       print('o Codigo foi Corrompido')
elif dia >= 32:
       print('o Codigo foi Corrompido')
else:
       print('o Codigo foi Corrompido')
