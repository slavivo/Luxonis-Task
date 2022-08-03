import psycopg2
from flask import Flask, render_template
from settings import DATABASE

app = Flask(__name__)

@app.route('/')

def index():
    conn = psycopg2.connect(**DATABASE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM flat;')
    flats = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', flats=flats)