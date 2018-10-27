from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    db.create_all()
    uname=str(randint(100000,999999))
    mail='{}@example.com'.format(uname)

    user = User(username=uname, email=mail)

    db.session.add(user)
    db.session.commit()
    return '{} uname added sucessfully'.format(uname)

if __name__ == "__main__":
    app.run(debug=True)
