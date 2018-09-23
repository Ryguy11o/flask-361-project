from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import custom_parser as parser

print('Starting parsing')
sentence_dict, word_dict, sentence_number_dict = parser.sentence_and_word_tokenizer()
print('Done Parsing')

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

@app.route('/getAnswers', methods=['POST'])
def getAnswers():
    data = request.data
    dataDict = json.loads(data)
    answers = parser.find_sentence(dataDict['question'], sentence_dict, word_dict)
    return jsonify(answers)

@app.route('/getParagraph', methods=['POST'])
def getParagraph():
	data = request.data
	dataDict = json.loads(data)
	number = sentence_number_dict[dataDict['sentence']]

	close_sentences = parser.find_close_sentences(number, sentence_dict)
	return jsonify(close_sentences)

if __name__ == '__main__':
    app.run(use_reloader=False)