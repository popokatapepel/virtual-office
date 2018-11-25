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
    return render_template('todos.html',todos=app.database.getTodos())

if __name__ == "__main__":
    #include values in db
    app.database.addTodo(TodoItem('miriam anrufen'))
    app.database.addTodo(TodoItem('weihnachtsgeschenke kaufen'))

    app.run(debug=True, host='0.0.0.0', threaded=True)
