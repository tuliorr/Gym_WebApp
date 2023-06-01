# Módulo de conexão entre a classe e o banco de dados

# Imports

from classes.agendamento import Agendamento

from database.runSQL import runSQL

# Função para retornar uma lista com todos os agendamentos

def get_all():
    
    agendamentos = []
    
    sql = 'SELECT * FROM webuser.AGENDAMENTOS'
    
    results = runSQL(sql)
    
    for row in results:
        
        tipo_plano = plano.get_one(row['plano'])
        
        agendamentos = Agendamento(row['atividade'],
                                   row['aluno'],
                                   row['id'])
        
        agendamentos.append(aluno)
    
    return agendamentos

# Função para obter as informações de um agendamento
def get_one(id):
    
    sql = 'SELECT * FROM webuser.AGENDAMENTOS WHERE id = %s'
    
    value = [id]
    
    result = runSQL(sql, value)[0]
    
    if result is not None:
        
        agendamento = Agendamento(result['atividade'],
                                   result['aluno'],
                                   result['id'])
            
    return agendamento

# Função para criar um agendamento
def new_one(agendamento):
    
    sql = 'INSERT INTO webuser.AGENDAMENTOS (atividade, aluno) VALUES (%s, %s) RETURNING *;'
    
    values = [agendamento.atividade.id, agendamento.aluno.id]
        
    results = runSQL(sql, values)
    
    agendamento.id = results[0]['id']
        
    return agendamento

# Função para verificar se um agendamento existe
def verifica_agendamento(atividade, aluno):
    
    sql = 'SELECT * FROM webuser.AGENDAMENTOS WHERE atividade = %s AND aluno = %s'
    
    value = [atividade, aluno]
    
    result = runSQL(sql, value)
    
    if len(result) == 0:
        return False
    
    else:
        return True
    
# Função para deletar um agendamento por meio do atividade e do aluno
def del_agendamento(atividade, aluno):
    
    sql = 'DELETE FROM webuser.AGENDAMENTOS WHERE atividade = %s AND aluno = %s'
    
    value = [atividade, aluno]
    
    results = runSQL(sql, value)