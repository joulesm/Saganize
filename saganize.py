from flask import Flask
from flask import render_template
from flask import request
import httplib

app = Flask(__name__)

def google_search(query):
    url = "/search?q=" + query
    conn = httplib.HTTPConnection("www.google.com")
    conn.request("GET", url)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    return data

@app.route('/')
def homepage():
    return 'Saganize this!!'

@app.route('/search')
@app.route('/search/<query>')
def do_search(query=None):
    return google_search(query)
    #return render_template('search.html', query = query)

if __name__ == '__main__':
    # auto reloads the server on changes, also enables debugging
    app.debug = True
    # server is publicly available
    app.run(host='0.0.0.0')