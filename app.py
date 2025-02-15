from flask import Flask, request, jsonify
import os
from model import predict_image

app = Flask(__name__)

# Optional root route to avoid "no data" issues on GET /
@app.route('/', methods=['GET'])
def home():
    return '''
    <h1>Smart Age App</h1>
    <p>POST an image to <code>/predict</code> to get age predictions.</p>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    print("Got a request to /predict", flush=True)
    if 'image' not in request.files:
        print("No file found in request", flush=True)
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['image']
    file_path = "temp.png"
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
