import nltk.data
import nltk
import re
from collections import Counter
from nltk.corpus import stopwords

def parse_and_tokenize(sentence):
	parsed_sent = re.sub(r'([^\s\w]|_)+', '', sentence.lower())
	return nltk.word_tokenize(parsed_sent)

def sentence_and_word_tokenizer():
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	fp = open("assets/train-v2.0.txt", encoding='utf-8', errors='ignore')
	data = fp.read()
	#breaking text into sentences
	sentence_list = tokenizer.tokenize(data)

	#creating a dictionary mapping sentences to an index
	#additionally, indexing each word with what sentences they appear in 
	sentence_dict = {};
	word_dict = {};
	sentence_number_dict = {};
	num = 0;
	for sentence in sentence_list:
		sentence_dict.update({num: sentence})
		sentence_number_dict.update({sentence: num})
		tokens = parse_and_tokenize(sentence)
		for word in tokens:
			word_dict.setdefault(word,set([])).add(num)
		num += 1
	return sentence_dict, word_dict, sentence_number_dict

def find_sentence(s, sentence_dict, word_dict):
	user_tokens = parse_and_tokenize(s)
	stop_words = set(stopwords.words('english')) 
	filtered_sentence = [w for w in user_tokens if not w in stop_words]
	total_sent_indexs = []
	for word in filtered_sentence:
		sent_indexs = word_dict.get(word)
		if sent_indexs is not None:
			total_sent_indexs.extend(sent_indexs)

	cnt = Counter(total_sent_indexs)

	answers = [];
	for sentence_index in [x[0] for x in cnt.most_common(6)]:
		answers.append(sentence_dict[sentence_index]) 

	return answers

def find_close_sentences(number, sentence_dict):
	close_sentences = []
	for x in range(number-5, number + 5):
		close_sentences.append(sentence_dict.get(x))
	return close_sentences