from django.db import models

class Pagamento(models.Model):

    DEBITO = 'DE'
    CREDITO = 'CR'

    nome = models.CharField('Nome do Titular', max_length=100)
    cpf = models.IntegerField('CPF')
    numero = models.BigIntegerField('Número do cartão')
    data = models.DateField('Data de Validade', max_length=6)
    cvv = models.IntegerField('CVV')
    DEB_CHOICES = [(DEBITO, 'Débito'), (CREDITO, 'Crédito'), ]
    deb = models.CharField('Débito ou Crédito',max_length=2, choices=DEB_CHOICES, default=DEBITO, )

    def str (self):
        return self.nome

    def is_upperclass(self):
        return self.deb