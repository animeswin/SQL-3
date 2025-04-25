import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produtos (
        ProdutoID INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeProduto TEXT NOT NULL,
        Quantidade INTEGER NOT NULL,
        Preco REAL NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Fornecedores (
        FornecedorID INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeFornecedor TEXT NOT NULL,
        Cidade TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estoque (
        EstoqueID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProdutoID INTEGER NOT NULL,
        FornecedorID INTEGER NOT NULL,
        Quantidade INTEGER NOT NULL,
        DataEntrada DATE NOT NULL,
        FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
        FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
    )
''')

print("Tabelas Produtos, Fornecedores e Estoque criadas com sucesso!")

produtos = [
    ('Notebook Dell', 15, 3500.00),
    ('Teclado Mecânico', 50, 450.00),
    ('Mouse Sem Fio', 30, 200.00)
]
cursor.executemany('''
    INSERT INTO Produtos (NomeProduto, Quantidade, Preco)
    VALUES (?, ?, ?)
''', produtos)

fornecedores = [
    ('Fornecedor A', 'São Paulo'),
    ('Fornecedor B', 'Rio de Janeiro'),
    ('Fornecedor C', 'Fortaleza')
]
cursor.executemany('''
    INSERT INTO Fornecedores (NomeFornecedor, Cidade)
    VALUES (?, ?)
''', fornecedores)

estoque = [
    (1, 1, 10, '2025-04-25'),  # ProdutoID 1, FornecedorID 1
    (2, 2, 20, '2025-04-25'),  # ProdutoID 2, FornecedorID 2
    (3, 3, 15, '2025-04-25')   # ProdutoID 3, FornecedorID 3
]
cursor.executemany('''
    INSERT INTO Estoque (ProdutoID, FornecedorID, Quantidade, DataEntrada)
    VALUES (?, ?, ?, ?)
''', estoque)

conn.commit()
print("Registros inseridos com sucesso!")
conn.close()