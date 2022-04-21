from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route("/")

def displayJobDetails():
    response = requests.get("https://raw.githubusercontent.com/at-n-t/pythonBeautifulSoup/main/jobDetails.json")
    responseJSON = response.json()
    return render_template('index.html', responseJSON = responseJSON)