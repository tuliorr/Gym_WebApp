# Módulo de conexão entre a classe e o banco de dados

# Imports

from classes.instrutor import Instrutor
from classes.atividade import Atividade

from database.runSQL import runSQL

# Função para listar todos os instrutores
def get_all():
    
    instrutores = []
    
    sql = 'SELECT * FROM webuser.INSTRUTORES'
    
    results = runSQL(sql)
    
    for row in results:

        instrutor = Instrutor(row['nome'],
                              row['sobrenome'],
                              row['data_nascimento'],
                              row['endereco'],
                              row['telefone'],
                              row['id'])

        instrutores.append(instrutor)
        
    return instrutores
    
# Função para retornar um instrutor
def get_one(id):
    
    sql = 'SELECT * FROM webuser.INSTRUTORES WHERE id = %s'
    
    value = [id]
    
    result = runSQL(sql, value)[0]
    
    if result is not None:
        
        instrutor = Instrutor(row['nome'],
                              row['sobrenome'],
                              row['data_nascimento'],
                              row['endereco'],
                              row['telefone'],
                              row['id'])
        
    return instrutor

# Função para listar todas as atividades de um instrutor
def get_activities(instructor_id):
    
    sql = 'SELECT * FROM webuser.ATIVIDADES WHERE id = %s'
    
    value = [instructor_id]
    
    result = runSQL(sql, value)[0]
    
    atividades = []
    if result is not None:

        for row in results:
            
            atividade = Atividade(row['nome'],
                                  row['instrutor'],
                                  row['data'],
                                  row['duracao'],
                                  row['capacidade'],
                                  row['tipo_plano'],
                                  row['ativo'],
                                  row['id'])
            
            atividades.append(atividade)
            
    return atividades      
    
# Função para cadastrar um instrutor
def new_one(instrutor):
    
    sql = 'INSERT INTO webuser.INSTRUTORES (nome, sobrenome, data_nascimento, endereco, telefone) \
        VALUES (%s, %s, %s, %s, %s,) RETURNING *;'
        
    values = [instrutor.nome, instrutor.sobrenome, instrutor.data_nascimento, instrutor.endereco, instrutor.telefone]

    result = runSQL(sql, values)
    
    instrutor.id = result[0]['id']
    
    return instrutor

# Função para deletar um instrutor
def delete_one(id):
    
    sql = 'DELETE FROM webuser.INSTRUTORES WHERE id = %s'
    
    value = [id]
    
    runSQL(sql, value)

# Função para editar um instrutor
def edit(instrutor):
      
    sql = 'UPDATE webuser.INSTRUTORES SET (nome, sobrenome, data_nascimento, endereco, telefone) = \
        (%s, %s, %s, %s, %s,) WHERE id = %s;'
        
    values = [instrutor.nome, instrutor.sobrenome, instrutor.data_nascimento, instrutor.endereco, instrutor.telefone]

    return runSQL(sql, values)

