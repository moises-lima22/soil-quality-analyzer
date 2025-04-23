import json
from utils.soil_utils import evaluate_soil
from dal.sample_dal import (
    fetch_all_samples,
    insert_sample_into_db,
    update_sample_in_db,
    delete_sample_from_db,
)
from config.settings import STORAGE_MODE

SAMPLES_FILE = "samples.json"


def load_samples():
    try:
        rows = fetch_all_samples()
        return {"status": "success", "data": [
            {
                "id": row[0],
                "ph": row[1],
                "nitrogen": row[2],
                "phosphorus": row[3],
                "potassium": row[4],
                "compaction": row[5],
                "status": row[6],
            }
            for row in rows
        ]}
    except RuntimeError as e:
        return {"status": "error", "message": str(e)}


def save_samples(samples):
    with open(SAMPLES_FILE, "w") as file:
        json.dump(samples, file, indent=2)


def validate_sample_data(data, is_update=False):
    required_keys = {"ph", "nitrogen", "phosphorus", "potassium", "compaction"}
    numeric_keys = {"ph", "nitrogen", "phosphorus", "potassium", "compaction"}

    # Verifica se todos os campos obrigatórios estão presentes
    if not is_update and not all(key in data for key in required_keys):
        return {"status": "error", "message": "Missing required fields"}

    # Valida os tipos de dados
    try:
        numeric_data = {key: float(data[key]) for key in numeric_keys if key in data}
        status = data.get("status")

        # Calcula o status automaticamente se não for fornecido
        if not status:
            status = evaluate_soil_status(numeric_data)

        if not isinstance(status, str):
            raise ValueError("Invalid data format. 'status' must be a string.")
        return {"status": "success", "data": {**numeric_data, "status": status}}
    except (ValueError, TypeError) as e:
        return {"status": "error", "message": str(e)}


def add_sample(data):
    validation = validate_sample_data(data)
    if validation["status"] == "error":
        return validation

    sample_data = validation["data"]
    try:
        insert_sample_into_db(sample_data)
        return {"status": "success"}
    except RuntimeError as e:
        return {"status": "error", "message": str(e)}


def update_sample(sample_id, data):
    validation = validate_sample_data(data, is_update=True)
    if validation["status"] == "error":
        return validation

    sample_data = validation["data"]
    try:
        update_sample_in_db(sample_id, sample_data)
        return {"status": "success"}
    except RuntimeError as e:
        return {"status": "error", "message": str(e)}


def delete_sample(sample_id):
    try:
        delete_sample_from_db(sample_id)
        return {"status": "success"}
    except RuntimeError as e:
        return {"status": "error", "message": str(e)}


def evaluate_soil_status(data):
    """
    Avalia o status do solo com base nos critérios fornecidos.
    Retorna "Apto" se 4 ou mais critérios forem atendidos, caso contrário "Inapto".
    """
    criteria_met = 0

    # Avaliação dos critérios
    if 5.5 <= data["ph"] <= 7.0:
        criteria_met += 1
    if data["nitrogen"] > 20:
        criteria_met += 1
    if data["phosphorus"] > 15:
        criteria_met += 1
    if data["potassium"] > 100:
        criteria_met += 1
    if data["compaction"] < 1.4:
        criteria_met += 1

    # Determina o status com base nos critérios atendidos
    return "Apto" if criteria_met >= 4 else "Inapto"


def evaluate_samples():
    try:
        rows = fetch_all_samples()
        samples = [
            {
                "id": row[0],
                "ph": row[1],
                "nitrogen": row[2],
                "phosphorus": row[3],
                "potassium": row[4],
                "compaction": row[5],
                "status": row[6],
            }
            for row in rows
        ]
        results = [evaluate_soil(sample) for sample in samples]
        return {"status": "success", "data": results}
    except RuntimeError as e:
        return {"status": "error", "message": str(e)}
