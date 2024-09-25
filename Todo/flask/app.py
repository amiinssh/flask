from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)

# Create the database tables
with app.app_context():
    db.create_all()

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        todo_title = request.form['title']
        todo_desc = request.form['desc']
        data = Todo(title=todo_title, desc=todo_desc)
        db.session.add(data)
        db.session.commit() 

    alltodo = Todo.query.all()
    return render_template('index.html', alltodo=alltodo)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo_to_update = Todo.query.get_or_404(sno)
    if request.method == 'POST':
        todo_to_update.title = request.form['title']
        todo_to_update.desc = request.form['desc']
        db.session.commit()
        return redirect('/')
    
    return render_template('update.html', todo=todo_to_update)

@app.route('/delete/<int:sno>', methods=['POST'])
def delete(sno):
    todo_to_delete = Todo.query.get_or_404(sno)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
