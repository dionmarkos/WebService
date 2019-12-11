#pip install Flask
#extensão Postman https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en
from flask import Flask
from flask import request

aplicacao = Flask(__name__)

@aplicacao.route('/postjson', methods=['POST'])
def post():
    print(request.is_json)
    conteudo = request.get_json()
    print('ID: ' + conteudo['id'])
    print('Nome: ' + conteudo['name'])
    return 'JSON publicado com sucesso.'

aplicacao.run(host='0.0.0.0', port=5000)
