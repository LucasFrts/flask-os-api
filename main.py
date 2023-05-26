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
        search_html = response.text
        return Response(dumps({'data': search_html}), mimetype='application/json')

if __name__ ==  '__main__':
    app.run()