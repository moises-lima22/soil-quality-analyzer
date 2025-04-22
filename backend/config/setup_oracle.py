import cx_Oracle
import time

# Dados da instância Oracle Docker
ADMIN_USER = "system"
ADMIN_PASSWORD = "oracle"
DSN = cx_Oracle.makedsn("oracle", 1521, service_name="freepdb1")

print("⏳ Conectando ao Oracle Docker...")

def wait_for_oracle(timeout=10):
    for i in range(timeout + 1):
        try:
            conn = cx_Oracle.connect(ADMIN_USER, ADMIN_PASSWORD, DSN)
            conn.close()
            print("✅ Conexão com o Oracle estabelecida.")
            return
        except cx_Oracle.DatabaseError as e:
            print(f"⏳ Tentativa {i+1}/{timeout}: Oracle ainda não está pronto... erro:", e)
            time.sleep(1)
    raise Exception(f"❌ O Oracle não está pronto após {timeout} segundos.")

# Aguarda o Oracle estar pronto
wait_for_oracle()

try:
    conn = cx_Oracle.connect(ADMIN_USER, ADMIN_PASSWORD, DSN)
    cursor = conn.cursor()

    # Criação da tabela no schema SYSTEM
    cursor.execute(
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
    cursor.close()
    conn.close()
    print("✅ Setup finalizado com sucesso.")

except Exception as e:
    print("❌ Erro ao configurar o banco Oracle:", e)
