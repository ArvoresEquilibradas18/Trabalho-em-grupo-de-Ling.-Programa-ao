from database.conexao import engine
from sqlalchemy import text

with engine.connect() as conn:
    # Ver colunas
    result = conn.execute(text("""
        SELECT COLUMN_NAME, IS_NULLABLE, DATA_TYPE 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'medicos'
    """))
    print("=== COLUNAS ===")
    for row in result:
        print(row)

    # Ver constraints unique
    result2 = conn.execute(text("""
        SELECT i.name, c.name as coluna
        FROM sys.indexes i
        JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
        JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
        WHERE i.is_unique = 1 AND OBJECT_NAME(i.object_id) = 'medicos'
    """))
    print("=== UNIQUE KEYS ===")
    for row in result2:
        print(row)