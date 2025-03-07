from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="veiculos")
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    quilometragem = models.IntegerField()

    def __str__(self):
        return f"{self.modelo} - {self.placa}"
    
class Servico(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="servicos")
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)
    proxima_manutencao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Serviço para {self.veiculo.placa} em {self.data}"

