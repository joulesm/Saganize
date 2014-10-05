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
    return fix_images(saganize_searchpage(data))

def saganize_searchpage(data):
    return replace_num_results(fix_images(data))

def replace_num_results(data):
    sI = data.find("class=\"sd\"") + 28
    eI = data.find("div", sI) - 2
    replace_results = data[sI : eI]
    return data.replace(replace_results, "Billions and billions of results")

def fix_images(data):
    img = '<a href="/webhp?hl=en" style="background:url(/images/nav_logo176.png) no-repeat 0 -41px;height:37px;width:95px;display:block" id="logo" title="Go to Google Home"></a>'
    img_replace = '<a href="www.google.com/search?q=carl+sagan"><img src="http://carlsaganday.com/wp-content/uploads/2013/09/carlsagan.jpg" height="37px" width="95px"></a>'
    return data.replace(img, img_replace)
    #return data.replace("/images/nav_logo176.png", "http://www.google.com/images/nav_logo176.png")

@app.route('/')
def homepage():
    return 'Saganize this!!'

@app.route('/search')
@app.route('/search/<query>')
def do_search(query=None):
    science_query = query + ' carl sagan'
    return google_search(science_query)
    #return render_template('search.html', query = query)

if __name__ == '__main__':
    # auto reloads the server on changes, also enables debugging
    app.debug = True
    # server is publicly available
    app.run(host='0.0.0.0')