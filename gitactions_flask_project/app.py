import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    print(cpu_percent,"memory",mem_percent)
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High Cpu or memory detected please scale up the infra"
        
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=Message)

if __name__=='__main__':
    app.run(debug = True, host = '0.0.0.0')