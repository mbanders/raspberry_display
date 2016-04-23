# Flask libraries
from flask import Flask, render_template
app = Flask(__name__)

# Python libraries
import datetime
import re
import subprocess

prev_info = {'time': datetime.datetime.now(), 'rx_mbytes': 0, 'tx_mbytes':0}

# Main app
@app.route('/')
def hello_world():
    global prev_info
    info = {}
    iface = 'eth0'
    ifconfig = subprocess.check_output("ifconfig %s" % iface, shell=True)
    info['time'] = datetime.datetime.now()
    info['rx_mbytes'] = int(re.search(' RX bytes:(\d+) ', ifconfig).group(1))/125000.
    info['tx_mbytes'] = int(re.search(' TX bytes:(\d+) ', ifconfig).group(1))/125000.
    info['rx_rate'] = (info['rx_mbytes'] - prev_info['rx_mbytes']) / (info['time'] - prev_info['time']).total_seconds()
    info['tx_rate'] = (info['tx_mbytes'] - prev_info['tx_mbytes']) / (info['time'] - prev_info['time']).total_seconds()
    info['rx_rate'] = "%.2f" % info['rx_rate']
    info['tx_rate'] = "%.2f" % info['tx_rate']
    info['uptime'] = subprocess.check_output('uptime -p', shell=True)
    prev_info = info
    return render_template('index.html', info=info)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
