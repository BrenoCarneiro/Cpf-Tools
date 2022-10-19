try:
    import os
    import PySimpleGUI as sg
    import pyperclip 
except ImportError:
    print("Instalando pacotes, em alguns instantes o aplicativo será iniciado...\n")
    os.system('python -m pip install pyperclip')
    os.system('python -m pip install PySimpleGUI')
finally:
    import PySimpleGUI as sg
    import random
    import pyperclip
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
            return 'CPF emitido em Rio Grande do Sul.'
        case 1:
            return 'CPF emitido em um desses estados: Distrito Federal, Goiás,\nMato Grosso, Mato Grosso do Sul, Tocantins.'
        case 2:
            return 'CPF emitido em um desses estados: Pará, Amazonas, Acre,\nAmapá, Rondônia, Roraima.'
        case 3:
            return 'CPF emitido em um desses estados: Ceara, Maranhão, Piauí.'    
        case 4:
            return 'CPF emitido em um desses estados: Pernambuco,\nRio Grande do Norte, Paraíba, Alagoas.'
        case 5:
            return 'CPF emitido no estado da Bahia ou Sergipe.'    
        case 6:
            return 'CPF emitido no estado de Minas Gerais.'
        case 7:
            return 'CPF emitido no estado do Rio de Janeiro ou Espírito Santo.'
        case 8:
            return 'CPF emitido no estado de São Paulo.'    
        case 9:
            return 'CPF emitido no estado do Paraná ou Santa Catarina.'
def cpfAleatorio():
    cpf = str(random.randint(10000000000,99999999999))
    cpf = validador(cpf)
    cpf = "".join([str(i) for i in cpf])
    return cpf

layout = [
    [sg.Text("Seja bem vindo(a) ao CPF Tools!\n", justification="center")],
    [sg.Text("Escolha uma opção abaixo:")],
    [sg.InputText("", key="cpf_tela"), sg.Button("Copiar")],
    [sg.Button("Gerar CPF Aleatório"), sg.Button("Validar CPF")],
    [sg.Text("", key="mensagem")]
]

janela = sg.Window("CPF Tools", layout)
while True:
    evento, valor = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == "Gerar CPF Aleatório":
        janela["cpf_tela"].update(cpfAleatorio())
        janela["mensagem"].update("CPF Gerado com sucesso!")
    if evento == "Validar CPF":
        cpf = valor["cpf_tela"].replace(".", "").replace("-","")
        if len(cpf) == 11 and cpf.isnumeric():
            cpfCheck = [str(i) for i in cpf]
            if cpfCheck == validador(cpf):
                janela["mensagem"].update(f"O CPF {cpf} é um número de documento válido!\n{regiaoCpf(cpf)}")
            else:
                cpfInteiroJoin= "".join(validador(cpf))
                janela["mensagem"].update(f"O CPF {cpf} informado é inválido!\nPara ser válido ele deveria conter os últimos dois dígitos: {cpfInteiroJoin[9:11]}\nComo no exemplo: {cpfInteiroJoin}")    
        else:
            janela["mensagem"].update("Formato do CPF inválido!")
    if evento == "Copiar":
        pyperclip.copy(valor["cpf_tela"])
        janela["mensagem"].update("CPF copiado com sucesso!")
janela.close()
