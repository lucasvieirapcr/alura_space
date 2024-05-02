from datetime import timezone, datetime

from django.contrib.auth.models import User
from django.db import models

class Fotografia(models.Model): #ele vai herdar a biblioteca
    #CRIANDO A LISTA PARA AS TAGS
    OPCOES_CATEGORIAS = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(max_length=50, null=False, blank=False)     #tamanho/se tá em branco/ string vazia
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    categoria = models.CharField(max_length=50, choices= OPCOES_CATEGORIAS, default="")
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", null=False, blank=True)
    publicada = models.BooleanField(default=False)  #quando criar um item, ele não irá ser publicado na mesma hora
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,   #Se o usuario for excluido, ele deleta a foto
        null=True,
        blank=False,
        related_name="user",
    )

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'


