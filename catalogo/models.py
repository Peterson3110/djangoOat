from django.db import models

class Catalogo(models.Model):

    GUITARRA = 'GU'
    VIOLAO = 'VI'
    SOPROS = 'SO'
    ACESSORIOS = 'AC'
    PIANO = 'PI'
    BATERIA = 'BA'
    BAIXO = 'BI'
    ARPAS = 'AR'

    INSTRUMENTOS = [
        (GUITARRA,'Guitarra'),
        (VIOLAO,'Violão'),
        (SOPROS,'Sopros'),
        (ACESSORIOS,'Acessórios'),
        (PIANO,'Piano'),
        (BATERIA,'Bateria'),
        (BAIXO,'Baixo'),
        (ARPAS,'Arpas'),
    ]
    instru = models.CharField('Escolha o Produto',max_length=8,choices=INSTRUMENTOS,default=GUITARRA,)
    marca = models.CharField('Marca (opcional)',max_length=100)
    modelo = models.CharField('Modelo (opcional)',max_length=100)

    def is_upperclass(self):
        return self.instru

    def str (self):
        return self.nome