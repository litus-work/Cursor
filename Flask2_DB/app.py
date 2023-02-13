from flask import Flask, request, render_template, redirect, url_for, g

from database import Database

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = Database()
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index_page():
    db = get_db()
    messages = db.get_messages()
    return render_template('index.html', messages=messages)


@app.route('/send', methods=['POST'])
def send():
    db = get_db()
    text = request.form['text']
    if text:
        db.add_message(text)
    return redirect(url_for('index_page'))


if __name__ == '__main__':
    app.db = get_db()
    app.db.create_table()
    app.run(debug=True)
