from flask import Flask, request, redirect
from datetime import datetime
import pickle

import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from keras.models import load_model
from keras.utils.np_utils import to_categorical
import re

app = Flask(__name__)

html_css_head_body_start = '''
                <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <title>Günlük</title>
                <style type="text/css">
                html { box-sizing: border-box; }
                *,
                *::before,
                *::after { box-sizing: inherit; }
                body {
                    font-family: sans-serif;
                    margin: 40px;
                    background-image: url(https://i.hizliresim.com/4aBakA.jpg);
                    }
                .mainDiv {
                        width: 1000px;
                        background-color:#FFF;
                        margin: 0 auto;
                        padding: 40px;
                        box-shadow: 0 4px 5px 0 rgba(0, 0, 0, 0.22),
                        0 1px 10px 0 rgba(0, 0, 0, 0.22),
                        0 2px 4px -1px rgba(0, 0, 0, 0.4);
                        margin-top:70px;
                        opacity:0.95;
                        }
                label {
                    display: block;
                    margin-bottom: 10px;
                    font-size: 16px;
                    }
                input {
                    border: 1px solid lightgray;
                    padding: 8px;
                    font-size: 14px;
                    width: 300px;
                    margin-top: 4px;
                    }
                textarea {
                    border: 1px solid lightgray;
                    padding: 8px;
                    font-size: 14px;
                    width: 500px;
                    height: 100px;
                    margin-top: 4px;
                    }
                a:link {
                    color: #630;
                    text-decoration: none;
                    }
                a:visited {
                        text-decoration: none;
                        color: #630;
                        }
                a:hover {
                        text-decoration: none;
                        color: #636;
                        }
                a:active {
                        text-decoration: none;
                        color: #630;
                        }
                a {
                    font-size: 17px;
                    color: #030;
                    font-weight: bold;
                    }
                body,td,th { color: #222; }
                </style>
                </head>
                <body><div class="mainDiv">
  				<table width="1000" border="0"><tr>
                '''

html_css_head_body_end = '</tr></table></div></body></html>'

form = '''
		<form action="/add/" method="post">
		<label>Başlık:<br><input type="text" name="title"></label>
		<label>Yazı:<br><textarea name="entry"></textarea></label>
		<input type="submit" value=' Kaydet '>
		</form>
'''


model = load_model('my_model.h5')

# loading
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


@app.route('/')
def main ():
	return f'{html_css_head_body_start}{get_td()}{html_css_head_body_end}'


@app.route('/add/', methods=['POST'])
def add():
	entry = request.form["entry"]
	title = request.form["title"]
	date = get_date()
	icerik = f'{date}\n{title}\n{entry}\n*-*\n'

	with open('db.txt', 'r') as f:
		veri = f.read()
		f.seek(0)
		f.write(veri + icerik)
	return redirect('/')


@app.route('/hi/')
def hi_world():
	return "<h1>Hi World</h1>"


def get_date():
	today = str(datetime.today())
	today = today.split(" ")
	date = today[0] + today[1][:2] + "-" + today[1][3:5]
	return date


def get_td():
	td_body = ""
	with open('db.txt', 'r') as f:
		veri = f.read()
	veri = veri.split("\n*-*\n")
	for item in veri[:-1]:
		item_ = item.split("\n")
		text = item_[2].split(".")
		text_ = ""
		for sentence in text:
			text_ += analysis_of_text(sentence)
		td_body = f'<i>{item_[0]}</i><br><b>{item_[1]}</b><br>{text}<br><br> <br>' + td_body

	td = f'<td><table width="900"><tr><td>{form}<br> <br> </td></tr><tr><td>{td_body}</td></tr></table</td>'
	return td


def analysis_of_text(text):
	sequences = tokenizer.texts_to_sequences(list(text))
	data = pad_sequences(sequences, maxlen=400)
	predictions = model.predict(data)
	# kızmak, korkmak, mutluluk, üzüntü
	pred = list(predictions[0])
	index = pred.index(max(pred))
	if index == 0:
		return f'<font color="red">{text}</font>'
	elif index == 1:
		return f'<font color="purple">{text}</font>'
	elif index == 2:
		return f'<font color="pink">{text}</font>'
	else:
		return f'<font color="brown">{text}</font>'

if __name__ == "__main__":
	app.run()