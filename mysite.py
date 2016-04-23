# Flask libraries
from flask import Flask, render_template
app = Flask(__name__)

# Python libraries
import subprocess

# Main app
@app.route('/')
def hello_world():
    info = {}
    info['uptime'] = subprocess.check_output(['uptime -s'], shell=True)
    return render_template('index.html', info=info)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
