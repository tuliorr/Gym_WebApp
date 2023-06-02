# Módulo de conexão entre a classe e o banco de dados

# Imports

import conectores.con_plano as plano

from classes.aluno import Aluno
from classes.atividade import Atividade

from database.runSQL import runSQL

# Função para retornar uma lista com todas as atividades
def get_all():
    
    atividades = []
    
    sql = 'SELECT * FROM webuser.ATIVIDADES ORDER BY nome ASC'
    
    results = runSQL(sql)
    
    for row in results:
        
        tipo_plano = plano.get_one(row['plano'])
        
        atividade = Atividade(row['nome'],
                              row['instrutor'],
                              row['data'],
                              row['duracao'],
                              row['capacidade'],
                              tipo_plano,
                              row['ativo'],
                              row['id'])
        
        atividades.append(atividade)
    
    return atividades

# Função para obter alunos de uma atividade
def get_alunos(id):
    
    alunos = []
    
    sql = 'SELECT alunos.* FROM webuser.ALUNOS INNER JOIN webuser.AGENDAMENTOS ON alunos.id = webuser.AGENDAMENTOS.aluno \
        WHERE webuser.AGENDAMENTOS.atividade = %s'
        
    value = [id]
    
    results = runSQL(sql, value)
    
    for row in results:
        
        aluno = Aluno(row["nome"],
                      row["sobrenome"],
                      row["data_nascimento"],
                      row["endereco"],
                      row["telefone"],
                      row["email"],
                      row["tipo_plano"],
                      row["data_inicio"],
                      row["ativo"],
                      row["id"])
        
        alunos.append(aluno)
        
    return alunos
    

# Função para obter atividades ativas a partir de uma data
def active_on_date(data):
    
    sql = 'SELECT * FROM webuser.ATIVIDADES WHERE ativo = true ORDER BY nome ASC where data = %s'
    
    value = [data]
    
    result = runSQL(sql, value)[0]
    
    atividades = []
    
    if result is not None:
        
        for row in result:
            
            tipo_plano = plano.get_one(row['plano'])
            
            atividade = Atividade(row['nome'],
                                  row['instrutor'],
                                  row['data'],
                                  row['duracao'],
                                  row['capacidade'],
                                  tipo_plano,
                                  row['ativo'],
                                  row['id'])
            
            atividades.append(atividade)
            
    return atividades

# Função para obter as atividades ativas ordenadas por data
def get_all_active():
    
    atividades = []
    
    sql = 'SELECT * FROM webuser.ATIVIDADES WHERE ativo = true ORDER BY data ASC'
    
    result = runSQL(sql)
       
    for row in result:
        
        tipo_plano = plano.get_one(row['plano'])
        
        atividade = Atividade(row['nome'],
                              row['instrutor'],
                              row['data'],
                              row['duracao'],
                              row['capacidade'],
                              tipo_plano,
                              row['ativo'],
                              row['id'])
        
        atividades.append(atividade)
            
    return atividades

# Função para obter as atividades inativas ordenadas por data
def get_all_inactive():
    
    atividades = []
    
    sql = 'SELECT * FROM webuser.ATIVIDADES WHERE ativo = false ORDER BY data ASC'
    
    result = runSQL(sql)
       
    for row in result:
        
        tipo_plano = plano.get_one(row['plano'])
        
        atividade = Atividade(row['nome'],
                              row['instrutor'],
                              row['data'],
                              row['duracao'],
                              row['capacidade'],
                              tipo_plano,
                              row['ativo'],
                              row['id'])
        
        atividades.append(atividade)
            
    return atividades

# Função para criar uma atividade
def new_one(atividade):
    
    sql = 'INSERT INTO webuser.ATIVIDADES (nome, instrutor, data, duracao, capacidade, tipo_plano, ativo) \
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *;'
    
    values = [atividade.nome, atividade.instrutor, atividade.data, atividade.duracao,
              atividade.capacidade, atividade.tipo_plano, atividade.ativo]
        
    results = runSQL(sql, values)
    
    atividade.id = results[0]['id']
        
    return atividade

# Função para deletar uma atividade
def delete_one(id):
    
    sql = 'DELETE FROM webuser.ATIVIDADES WHERE id = %s'
    
    values = [id]
        
    runSQL(sql, values)

# Função para editar uma atividade
def edit(atividade):
    
    sql = 'UPDATE webuser.ATIVIDADES SET (nome, instrutor, data, duracao, capacidade, tipo_plano, ativo) \
        VALUES (%s, %s, %s, %s, %s, %s, %s) WHERE atividade = %s'
        
    values = [atividade.nome, atividade.instrutor, atividade.data, atividade.duracao,
              atividade.capacidade, atividade.tipo_plano, atividade.ativo]
    
    runSQL(sql, values)

# Função para verificar se uma atividade existe
def verifica_atividade(atividade, aluno, data):
    
    sql = 'SELECT * FROM webuser.ATIVIDADES WHERE atividade = %s AND aluno = %s AND data = %s'
    
    value = [atividade, aluno, data]
    
    result = runSQL(sql, value)
    
    if len(result) == 0:
        return False
    
    else:
        return True
    
# Função para obter uma atividade ativa
def get_one(id):
    
    sql = 'SELECT * FROM webuser.ATIVIDADES WHERE ativo = true AND id = %s'
    
    value = [id]
    
    result = runSQL(sql, value)[0]
    
    if result is not None:

        tipo_plano = plano.get_one(row['plano'])
        
        atividade = Atividade(row['nome'],
                              row['instrutor'],
                              row['data'],
                              row['duracao'],
                              row['capacidade'],
                              tipo_plano,
                              row['ativo'],
                              row['id'])
        
    return atividade
        
