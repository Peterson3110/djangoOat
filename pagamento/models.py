from django.db import models

class Pagamento(models.Model):

    DEBITO = 'DE'
    CREDITO = 'CR'

    nome = models.CharField('Nome do Titular', max_length=100)
    cpf = models.IntegerField('CPF', max_length=11)
    numero = models.BigIntegerField('Número do cartão', max_length=16)
    data = models.DateField('Data de Validade', max_length=6)
    cvv = models.IntegerField('CVV', max_length=3)
    DEB_CHOICES = [(DEBITO, 'Débito'), (CREDITO, 'Crédito'), ]
    deb = models.CharField('Débito ou Crédito',max_length=2, choices=DEB_CHOICES, default=DEBITO, )

    def str (self):
        return self.nome

    def is_upperclass(self):
        return self.deb