import logging
import os
from database import Database, TodoItem
import re
import base64
from random import randint
from ocr.Doc import Doc
from shutil import copy

from random import randint

from PIL import Image
from flask import Flask, flash, redirect, url_for, jsonify, request, session, render_template
from json import dumps
from werkzeug.utils import secure_filename

logging.basicConfig(level=logging.DEBUG)

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='vault'
ALLOWED_EXTENSIONS = set(['png'])

app.database = Database()
app.secret='SECRET'

@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        image_b64 = request.values['imageBase64']
        image_data=base64.standard_b64decode(re.sub('^data:image/.+;base64,', '', image_b64))
        #image_data = re.sub('^data:image/.+;base64,', '', image_b64).decode('base64')
        docId = randint(111111,999999)
        with open(os.path.join(app.config['UPLOAD_FOLDER'],'{}.png'.format(str(docId))), 'wb') as f:
            f.write(image_data)
        return jsonify(
            id=docId
        )

@app.route('/analysisResult', methods=['GET'])
def ana_result():
    fid=request.args.get('id')
    fpath = os.path.join(app.config['UPLOAD_FOLDER'], '{}.png'.format(fid))
    doc2analyse = Doc(fpath)
    doc2analyse.analyse()
    copy(fpath, os.path.join('static', '{}.png'.format(fid)))
    todotext = doc2analyse.getTodotext()
    return render_template('result.html',
                           fname='{}.png'.format(fid),
                           sender=doc2analyse.sender,
                           type=doc2analyse.text,
                           docId = fid,
                           hasTodo=(todotext!=None),
                           todo=todotext)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        file= request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            fid=str(randint(111111, 999999))
            filename = '{}.png'.format(fid)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('ana_result', **dict(id=fid)))

@app.route('/createTodo', methods=['GET'])
def createTodo():
    fid = request.args.get('id')
    fpath = os.path.join(app.config['UPLOAD_FOLDER'], '{}.png'.format(fid))
    doc2analyse = Doc(fpath)
    doc2analyse.analyse()
    todotext = doc2analyse.getTodotext()
    app.database.addTodo(todotext)
    return "ok"

@app.route("/todoList", methods=['GET','POST'])
def todoList():
    if request.method=='GET':
        return render_template('todos.html',todos=app.database.getTodos())
    elif request.method == 'POST':
        id=int(request.form['todoid'])
        done=True if request.form['done']=='true' else False
        app.database.changeTodo(id,done)
        return 'this is a post request'

if __name__ == "__main__":
    #include values in db
    app.database.addTodo('miriam anrufen')
    app.database.addTodo('weihnachtsgeschenke kaufen')
    app.database.changeTodo(0,True)
    app.run(debug=True, host='0.0.0.0', threaded=True)
