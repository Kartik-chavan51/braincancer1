from flask import Flask, render_template, request
import numpy as np
import os
from model import image_pre, predict

app = Flask(__name__)

UPLOAD_FOLDER = r'C:\Users\Kartik\Desktop\photoofcancer\brain_tumor_dataset'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'there is no file in form!'
        file1 = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.jpg')
        file1.save(path)
        data = image_pre(path)
        s = predict(data)
        if s > 0.5:
            result = 'No Brain Cancer'
        else:
            result = 'Brain Cancer'
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)