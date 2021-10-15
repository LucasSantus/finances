from typing import ValuesView
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Movimentacao(models.Model):
    conta = ForeignKey(
        'contas.Conta',
        on_delete = models.PROTECT,
        related_name = "movimentacao_conta",
        verbose_name = "Conta em que a movimentação ocorreu"
    )
    
    liquidada = models.BooleanField(
        verbose_name = "Despesa descontada/receita recebida?",
        editable = False,
        default = False,
    )
    
    descricao = models.CharField(
        verbose_name = "Descrição",
        max_length = 50,
    )
    
    valor = models.DecimalField(
        verbose_name = "Valor da movimentação",
        max_digits = 10,
        decimal_places = 2
    )
    
    data = models.DateField(
        verbose_name = "Data da movimentação"
    )

    class Meta:
        db_table = "movimentacao"
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"
        
    def __str__(self):
        return f"R$ {self.valor} | {self.conta}"