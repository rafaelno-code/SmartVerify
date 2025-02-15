# Smart Age App (Local Installation)

This project uses a **Keras model** exported from Google Teachable Machine (`keras_model.h5`) to classify images by age range. Below are instructions for setting up a **local** Python environment, installing dependencies, and running the Flask application.

---

## 1. Prerequisites

### Python Version
- We tested with **3.11** on macOS (Apple Silicon).  
- If you're using Windows or Intel macOS, the same Python version should still work.

### Where to Download Python
- **Windows**: [Python.org Downloads](https://www.python.org/downloads/windows/)  
- **macOS**: [Python.org Downloads](https://www.python.org/downloads/macos/) or use Homebrew (`brew install python@3.11`)  

---

## 2. Creating a Virtual Environment

1. **Open a terminal** (Command Prompt on Windows, Terminal on macOS).
2. **Verify** you have the correct Python version:
   ```bash
   python --version
If it doesn’t match the required version (e.g., 3.11.x), install or specify the path to that Python.

3. **Create** a virtual environment (named venv):
   ```bash
   python -m venv venv
This will create a folder called venv with isolated Python packages.

4. **Activate** the environment
- Windows (CMD):
  ```bat
  venv\Scripts\activate

- macOS/Linux:
  ```bash
  source venv/bin/activate

5. Confirm you see (venv) or a similar marker in your command prompt.

---

## 3. Installing Dependencies 

With your virtual environment active:
  ```bash
pip install --upgrade pip
pip install -r requirements.txt
```
- This installs Flask, TensorFlow, Pillow, Numpy, etc.
- If you encounter errors (especially on Apple Silicon), see “Troubleshooting” below.

---

## 4. Project Files 
- `app.py`: The Flask application, which defines two routes:
  - `GET /`: A simple welcome message.
  - `POST /predict`: Accepts an image file for inference.
- `model.py`: Loads `keras_model.h5` and `labels.txt`, and provides a `predict_image(...)` function.
- `keras_model.h5` + `labels.txt`: The exported Teachable Machine model + label names.
- `requirements.txt`: Lists the Python packages needed.
- `test_images/`: Contains some sample images for testing (optional).

--- 

## 5. Running Locally 

1. Activate your virtual environment if not already active.

2. Run the Flask app:
```bash
python app.py
```

3. You should see:
```csharp
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

4. Test in your browser by visiting http://127.0.0.1:5000/ to see a welcome message.

5. Test the /predict route with curl or a tool like Postman:
Open a new terminal window and run:
```bash
curl -X POST -F "image=@test_images/IMG_6567.png" http://127.0.0.1:5000/predict
```
You should get a JSON response like:
```json
{"class":"21-30","confidence":0.85}
```