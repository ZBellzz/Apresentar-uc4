list_vendedores = []
salario_das_vendas = []
venda = 0


while True:
    confirmar = input('Deseja continuar informando? "sim" para continuar ou "nao" para parar ').lower()

    match confirmar:
        case 'sim':
            vendedor = float(input('Informe o nome do vendedor: '))
            list_vendedores.append(vendedor)

            numeros_de_vendas = int(input('Informe quantas vendas foi realizadas: '))
            
            for c in range(0,numeros_de_vendas +1):
                valor_da_venda = float(input('Informe o valor da venda'))
                venda += valor_da_venda

            venda = venda * 0.09
            salario = 200 + venda
            salario_das_vendas.append(salario)




        case 'nao':
            
            if salario_das_vendas[0 :-1] < 299:
                vv =len(salario_das_vendas)
                

                print()



            break

        case _:
            print('Opção incorreta')
