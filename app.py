import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect("sensores.db")
cursor = conn.cursor()

# Criando tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor_sensor INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')


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


# Exemplo de inserção manual de dados
sensor_value = int(input("Digite o valor do sensor: "))  # Simulando entrada manual
cursor.execute("INSERT INTO leituras (valor_sensor) VALUES (?)", (sensor_value,))
conn.commit()

print("Dado armazenado com sucesso!")

# Fechando conexão
conn.close()