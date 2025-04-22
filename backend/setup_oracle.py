import cx_Oracle
import time

# Dados da instância Oracle Docker
ADMIN_USER = "system"
ADMIN_PASSWORD = "oracle"
DSN = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")

# Novo schema (usuário) da aplicação
NEW_USER = "soil_user"
NEW_PASS = "soil123"

print("⏳ Conectando ao Oracle Docker...")

# Aguarda alguns segundos se container acabou de subir
time.sleep(5)

try:
    conn = cx_Oracle.connect(ADMIN_USER, ADMIN_PASSWORD, DSN)
    cursor = conn.cursor()

    # Criação do usuário (ignora se já existir)
    try:
        cursor.execute(f"CREATE USER {NEW_USER} IDENTIFIED BY {NEW_PASS}")
        print(f"✅ Usuário {NEW_USER} criado.")
    except cx_Oracle.DatabaseError as e:
        if "ORA-01920" in str(e) or "ORA-01918" in str(e):
            raise
        print("ℹ️ Usuário já existe, seguindo...")

    # Permissões básicas
    cursor.execute(f"GRANT CONNECT, RESOURCE TO {NEW_USER}")
    print("🔐 Permissões atribuídas.")

    # Conecta com o novo usuário
    user_conn = cx_Oracle.connect(NEW_USER, NEW_PASS, DSN)
    user_cursor = user_conn.cursor()

    # Criação da tabela
    user_cursor.execute(
        """
        BEGIN
            EXECUTE IMMEDIATE '
                CREATE TABLE SoilSample (
                    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    ph NUMBER(3,1),
                    nitrogen NUMBER,
                    phosphorus NUMBER,
                    potassium NUMBER,
                    compaction NUMBER(3,2),
                    status VARCHAR2(10)
                )
            ';
        EXCEPTION
            WHEN OTHERS THEN
                IF SQLCODE != -955 THEN
                    RAISE;
                END IF;
        END;
    """
    )

    print("📦 Tabela SoilSample criada (ou já existente).")
    user_cursor.close()
    user_conn.close()
    cursor.close()
    conn.close()
    print("✅ Setup finalizado com sucesso.")

except Exception as e:
    print("❌ Erro ao configurar o banco Oracle:", e)
