from django.db import models, transaction

class Tipo(models.IntegerChoices):
    RECEITA = 1, "Receita"
    DESPESA = 2, "Despesa"

class Categoria(models.Model):
    nome = models.CharField(
        verbose_name = "Nome da categoria",
        max_length = 80,
    )
    
    tipo = models.IntegerField(
        choices = Tipo.choices,
        default = Tipo.DESPESA,
        verbose_name="Tipo da categoria"
    )
    
    class Meta:
        db_table = "categoria"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        
    def __str__(self):
        return self.nome
    
class Movimentacao(models.Model):
    tipo = models.IntegerField(
        choices = Tipo.choices,
        default = Tipo.DESPESA,
        verbose_name="Tipo da Movimentação"
    )
        
    conta = models.ForeignKey(
        'contas.Conta',
        on_delete = models.PROTECT,
        related_name = "conta_movimentacao",
        verbose_name = "Conta em que a movimentação ocorreu"
    )
    
    categoria = models.ForeignKey(
        'movimentacoes.Categoria',
        on_delete = models.PROTECT,
        related_name = "categoria_movimentacao",
        verbose_name = "Categoria em que a movimentação ocorreu"
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
    
    def save(self, *args, **kwargs):
        if not self.liquidada:
            try:
                with transaction.atomic():
                    self.conta.liquidar_movimentacao(
                        self.tipo, self.valor
                    )
                    self.conta.save()
                    self.liquidada = True
            except Exception:
                raise Exception(
                    "Ocorreu uma falha. Por favor, tente novamente mais tarde"
                )
        super(Movimentacao, self).save(*args, **kwargs)

    class Meta:
        db_table = "movimentacao"
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"
        
    def __str__(self):
        return f"R$ {self.valor} | {self.conta}"