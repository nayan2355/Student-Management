from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("student.db")
    conn.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, roll TEXT, course TEXT)")
    conn.close()
init_db()

@app.route('/', methods=['GET','POST'])
def home():
    conn = sqlite3.connect("student.db")
    if request.method == 'POST':
        conn.execute("INSERT INTO students (name, roll, course) VALUES (?,?,?)",
                     (request.form['name'], request.form['roll'], request.form['course']))
        conn.commit()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)