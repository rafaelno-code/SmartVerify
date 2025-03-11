from flask import Flask, request, jsonify, render_template
import os
from model import predict_image

app = Flask(__name__)

# Optional root route to avoid "no data" issues on GET /
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print("Got a request to /predict", flush=True)
    if 'image' not in request.files:
        print("No file found in request", flush=True)
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['image']
    file_path = "temp.png" #Change this line to the uploaded image by the user
    file.save(file_path)
    print(f"Saved image to {file_path}", flush=True)

    # Add a try-except around model inference
    try:
        label, confidence = predict_image(file_path)
        os.remove(file_path)
        print(f"label={label}, confidence={confidence}", flush=True)
        return jsonify({"class": label, "confidence": confidence})
    except Exception as e:
        print(f"Inference error: {e}", flush=True)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
