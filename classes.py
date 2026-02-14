class Orcamento:
    def __init__(self, tipo, quartos, garagem, crianca, vagas_extras):
        self.tipo = tipo
        self.quartos = quartos
        self.garagem = garagem
        self.crianca = crianca
        self.vagas_extras = vagas_extras

    def calcular_valor(self):
        valor = 0

        if self.tipo == "casa":
            valor = 900.0 
        elif self.tipo == "apartamento":
            valor = 700.0 
        elif self.tipo == "estudio":
            valor = 1200.0 

        if self.tipo == "apartamento" and self.quartos == 2:
            valor += 200.0 
        elif self.tipo == "casa" and self.quartos == 2:
            valor += 250.0 

        # Regra de Garagem para Casa/Apto
        if (self.tipo in ["casa", "apartamento"]) and self.garagem == 1:
            valor += 300.0
        
        # Regra de Garagem para Estúdio 
        elif self.tipo == "estudio":
            if self.vagas_extras >= 2:
                # 250 pelas duas primeiras + 60 por cada uma além dessas duas
                valor += 250.0 + ((self.vagas_extras - 2) * 60.0)

        # Desconto sem crianças Apartamento 
        if self.tipo == "apartamento" and not self.crianca:
            valor *= 0.95

        return valor
