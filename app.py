# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from jinja2.loaders import split_template_path

app = Flask(__name__)

# ブラウザに画面を表示
@app.route('/', methods=['GET'])
def get():
    return render_template('index.html')


#ブラウザからのデータ取得
@app.route('/', methods={'POST'})
def index():
    speaker_action = request.form.get('speaker_action')
    if speaker_action == '送信':
        speaker_text = request.form.get('speaker_text')
        print(speaker_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run("0.0.0.0")