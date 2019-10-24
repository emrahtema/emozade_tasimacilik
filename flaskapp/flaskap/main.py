from flask import Flask, request, redirect

app = Flask(__name__)

entries = [
	{
		'username': 'Günay',
		'entry': 'selam ^^'
	},
	{
		'username': 'Betty',
		'entry': 'unicorn'
	}
]


@app.route('/')
def questbook():
	title = '<h1>hello world</h1>'
	form = "<form action='/add/' method='post'>"
	form += "<p>username: <input type='text' name='username'></p>"
	form += "<p>entry: <textarea name='entry'></textarea></p>"
	form += "<input type='submit' value='OKAY'>"
	form += "</form>"
	body = '<div>'
	for entry in entries:
		body += f"<strong>{entry['username']}</strong>"
		body += f"<p>{entry['entry']}</p>"
	body += '</div>'
	return f'{title}{form}{body}'

@app.route('/add/', methods=['POST'])
def add():
	global entries
	entries.append(request.form)
	return redirect('/')


@app.route('/hi/')
def hi_world():
	return "<h1>Hi World</h1>"


if __name__ == "__main__":
	app.run()