from flask import Flask, render_template
import logging

import os

app = Flask(__name__)

@app.route('/')
def index():
    os.chdir("viz/static/images/")
    cwd = os.getcwd()
    # image_names = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg', 'image6.jpg', 'image7.jpg', 'image8.jpg', 'image9.jpg', 'image10.jpg']
    image_names = os.listdir(cwd)
    return render_template('index.html', image_names=image_names)

if __name__ == '__main__':
    app.run(debug=True)
