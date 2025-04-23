from flask import Blueprint, request, jsonify, send_file
from services.sample_service import (
    add_sample,
    load_samples,
    update_sample,
    delete_sample,
    evaluate_samples,
    save_report_to_txt,
)
from utils.soil_utils import evaluate_soil
from config.settings import STORAGE_MODE
import os

sample_bp = Blueprint("sample", __name__)


@sample_bp.route("/samples", methods=["GET"])
def get_samples():
    result = load_samples()
    if result.get("status") == "error":
        return jsonify({"error": result["message"]}), 500
    return jsonify(result["data"]), 200


@sample_bp.route("/samples", methods=["POST"])
def create_sample():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input. JSON data is required."}), 400

    result = add_sample(data)
    if result.get("status") == "error":
        return jsonify({"error": result["message"]}), 400
    return jsonify({"message": "Sample added successfully"}), 201


@sample_bp.route("/samples/<int:sample_id>", methods=["PUT"])
def update_sample_endpoint(sample_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input. JSON data is required."}), 400

    result = update_sample(sample_id, data)
    if result.get("status") == "error":
        return jsonify({"error": result["message"]}), 400
    return jsonify({"message": "Sample updated successfully"}), 200


@sample_bp.route("/samples/<int:sample_id>", methods=["DELETE"])
def delete_sample_endpoint(sample_id):
    result = delete_sample(sample_id)
    if result.get("status") == "error":
        return jsonify({"error": result["message"]}), 400
    return jsonify({"message": "Sample deleted successfully"}), 200


@sample_bp.route("/evaluate", methods=["GET"])
def evaluate_all():
    result = evaluate_samples()
    if result.get("status") == "error":
        return jsonify({"error": result["message"]}), 500
    return jsonify(result["data"]), 200


@sample_bp.route("/samples/report", methods=["GET"])
def download_report():
    try:
        result = load_samples()
        if result.get("status") == "error":
            return jsonify({"error": result["message"]}), 500

        samples = result["data"]

        filename = "report.txt"
        save_report_to_txt(samples, filename)

        return send_file(
            filename,
            as_attachment=True,
            download_name=filename,
            mimetype="text/plain",
        )
    except Exception as e:
        return jsonify({"error": f"Erro ao gerar o relatório: {str(e)}"}), 500
