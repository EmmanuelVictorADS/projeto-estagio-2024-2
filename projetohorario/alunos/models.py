from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    idAluno = models.AutoField(primary_key=True)
    nomeAluno = models.CharField(max_length=100)
    serie = models.CharField(max_length=50)
    turma = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionando com o usuário

class Formulario(models.Model):
    idFormulario = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)  # Cada formulário pertence a um aluno
    resposta = models.TextField()
    numQuestao = models.IntegerField()
    observacao = models.TextField(blank=True, null=True)

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    bimestre = models.IntegerField()
    nota = models.DecimalField(max_digits=5, decimal_places=2)

class Horario(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    dia = models.CharField(max_length=20)
    hora = models.TimeField()
    materia = models.CharField(max_length=50)
