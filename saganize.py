from flask import Flask
from flask import render_template
from flask import request
import httplib
import urllib

app = Flask(__name__)

def google_search(query):
    url = "/search?q=" + urllib.quote_plus(query)
    conn = httplib.HTTPConnection("www.google.com")
    conn.request("GET", url)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    return saganize_searchpage(data)

def saganize_searchpage(data):
    startIndex = data.find("class=\"sd\"") + 28
    endIndex = data.find("div", startIndex) - 2
    replace_results = data[startIndex : endIndex]
    return data.replace(replace_results, "Billions and billions of results")

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