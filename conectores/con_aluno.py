# Módulo de conexão entre a classe e o banco de dados

# Imports

import conectores.con_plano as plano

from classes.aluno import Aluno
from classes.atividade import Atividade

from database.runSQL import runSQL

# Função para retornar uma lista com todos os alunos
def get_all():
    
    alunos = []
    
    sql = 'SELECT * FROM webuser.ALUNOS ORDER BY nome ASC'
    
    results = runSQL(sql)
    
    for row in results:
        
        tipo_plano = plano.get_one(row['plano'])
        
        aluno = Aluno(row['nome'],
                      row['sobrenome'],
                      row['data_nascimento'],
                      row['endereco'],
                      row['telefone'],
                      row['email'],
                      tipo_plano,
                      row['data_inicio'],
                      row['ativo'],
                      row['id'])
        
        alunos.append(aluno)
    
    return alunos


# Função para obter as informações de um aluno
def get_one(id):
    
    sql = 'SELECT * FROM webuser.ALUNOS WHERE id = %s'
    
    value = [id]
    
    result = runSQL(sql, value)[0]
    
    if result is not None:
        
        tipo_plano = plano.get_one(row['plano'])
        
        aluno = Aluno(result['nome'],
                      result['sobrenome'],
                      result['data_nascimento'],
                      result['endereco'],
                      result['telefone'],
                      result['email'],
                      tipo_plano,
                      result['data_inicio'],
                      result['ativo'],
                      result['id'])
            
    return aluno

# Função para listar todas as atividades de um aluno
def get_activities(user_id):
    
    atividades = []
    
    sql = 'SELECT atividades.* FROM webuser.ATIVIDADES \
        INNER JOIN webuser.AGENDAMENTOS on webuser.ATIVIDADES.id = webuser.AGENDAMENTOS.atividade WHERE webuser.AGENDAMENTOS.aluno = %s'
        
    value = [user_id]
    
    results = runSQL(sql, value)
    
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

# Função para obter uma lista com todos os alunos ativos
def get_all_active():
    
    alunos = []
    
    sql = 'SELECT * FROM webuser.ALUNOS WHERE ativo = true ORDER BY nome ASC'
    
    results = runSQL(sql)
    
    for row in results:
        
        tipo_plano = plano.get_one(row['plano'])
        
        aluno = Aluno(row['nome'],
                      row['sobrenome'],
                      row['data_nascimento'],
                      row['endereco'],
                      row['telefone'],
                      row['email'],
                      tipo_plano,
                      row['data_inicio'],
                      row['ativo'],
                      row['id'])
        
        alunos.append(aluno)
    
    return alunos

# Função para obter uma lista com todos os alunos inativos
def get_all_inactive():
    
    alunos = []
    
    sql = 'SELECT * FROM webuser.ALUNOS WHERE ativo = false ORDER BY nome ASC'
    
    results = runSQL(sql)
    
    for row in results:
        
        tipo_plano = plano.get_one(row['plano'])
        
        aluno = Aluno(row['nome'],
                      row['sobrenome'],
                      row['data_nascimento'],
                      row['endereco'],
                      row['telefone'],
                      row['email'],
                      tipo_plano,
                      row['data_inicio'],
                      row['ativo'],
                      row['id'])
        
        alunos.append(aluno)
    
    return alunos


# Função para criar um aluno
def new_one(novo_aluno):
    
    sql = 'INSERT INTO webuser.ALUNOS \
        (nome, sobrenome, data_nascimento, endereco, telefone, email, tipo_plano, data_inicio, ativo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) \
        RETURNING *;'
    
    values = [novo_aluno.nome, novo_aluno.sobrenome, novo_aluno.data_nascimento, novo_aluno.endereco, novo_aluno.telefone, 
              novo_aluno.email, novo_aluno.tipo_plano, novo_aluno.data_inicio, novo_aluno.ativo]
        
    results = runSQL(sql, values)
    
    novo_aluno.id = results[0]['id']
        
    return novo_aluno

# Função para deletar um aluno
def del_one(id):
    
    sql = 'DELETE FROM webuser.ALUNOS WHERE id = %s'
    
    value = [id]
    
    results = runSQL(sql, value)

# Função para alterar um aluno
def edit(upd_aluno):
    
    sql = 'UPDATE webuser.ALUNOS SET \
        (nome, sobrenome, data_nascimento, endereco, telefone, email, tipo_plano, data_inicio, ativo) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) \
        WHERE id = %s'
    
    values = [upd_aluno.nome, upd_aluno.sobrenome, upd_aluno.data_nascimento, upd_aluno.endereco, upd_aluno.telefone,
              upd_aluno.email, upd_aluno.tipo_plano, upd_aluno.data_inicio, upd_aluno.ativo]
    
    results = runSQL(sql, values)