from flask import Blueprint, request, jsonify
from services.sample_service import add_sample, load_samples
from utils.soil_utils import evaluate_soil
from config.settings import STORAGE_MODE

sample_bp = Blueprint("sample", __name__)

@sample_bp.route("/samples", methods=["GET"])
def get_samples():
    return jsonify(load_samples())

@sample_bp.route("/samples", methods=["POST"])
def create_sample():
    data = request.get_json()
    required_keys = {"ph", "nitrogen", "phosphorus", "potassium", "compaction"}

    if not all(key in data for key in required_keys):
        return jsonify({"error": "Missing fields"}), 400

    try:
        data = {key: float(value) for key, value in data.items()}
    except ValueError:
        return jsonify({"error": "Invalid data format. All values must be numbers."}), 400

    result = add_sample(data, STORAGE_MODE)
    return jsonify({"message": "Sample added successfully", "status": result["status"]}), 201

@sample_bp.route("/evaluate", methods=["GET"])
def evaluate_all():
    samples = load_samples()
    results = [evaluate_soil(sample) for sample in samples]
    return jsonify(results)