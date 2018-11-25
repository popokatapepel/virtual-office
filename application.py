import logging
import os
from database import Database, TodoItem

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
