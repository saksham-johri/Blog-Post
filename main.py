from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def about():
    return render_template('about.html')

def contact():
    return render_template('contact.html')

app.run()