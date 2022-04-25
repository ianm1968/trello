from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    response=requests.get('https://api.nasa.gov/planetary/apod', params={'api_key':os.getenv('API_KEY')})
    content=response.json()
    return render_template('index.html', landing_image=content['hdurl'])

@app.route('/mars')
def mars():
    camera=request.args.get('camera', 'FHAZ')
    response=requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000', params={'api_key':os.getenv('API_KEY'), 'camera':camera})
    content=json.loads(response.content)
    images = content['photos']
    image = images[0]
    return render_template('mars.html', landing_image = image['img_src'])