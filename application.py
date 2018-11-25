import logging
import os
import * from database

from random import randint
from flask import Flask, redirect, url_for, jsonify, request, session, render_template
from json import dumps

logging.basicConfig(level=logging.DEBUG)

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='vault'
app.database = Database()

@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        #file=request.files['image']
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'this is a post request'

@app.route("/todoList", methods=['GET','POST'])
def todoList():
    render_template('todos.html',todos=app.Database.getTodos())
    pass

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', threaded=True)
