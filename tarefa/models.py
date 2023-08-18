from django.db import models


class Tarefa(models.Model):
    #Charfield(): campo de caracteres
    #verbose.name: diz qual nome será exibido
    nome = models.CharField(max_length = 50)
    data = models.DateTimeField()
    
    def __str__(self):
        return self.nome
    