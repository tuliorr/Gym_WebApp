# Módulo de conexão entre a classe e o banco de dados

# Imports

from classes.plano import TipoPlano
from database.runSQL import runSQL

# Função para obter todos os planos
def get_all():
    
    tipos_planos = []
    
    sql = 'SELECT * FROM webuser.PLANOS'
    
    results = runSQL(sql)
    
    for row in results:
        tipo_plano = TipoPlano(row['id'], row['plano'])
        tipos_planos.append(tipo_plano)
    
    return tipos_planos


# Função para obter um plano
def get_one(id):
    
    sql = 'SELECT * FROM webuser.PLANOS WHERE id = %s'
    
    value = [id]
    
    result = runSQL(sql, value)[0]
    
    if result is not None:
        tipo_plano = TipoPlano(result['plano'], result['id'])
        
    return tipo_plano

# Função para criar um tipo de plano
def new_one(novo_plano):
    
    sql = 'INSERT INTO webuser.PLANOS (plano) VALUES (%s) RETURNING *;'
    
    values = [novo_plano.plano]
    
    results = runSQL(sql, values)
    
    novo_plano.id = results[0]['id']
        
    return novo_plano

# Função para deletar um plano
def del_one(id):
    
    sql = 'DELETE FROM webuser.PLANOS WHERE id = %s'
    
    value = [id]
    
    results = runSQL(sql, value)

# Função para alterar um plano
def edit(tipo_plano):
    
    sql = 'UPDATE webuser.PLANOS SET (plano) = (%s) WHERE id = %s'
    
    values = [tipo_plano.plano, tipo_plano.id]
    
    results = runSQL(sql, values)