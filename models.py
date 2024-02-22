from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    description = db.Column(db.Text)
    duration = db.Column(db.Integer)
    date = db.Column(db.String(10))
    time = db.Column(db.String(5))
    status = db.Column(db.Boolean, default=False)  
    report_id = db.Column(db.Integer, db.ForeignKey('task.id'))  #