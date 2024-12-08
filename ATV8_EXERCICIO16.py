
#vetor
list_vendedores = []
salario_das_vendas = []
venda = 0
contadores = [0] * 9

while True:
    confirmar = input('Deseja continuar informando? "sim" para continuar ou "nao" para parar ').lower()

    match confirmar:
        case 'sim':
            # para contar quantos vendedores sao
            vendedor = str(input('Informe o nome do vendedor: '))
            list_vendedores.append(vendedor)

            #numero de vezes q vendeu para repetir
            numeros_de_vendas = int(input('Informe quantas vendas foi realizadas: '))
            
            # repete a quantidade de vezes informada
            for c in range(numeros_de_vendas):
                valor_da_venda = float(input('Informe o valor da venda'))
                venda += valor_da_venda

            # calcula o salario mais 9% do bruto
            venda = venda * 0.09
            salario = 200 + venda
            salario_das_vendas.append(salario)


            # // divide inteira por 100(ignora decimal), -2 para ter o indice, 8 para limitar em 8 faixas
            faixa = min(int(salario // 100) - 2, 8)
            
            # soma adiciona 1 vendedor na sua faixa
            contadores[faixa] += 1

        case 'nao':
            print("\nDistribuição de salários:")
            
            # faixa de valores, serve somente para indice, e a minha preguiça de print
            faixas = [
                "$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
                "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999", "$1000 em diante"
            ]
            # percorre a lista e retorna o numero de vendedores na faixa
            for i, contador in enumerate(contadores):
                print(f"{faixas[i]}: {contador} vendedores")
            break


        case _:
            print('Opção incorreta')
