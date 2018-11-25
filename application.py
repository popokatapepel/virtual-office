import logging
import os
import re
import base64
from random import randint

from random import randint

from PIL import Image
from flask import Flask, redirect, url_for, jsonify, request, session, render_template
from json import dumps

logging.basicConfig(level=logging.DEBUG)

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='vault'

@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        #file=request.files['image']
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        image_b64 = request.values['imageBase64']
        image_data=base64.standard_b64decode(re.sub('^data:image/.+;base64,', '', image_b64))
        #image_data = re.sub('^data:image/.+;base64,', '', image_b64).decode('base64')
        with open(os.path.join(app.config['UPLOAD_FOLDER'],'{}.png'.format(str(randint(111111,999999)))), 'wb') as f:
            f.write(image_data)

        return 'this is a post request'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', threaded=True)
