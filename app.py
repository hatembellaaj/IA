import subprocess



from flask import Flask

app = Flask(__name__)



def run_command():

    return subprocess.Popen('python IAServicePython.py', shell=True, stdout=subprocess.PIPE).stdout.read()



@app.route('/')

def command_server():

    return run_command()