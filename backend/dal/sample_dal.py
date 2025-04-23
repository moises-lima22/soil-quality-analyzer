from utils.oracle_utils import get_connection


def fetch_all_samples():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, ph, nitrogen, phosphorus, potassium, compaction, status
            FROM SoilSample
            """
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception as e:
        raise RuntimeError(f"Error fetching samples: {str(e)}")


def insert_sample_into_db(sample_data):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO SoilSample (ph, nitrogen, phosphorus, potassium, compaction, status)
            VALUES (:1, :2, :3, :4, :5, :6)
            """,
            (
                sample_data["ph"],
                sample_data["nitrogen"],
                sample_data["phosphorus"],
                sample_data["potassium"],
                sample_data["compaction"],
                sample_data["status"],
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        raise RuntimeError(f"Error inserting sample: {str(e)}")


def update_sample_in_db(sample_id, sample_data):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE SoilSample
            SET ph = :1, nitrogen = :2, phosphorus = :3, potassium = :4, compaction = :5, status = :6
            WHERE id = :7
            """,
            (
                sample_data["ph"],
                sample_data["nitrogen"],
                sample_data["phosphorus"],
                sample_data["potassium"],
                sample_data["compaction"],
                sample_data["status"],
                sample_id,
            ),
        )
        if cursor.rowcount == 0:
            raise ValueError("Sample not found")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        raise RuntimeError(f"Error updating sample: {str(e)}")


def delete_sample_from_db(sample_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM SoilSample
            WHERE id = :1
            """,
            (sample_id,),
        )
        if cursor.rowcount == 0:
            raise ValueError("Sample not found")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        raise RuntimeError(f"Error deleting sample: {str(e)}")