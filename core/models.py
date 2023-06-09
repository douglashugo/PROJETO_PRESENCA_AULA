from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Presenca(models.Model):
    nome_aluno = models.CharField(max_length=100)
    nome_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_aluno
