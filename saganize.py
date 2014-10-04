from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Saganize this!!'

@app.route('/search')
@app.route('/search?q=<query>')
def do_search(query=None):
    #return 'saganized-search on %s' % query
    return render_template('search.html', query = query)

if __name__ == '__main__':
    # auto reloads the server on changes, also enables debugging
    app.debug = True
    # server is publicly available
    app.run(host='0.0.0.0')