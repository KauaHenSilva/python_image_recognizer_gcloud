import os
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates')
model = load_model('models/cifar10_model.keras')

class_names = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (32, 32))
    image = image.astype('float32') / 255.0
    image = image.reshape((1, 32, 32, 3))
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'imagem' not in request.files:
        return "Nenhum arquivo enviado", 400
    
    file = request.files['imagem']
    if file.filename == '':
        return "Nome do arquivo vazio", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join('uploads', filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(filepath)

    image = preprocess_image(filepath)
    prediction = model.predict(image)
    predicted_class = class_names[np.argmax(prediction)]

    return render_template('result.html', prediction=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
