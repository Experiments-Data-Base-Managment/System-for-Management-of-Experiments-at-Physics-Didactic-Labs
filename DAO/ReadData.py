import sqlite3

#Conexao
conn = sqlite3.connect('sistemaGestor.db')

cursor = conn.cursor()

#cursor.execute("""
#SELECT * FROM experimentos;
#""")

#for linha in cursor.fetchall():
 #   print(linha)

cursor.execute('SELECT max(id) FROM experimentos')
max_id = cursor.fetchone()[0]
print "EXP_" + str(max_id)
conn.close()
