from flask import Flask

app = Flask(__name__)

#-------- Routes ---------------

@app.route('/')
def index():
	return 'Hello. This is my logbook!'

@app.route('/log/add')
def addLog():
    return "This page adds a log entry."

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    # app.dburi = 'sqlite:////vagrant/logbook/db/logbook.db'
    app.run(host='0.0.0.0', port=5000)