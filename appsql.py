import sqlite3

# Conectar ao banco
conn = sqlite3.connect("sensores.db")
cursor = conn.cursor()

# **CREATE** - Inserir dado
def inserir(valor):
    cursor.execute("INSERT INTO leituras (valor_sensor) VALUES (?)", (valor,))
    conn.commit()
    print("Dado inserido!")

# **READ** - Ler dados
def ler_todos():
    cursor.execute("SELECT * FROM leituras")
    for linha in cursor.fetchall():
        print(linha)

# **UPDATE** - Atualizar dado
def atualizar(id, novo_valor):
    cursor.execute("UPDATE leituras SET valor_sensor = ? WHERE id = ?", (novo_valor, id))
    conn.commit()
    print("Dado atualizado!")

# **DELETE** - Deletar dado
def deletar(id):
    cursor.execute("DELETE FROM leituras WHERE id = ?", (id,))
    conn.commit()
    print("Dado deletado!")

# Testando funções
inserir(500)
ler_todos()
atualizar(1, 600)
deletar(1)

# Fechando conexão
conn.close()