class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['cliente', 'modelo', 'placa', 'quilometragem']
class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['veiculo', 'descricao', 'proxima_manutencao']
