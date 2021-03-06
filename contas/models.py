from django.db import models
from movimentacoes.models import Tipo as TipoMovimentacao

class Tipo(models.IntegerChoices):
    SALARIO = 1, "Conta Salário"
    CORRENTE = 2, "Conta Corrente"
    POUPANCA = 3, "Conta Poupança"

class Conta(models.Model):
    nome = models.CharField(
        verbose_name="Nome da conta",
        max_length=50,
    )
    
    tipo = models.IntegerField(
        choices = Tipo.choices,
        default = Tipo.CORRENTE,
        verbose_name="Tipo de conta"
    )
    
    saldo = models.DecimalField(
        verbose_name="Saldo da conta",
        max_digits=12,
        decimal_places=2,
        default=0.0,
    )
    
    def liquidar_movimentacao(self, tipo_movimentacao, valor):
        if tipo_movimentacao == TipoMovimentacao.RECEITA:
            self.saldo += valor
        elif tipo_movimentacao == TipoMovimentacao.DESPESA:
            self.saldo -= valor
        
    
    class Meta:
        db_table = "conta"
        verbose_name = "Conta"
        verbose_name_plural = "Contas"
        
    def __str__(self):
        return self.nome