from django.db import models
from django.db.models.functions import Lower

class RoomName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.IntegerField()

    def __str__(self):
        return f"Id: {self.id}, Nome: {self.name}, Tipo: {self.type}"

    class Meta:
        ordering = [Lower('name')]

class Tue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    power = models.IntegerField()

    def __str__(self):
        return f"Id: {self.id}, Nome: {self.name}, Potência: {self.power}"

    class Meta:
        ordering = [Lower('name')]

class DemandFactor1(models.Model):
    id = models.AutoField(primary_key=True)
    min = models.IntegerField()
    max = models.IntegerField()
    fd1 = models.FloatField()

    def __str__(self):
        return f"Id: {self.id}, Mínimo: {self.min}, Máximo: {self.max}, Fator de demanda 1: {self.fd1}"


class DemandFactor2(models.Model):
    id = models.AutoField(primary_key=True)
    tueNumber = models.IntegerField()
    fd2 = models.FloatField()

    def __str__(self):
        return f"Id: {self.id}, Número de TUEs: {self.tueNumber}, Fator de demanda 2: {self.fd2}"


class Measurements(models.Model):
    id = models.AutoField(primary_key=True)
    demand = models.IntegerField()
    circuitBreaker = models.IntegerField()
    phase = models.IntegerField()
    neutral = models.IntegerField()
    grounding = models.IntegerField()
    conduit = models.IntegerField()
    typePhase = models.IntegerField()

    def __str__(self):
        return f"Id: {self.id}, Demanda: {self.demand}, Disjuntor: {self.circuitBreaker}, Fase: {self.phase}, Neutro: {self.neutral}, Aterramento: {self.grounding}, Eletroduto: {self.conduit}, Tipo de Fase: {self.typePhase}"
