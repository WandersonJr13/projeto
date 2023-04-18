from django.db import models
from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text='motivo')
    funcionario = models.ForeignKey(Funcionario, models.PROTECT)


    def __str__(self):
        return self.motivo
