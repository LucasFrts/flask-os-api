from flask import Flask, Response, request
from flask_cors import CORS
from bs4 import BeautifulSoup
from bson.json_util import dumps
import json, requests

app = Flask(__name__)
CORS(app)


@app.route('/getSiteFromUrl', methods = ['POST'])
def seach():
    data = json.loads(request.data)
    query = data['query']
    response = requests.get(query)
    if response.status_code == 200:
        with open('main.js', 'r') as file:
            js_code = file.read()

        response_text = response.text
        soup = BeautifulSoup(response_text, 'html.parser')
        anchors = soup.find_all('a')
        
        for anchor in anchors:
            if anchor.text != '#':
                anchor['onClick'] = 'function(event){event.preventDefault(); sendUrlToScrapApplication(event);}()'

        for script in soup.find_all('script'):
            script.decompose()

        script_tag = soup.new_tag('script')
        script_tag.string = f'(function(){{\n{js_code}\n}})();'

        body_tag = soup.find('body')
        body_tag.insert(0, script_tag)
        html_processado = str(soup)

        return Response(dumps({'data': html_processado}), mimetype='application/json')
    else: return Response(dumps({'data':[], 'message':'um erro ocorreu'}), mimetype='application/json')

@app.route('/getNextPageUrl', methods=['POST'])
def search_next():
    data    = json.loads(request.data)
    query   = data['link']


if __name__ ==  '__main__':
    app.run()