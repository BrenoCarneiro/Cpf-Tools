# CPF Tools

## Notas da versão 2.0

Nessa nova versão foi incluída uma interface gráfica através do PySimpleGUI, também é possível copiar o número gerado atráves de um clique no botão de copiar. No momento o aplicativo só foi testado em Windows, caso execute em outro S.O e não tenha os pacotes necessários o aplicativo poderá não funcionar.

![image](https://user-images.githubusercontent.com/102473053/196800880-9a732fdf-c1d3-42be-af66-0cd8f7c4a5c8.png)

## Features

- Gera número de CPF aleatório e totalmente válido 
- Verifica se o número digitado é válido
- Sugere mudança no número verificado caso o mesmo seja inválido
- Informa de qual região o número do documento pertence
- Copiar o número gerado para o clipboard atráves de um simples clique

## Pacotes e módulos

Lista dos pacotes utilizados e a sua utilização no código:

| Pacote | Utilização |
| ------ | ------ |
| os | Instala os pacotes externos caso a máquina não tenha |
| random | Cria um número aleatório  |
| pyperclip | Copia uma variável para o clipboard  |
| pysimplegui | Cria uma janela |


## License

MIT
