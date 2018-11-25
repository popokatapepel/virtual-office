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
from flask import Flask, redirect, url_for, jsonify, request, session, render_template
from json import dumps

logging.basicConfig(level=logging.DEBUG)

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='vault'
app.database = Database()
app.secret='SECRET'

@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        image_b64 = request.values['imageBase64']
        image_data = base64.standard_b64decode(re.sub('^data:image/.+;base64,', '', image_b64))
        fpath=os.path.join(app.config['UPLOAD_FOLDER'], '{}.png'.format(str(randint(111111, 999999))))
        with open(fpath, 'wb') as f:
            f.write(image_data)
        return 'this is a post request'

@app.route('/analysis_result', methods=['GET'])
def ana_result():
    fid=request.args.get('id')
    fpath = os.path.join(app.config['UPLOAD_FOLDER'], '{}.png'.format(fid))
    doc2analyse = Doc(fpath)
    doc2analyse.analyse()
    copy(fpath, os.path.join('static', '{}.png'.format(fid)))
    return render_template('result.html',
                           fname='{}.png'.format(fid),
                           sender=doc2analyse.sender,
                           type=doc2analyse.text)





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
