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
        response_text = response.text
        soup = BeautifulSoup(response_text, 'html.parser')
        for script in soup.find_all('script'):
            script.decompose()
        html_processado = str(soup)

        return Response(dumps({'data': html_processado}), mimetype='application/json')
    else: return Response(dumps({'data':[], 'message':'um erro ocorreu'}), mimetype='application/json')

if __name__ ==  '__main__':
    app.run()