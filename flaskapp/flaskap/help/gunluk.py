from flask import Flask, request, redirect

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
                    font-size: 18px;
                    }
                input {
                    border: 1px solid lightgray;
                    padding: 8px;
                    font-size: 18px;
                    width: 300px;
                    margin-top: 4px;
                    }
                textarea {
                    border: 1px solid lightgray;
                    padding: 8px;
                    font-size: 18px;
                    width: 500px;
                    height: 150px;
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


@app.route('/')
def main ():
	return f'{html_css_head_body_start}{get_td1()}{get_td2()}{html_css_head_body_end}'


@app.route('/add/', methods=['POST'])
def add():
	global entries
	entries.append(request.form)
	return redirect('/')


@app.route('/hi/')
def hi_world():
	return "<h1>Hi World</h1>"


def get_td1():
	td = f'<td width="300">...</td>'
	return td


def get_td2():
	td_body = ""
	td = f'<td><table width="700"><tr><td>{form}</td></tr><tr><td>{td_body}</td></tr></table</td>'
	return td

if __name__ == "__main__":
	app.run()