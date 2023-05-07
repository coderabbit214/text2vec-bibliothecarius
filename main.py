from flask import Flask, request, jsonify
from text2vec import SentenceModel

app = Flask(__name__)
model = SentenceModel('text2vec-base-chinese')

@app.route('/vector', methods=['POST'])
def vector():
    embeddings = model.encode(request.json['input'])
    return jsonify(embeddings.tolist())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=False)
