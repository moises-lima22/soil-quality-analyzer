from flask import Flask
from flask_cors import CORS
from controllers.sample_controller import sample_bp

app = Flask(__name__)
CORS(app)

# Registrar Blueprint
app.register_blueprint(sample_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
