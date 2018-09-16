#!/usr/bin/python3

from flask import flash, render_template, request, redirect, Flask
from forms import ProductSearchForm
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search = ProductSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form = search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        query = urllib.parse.quote(search)
        url = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        results = print (soup)

    if not results:
        flash('No results found!!')
        return redirect('/')
    else:
        print ('bye')



if __name__ == '__main__':
    app.run()
     

