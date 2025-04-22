import cx_Oracle

# Dados do banco Oracle (Docker)
USERNAME = "soil_user"
PASSWORD = "soil123"
DSN = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")


def get_connection():
    return cx_Oracle.connect(USERNAME, PASSWORD, DSN)


def insert_sample(data, status):
    conn = None
    cursor = None  # Inicialize o cursor como None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO soil_samples (ph, nitrogen, phosphorus, potassium, compaction, status)
            VALUES (:ph, :nitrogen, :phosphorus, :potassium, :compaction, :status)
            """,
            {
                "ph": data["ph"],
                "nitrogen": data["nitrogen"],
                "phosphorus": data["phosphorus"],
                "potassium": data["potassium"],
                "compaction": data["compaction"],
                "status": status,
            },
        )
        conn.commit()
        print("📥 Amostra inserida no banco Oracle com sucesso.")
    except Exception as e:
        print("❌ Erro ao inserir no Oracle:", e)
    finally:
        if cursor:  # Verifique se o cursor foi inicializado
            cursor.close()
        if conn:  # Verifique se a conexão foi inicializada
            conn.close()
