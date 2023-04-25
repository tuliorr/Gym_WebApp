# Classe Agendamento
class Agendamento:
    
    # Método construtor para inicialização dos atributos
    def __init__(self, atividade, aluno, id=None):
            self.atividade = atividade
            self.aluno = aluno
            self.id = id