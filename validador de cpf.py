import random

def validador(cpf):
    cpfInteiro = [int(i) for i in cpf]
    digito1 = 0
    digito2 = 0
    multiplicador1 = 10
    multiplicador2 = 11
    for i in cpfInteiro[0:9]:
        calc1 = (i*multiplicador1)
        digito1 += calc1
        multiplicador1 -= 1
    if (digito1 % 11) >= 2:
        digito1 = 11 - (digito1 % 11)
        cpfInteiro[9] = digito1
     
    else:
        digito1 = 0
        cpfInteiro[9] = digito1

    for i in cpfInteiro[0:10]:
        calc2 = (i*multiplicador2)
        digito2 += calc2
        multiplicador2 -= 1
    if (digito2 % 11) >= 2:
        digito2 = 11 - (digito2 % 11)
        cpfInteiro[10] = digito2
    
    else:
        digito2 = 0
        cpfInteiro[10] = digito2
    cpfInteiro = [str(i) for i in cpfInteiro]
    return cpfInteiro

def regiaoCpf(cpf):
    idRegiaoCpf = [int(i) for i in cpf]
    match idRegiaoCpf[8]:
        case 0:
            return 'e foi emitido no estado do RS'
        case 1:
            return 'e foi emitido em um desses estados: DF, GO, MT, MS, TO'
        case 2:
            return 'e foi emitido em um desses estados: PA, AM, AC, AP, RO, RR'
        case 3:
            return 'e foi emitido em um desses estados: CE, MA, PI'    
        case 4:
            return 'e foi emitido em um desses estados: PE, RN, PB, AL'
        case 5:
            return 'e foi emitido no estado da BA ou SE'    
        case 6:
            return 'e foi emitido no estado de MG'
        case 7:
            return 'e foi emitido no estado do RJ ou ES'
        case 8:
            return 'e foi emitido no estado de SP'    
        case 9:
            return 'e foi emitido no estado do PR ou SC'

def cpfAleatorio():
    cpf = str(random.randint(10000000000,99999999999))
    cpf = validador(cpf)
    cpf = [str(i) for i in cpf]
    return cpf
        
opcao = '1'
print('Seja bem vindo(a)!')
while opcao == '1' or opcao == '2':    
    opcao = input("\nDigite o número da opção que deseja: \n 1 - Validador de CPF \n 2 - Gerador de CPF aleatório \n 3 - Encerrar o programa \n ->")
    match opcao:
        case '1':
            resposta = "SIM"
            while resposta == "SIM":
                cpf = input('\nDigite o CPF: ').replace(".", "").replace("-","")
                if len(cpf) == 11 and cpf.isnumeric():
                    cpfCheck= [str(i) for i in cpf]
                    if cpfCheck == validador(cpf):
                        print(f"\nO CPF {cpf} é um número de documento válido {regiaoCpf(cpf)}")          
                        resposta = input("Deseja verificar outro CPF? Digite SIM ou NAO para retornar ao menu inicial. \n ->").upper()
                    else:
                        cpfInteiroJoin= "".join(validador(cpf))
                        print(f"\nO CPF {cpf} informado é inválido, para ser valido o mesmo deveria conter os últimos dois dígitos: {cpfInteiroJoin[9:11]}, como no exemplo: {cpfInteiroJoin}")
                        resposta = input("Deseja verificar novamente? Digite SIM ou NAO para retornar ao menu \n ->").upper()
                else:
                    resposta = input("Formato do CPF inválido. Deseja tentar novamente? Digite SIM ou NAO para retornar ao menu inicial. \n ->").upper()
        case '2':
            resposta = "SIM"
            while resposta == "SIM":
                print('\nCPF Gerado com sucesso: ' + "".join(cpfAleatorio()))
                resposta = input("Deseja gerar um novo CPF? Digite SIM ou NAO para retornar ao menu incial. \n ->").upper()

        case default:
            break