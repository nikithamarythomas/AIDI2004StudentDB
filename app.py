from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    amount_due = db.Column(db.Float, nullable=False)

# Serve the home page
@app.route('/')
def home():
    return render_template('home.html')

# Add Student Page
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        data = request.form
        new_student = Student(
            student_id=int(data['student_id']),
            first_name=data['first_name'],
            last_name=data['last_name'],
            dob=datetime.strptime(data['dob'], '%Y-%m-%d').date(),
            amount_due=float(data['amount_due'])
        )
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('students_list'))
    return render_template('add_student.html')

# View Students Page
@app.route('/view')
def students_list():
    students = Student.query.all()
    return render_template('students_list.html', students=students)

# Delete Student
@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('students_list'))

# Update Student Page
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        data = request.form
        student.student_id = int(data['student_id'])
        student.first_name = data['first_name']
        student.last_name = data['last_name']
        student.dob = datetime.strptime(data['dob'], '%Y-%m-%d').date()
        student.amount_due = float(data['amount_due'])
        db.session.commit()
        return redirect(url_for('students_list'))
    return render_template('update_student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
