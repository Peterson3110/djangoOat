from django.db import models

class Estoque(models.Model):

    GUITARRA = 'GU'
    VIOLAO = 'VI'
    SOPROS = 'SO'
    ACESSORIOS = 'AC'
    PIANO = 'PI'
    BATERIA = 'BA'
    BAIXO = 'BI'
    ARPAS = 'AR'

    INSTRUMENTOS = [
        (GUITARRA, 'Guitarra'),
        (VIOLAO, 'Violão'),
        (SOPROS, 'Sopros'),
        (ACESSORIOS, 'Acessórios'),
        (PIANO, 'Piano'),
        (BATERIA, 'Bateria'),
        (BAIXO, 'Baixo'),
        (ARPAS, 'Arpas'),
    ]

    instru = models.CharField('Escolha o Produto', max_length=8, choices=INSTRUMENTOS, default=GUITARRA,)
    quantidade = models.BigIntegerField("Quantidade de Produtos")
    endereco = models.CharField('Endereço', max_length=100)
    fornecedor = models.CharField(max_length=100)

    def str(self):
        return self.nome

    def is_upperclass(self):
        return self.instru