from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'lea'
app.config['MYSQL_PASSWORD'] = '-' 
app.config['MYSQL_DB'] = 'todo_db'

mysql = MySQL(app)
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    cur.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        name_task = request.form.get('name_task')
        deadline = request.form.get('deadline')
        print(f"name_task: {name_task}, deadline: {deadline}")  # Debugging
        if name_task and deadline:
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO tasks (name_task, deadline) VALUES (%s, %s)', (name_task, deadline))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('index'))
    return render_template('add_task.html')



@app.route('/remove', methods=['POST'])
def remove_task():
    task_name = request.form['task_name']
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tasks WHERE name_task = %s', (task_name,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
