from flask import Flask
from flask import render_template
from flask import request

import httplib
import urllib
import random

import science_list

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
    return replace_black_bar(add_onebox(replace_num_results(replace_shopping(fix_images(data)))))

def replace_black_bar(data):
    search_skipped = False
    j = 0
    for i in range(len(data)):
        gbts = 'class=gbts'
        if data[i : i + len(gbts)] == gbts:
            sI = i + len(gbts) + 1
            eI = data.find('</span>', i)
            if data[sI : eI] in science_list.gList:
                data = data[:sI] + science_list.new_gList[j] + data[eI:]
                j += 1
    return data

def add_onebox(data):
    onebox = '<li class="g"><div id="_vBb"><span class="_m3b">carl_sagan_cosmos_quote</span><div class="_eGc"> - Carl Sagan, Cosmos </div><br></div></li>'
    sI = data.find('id="ires"') + 14
    return data[:sI] + onebox + data[sI:]

def replace_num_results(data):
    sI = data.find("class=\"sd\"") + 28
    eI = data.find("div", sI) - 2
    replace_results = data[sI : eI]
    return data.replace(replace_results, "Billions and billions of results")

def replace_shopping(data):
    return data.replace("Shopping", "<b>SCIENCE!!</b>")

def fix_images(data):
    img = '<a href="/webhp?hl=en" style="background:url(/images/nav_logo176.png) no-repeat 0 -41px;height:37px;width:95px;display:block" id="logo" title="Go to Google Home"></a>'
    img_replace = '<a href="www.google.com/search?q=carl+sagan" style="margin-left:25px;margin-top:12px;position:absolute;"><img src="http://carlsaganday.com/wp-content/uploads/2013/09/carlsagan.jpg" height="37px"></a>'
    return data.replace(img, img_replace)
    #return data.replace("/images/nav_logo176.png", "http://www.google.com/images/nav_logo176.png").replace("http://www.google.comhttp://www.google.com", "http://www.google.com")
    #return data

def sciencify_query(query):
    return query + ' ' + science_list.sList[random.randint(0, len(science_list.sList) - 1)]

@app.route('/')
def homepage():
    return 'Saganize this!!'

@app.route('/search')
@app.route('/search/<query>')
def do_search(query=None):
    return google_search(sciencify_query(query))
    #return render_template('search.html', query = query)

if __name__ == '__main__':
    # auto reloads the server on changes, also enables debugging
    app.debug = True
    # server is publicly available
    app.run(host='0.0.0.0')