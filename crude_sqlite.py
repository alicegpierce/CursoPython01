import sqlite3

#Primeiro vamos nos conectar ao banco de dados (ou criar um novo se nao existir)
def conectar_banco():
    conexao = sqlite3.connect('exemplo.db') #Nome do banco de dados
    return conexao 

#Criar tabela no novo banco exemplo.db
def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER 
        )
    ''') #dentro dos parenteses temos sql aka sqlite
    conexao.commit()
    conexao.close()

#Inserir dados na tabela 
def inserir_usuario(campo_nome, campo_idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade) VALUES (?,?)
    ''', (campo_nome, campo_idade)) #dentro dos parenteses temos sql aka sqlite #os pontos de interrogacao no sql significa "reserva de espaços"
    conexao.commit()
    conexao.close()

#Ler dados do banco 
def listar_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios
        ''') 
   # conexao.commit() #Desativei pois nesse caso nao ha necessidade de ''comprometer'' para apenar ler dados
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

#Atualizar dados do banco 
def atualizar_usuario(id, novo_nome, nova_idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET nome = ?,
        idade = ?
        WHERE id = ?
        ''', (novo_nome, nova_idade, id)) 
    conexao.commit()
    conexao.close()

#Excluir dados do banco 
def excluir_usuario(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM usuarios WHERE ID = ?''', (id,)) 
    conexao.commit()
    conexao.close()

#Exemplos de uso das Funções CRUD

#Criar a tabela (execute apenas uma vez - só vai criar se nao existir ja que dei o comando no inicio if not exists)
criar_tabela()

#Inserir alguns dados!
inserir_usuario('Caio', 31)
inserir_usuario('Jesreel', 21)
inserir_usuario('Eloara', 42)
inserir_usuario('Alice', 23)
inserir_usuario('Emily', 20)
inserir_usuario('Davi', 18)
inserir_usuario('Andressa', 51)

#Ver os dados cadastrados:
print('Dados Originais - antes da atualização')
listar_usuarios()

#Quero atualizar a idade de um usuário:
atualizar_usuario(4, 'Alice Pierce', 24)

#Lista atualizada de usuários:
print('\n Lista de usuários atualizada')
listar_usuarios()

#Excluir usuário:
excluir_usuario(1)

#Lista atualizada de usuários após exclusão:
print('\n Lista de usuários atualizada')
listar_usuarios()