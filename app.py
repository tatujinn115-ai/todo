import sys
sys.path.insert(0, './venv/Lib/site-packages')

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo = request.form.get('todo')
        if todo:
            todos.append(todo)
        return redirect(url_for('index'))
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)
