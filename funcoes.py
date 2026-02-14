import csv

def gerar_csv_aluguel(valor_mensal, parcelas_contrato):
    valor_contrato = 2000.0
    valor_parcela = valor_contrato / parcelas_contrato

    with open("parcelas_aluguel.csv", mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Mês", "Valor"])

        for mes in range(1, 13):
            if mes <= parcelas_contrato:
                total_mes = valor_mensal + valor_parcela
            else:
                total_mes = valor_mensal

            escritor.writerow([mes, f"{total_mes:.2f}"])

    print("Arquivo parcelas_aluguel.csv gerado com sucesso!")


