from app import app
from flask import Flask, render_template, url_for

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
  return render_template('index.html')

@app.route('/collection')
@app.route('/collection/<int:cid>')
def collection(cid = 0):
  return render_template('collection.html', cid = cid)
