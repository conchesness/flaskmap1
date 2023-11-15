
from app import app
import os
from flask import render_template
from .locations import locations

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/map')
def map():
    return render_template('map.html',locations=locations)