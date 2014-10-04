from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Saganize this!!'

@app.route('/search')
def search():
    return 'saganized-search'


if __name__ == '__main__':
    # auto reloads the server on changes, also enables debugging
    app.debug = True
    # server is publicly available
    app.run(host='0.0.0.0')