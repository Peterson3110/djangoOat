from django.db import models

class Usuario(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.BigIntegerField(max_length=14)
    endereco = models.CharField('Endereço', max_length=100)
    nascimento = models.DateField('Data de Nascimento',max_length=8)
    senha = models.CharField('Senha',max_length=8)
    senha1 = models.CharField('Confirme sua senha',max_length=8)

    def str (self):
        return self.nome