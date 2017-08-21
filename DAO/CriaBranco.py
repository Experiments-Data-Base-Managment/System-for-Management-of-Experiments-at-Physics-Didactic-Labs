import sqlite3

#Conexao
conn = sqlite3.connect('sistemaGestor.db')

#Definindo cursos
cursor = conn.cursor()

#Criando Tabela
cursor.execute("""
CREATE TABLE experimentos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        instituicao TEXT NOT NULL,
        curso TEXT NOT NULL,
        turma TEXT NOT NULL,
        professor TEXT NOT NULL,
        aluno TEXT NOT NULL,
        experimento TEXT NOT NULL,
        id_experimento TEXT NOT NULL,
        data DATE NOT NULL,
        hora TEXT NOT NULL
        estado_cidade TEXT NOT NULL,
        descricao TEXT NOT NULL

);
""")

cursor.execute("""
INSERT INTO experimentos (nome, descricao, instituicao, cidade, data)
VALUES ('Luiz', 'experimento teste', 'UNEB', 'Salvador','2017-03-07')
""")

conn.commit()


conn.close()

