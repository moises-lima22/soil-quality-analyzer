import json
from utils.soil_utils import evaluate_soil
from utils.oracle_utils import insert_sample
from config.settings import STORAGE_MODE

SAMPLES_FILE = "samples.json"

def load_samples():
    try:
        with open(SAMPLES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_samples(samples):
    with open(SAMPLES_FILE, "w") as file:
        json.dump(samples, file, indent=2)

def add_sample(data, storage_mode):
    result = evaluate_soil(data)

    if storage_mode == "json":
        samples = load_samples()
        samples.append(data)
        save_samples(samples)
    elif storage_mode == "oracle":
        insert_sample(data, result["status"])

    return result