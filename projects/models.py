from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    art = models.CharField(max_length=100, blank=True)  # Permitindo vazio

    # Relacionamento com o usuário (autor do projeto)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
        return f"{self.projectName} - {self.responsible} - {self.address} - {self.art}"