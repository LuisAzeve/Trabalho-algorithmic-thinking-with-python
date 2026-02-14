from funcoes import *
from classes import *

def apresenta_menu():
    while True:
        menu = input("""
-----------------------------------------------
                     Bem vindo!
-----------------------------------------------

Selecione a opção desejada:
1. Gerar orçamento
0. Sair
""")

        if menu == '1':
            tipo = input("""
Selecione o tipo de orçamento que deseja:
1. Casa
2. Apartamento
3. Estúdio
""")

            if tipo == '1':
                tipo_imovel = "casa"
            elif tipo == '2':
                tipo_imovel = "apartamento"
            elif tipo == '3':
                tipo_imovel = "estudio"
            else:
                print("Opção inválida")
                continue

            quartos = int(input("Quantidade de quartos (1 ou 2): "))
            garagem = int(input("Possui garagem? (1 = sim / 0 = não): "))
            crianca = input("Possui crianças? (s/n): ").lower() == 's'

            vagas_extras = 0
            if tipo_imovel == "estudio":
                vagas_extras = int(input("Quantidade de vagas extras: "))

            orcamento = Orcamento(
                tipo_imovel,
                quartos,
                garagem,
                crianca,
                vagas_extras
            )

            valor = orcamento.calcular_valor()
            print(f"\nValor do aluguel mensal: R$ {valor:.2f}")

            parcelas = int(input("Deseja parcelar o contrato de R$ 2000,00 em quantas vezes? (1 a 5): "))
    
            if parcelas < 1 or parcelas > 5:
                print("Número de parcelas inválido. Usando 1 parcela.")
                parcelas = 1

            
            valor_contrato = 2000.0
            valor_parcela = valor_contrato / parcelas

            print("\n--- RESUMO DO CONTRATO ---")
            print(f"Taxa de Contrato Total: R$ {valor_contrato:.2f}")
            print(f"Parcelamento: {parcelas}x de R$ {valor_parcela:.2f}")
            print(f"Total mensal (Aluguel + Parcela do Contrato): R$ {(valor + valor_parcela):.2f}")
            print("---------------------------\n")

            gerar = input("Deseja gerar o arquivo CSV com as 12 parcelas? (s/n): ").lower()
            if gerar == 's':
                gerar_csv_aluguel(valor, parcelas)

        
        elif menu == '0':
                print("Encerrando aplicação...")
                break


apresenta_menu()