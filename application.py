import logging
import os

from random import randint
from flask import Flask, redirect, url_for, jsonify, request, session, render_template
from json import dumps

logging.basicConfig(level=logging.DEBUG)

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='vault'

@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('photo.html')
    elif request.method=='POST':
        file=request.files['image']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'this is a post request'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', threaded=True)
