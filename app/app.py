from flask import Flask, request, render_template, url_for
from keras.preprocessing import image
from keras.models import load_model
import numpy as np

app = Flask(__name__)

# load your trained model (you need to provide the correct)
cnn = load_model('../model.keras')

@app.route('/', methods=['GET', 'POST'])
def predict():
    '''gives us prediction by evaluating model'''
    prediction = None 
    if request.method == 'POST':
        img_file = request.files['img']
        if img_file:
            img_path = 'temp.img'
            img_file.save(img_path)
            test_image = image.load_img(img_path, target_size=(64, 64))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            result = cnn.predict(test_image)
            if result[0][0] == 1:
                prediction = 'dog'
            else:
                prediction = 'cat'

    return render_template('home.html', prediction = prediction)

if __name__ == '__main__':
    app.run(debug=True)