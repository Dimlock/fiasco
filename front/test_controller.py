from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    items = ['Первый элемент', 'Второй элемент', 'Третий элемент']
    return render_template("test_index.html", items=items)


app.run(debug=True)
