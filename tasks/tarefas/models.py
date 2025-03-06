from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    quilometragem = models.IntegerField()

    def __str__(self):
        return f"{self.modelo} - {self.placa}"

class Servico(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_servico = models.DateField(auto_now_add=True)
    proxima_manutencao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.veiculo}"
