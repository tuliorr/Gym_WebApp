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

# Função para obter as informações de uma atividade
def get_one(id):
    
    sql = 'SELECT * FROM webuser.ATIVIDADES WHERE id = %s'
    
    value = [id]
    
    result = runSQL(sql, value)[0]
    
    if result is not None:
        
        tipo_plano = plano.get_one(row['plano'])
        
        atividade = Atividade(result['nome'],
                              result['instrutor'],
                              result['data'],
                              result['duracao'],
                              result['capacidade'],
                              tipo_plano,
                              result['ativo'],
                              result['id'])
            
    return atividade

# Função para criar um atividade
def new_one(atividade):
    
    sql = 'INSERT INTO webuser.ATIVIDADES (nome, instrutor, data, duracao, capacidade, tipo_plano, ativo) \
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *;'
    
    values = [atividade.nome.id, atividade.instrutor.id, atividade.data.id, atividade.duracao.id,
              atividade.capacidade.id, atividade.tipo_plano.id, atividade.ativo.id]
        
    results = runSQL(sql, values)
    
    atividade.id = results[0]['id']
        
    return atividade

# Função para verificar se uma atividade existe
def verifica_atividade(nome, instrutor, data):
    
    sql = 'SELECT * FROM webuser.ATIVIDADES WHERE atividade = %s AND aluno = %s'
    
    value = [atividade, aluno]
    
    result = runSQL(sql, value)
    
    if len(result) == 0:
        return False
    
    else:
        return True
