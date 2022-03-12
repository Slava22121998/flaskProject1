import json

from flask import Flask, render_template

with open("candidates.json", encoding='UTF-8') as f:
    data = json.load(f)

app = Flask(__name__)


@app.route('/')
def info1_page():
    return render_template('info1.html', candidates=data)


@app.route('/candidate/<int:uid>')
def info2_page(uid):
    return render_template('info2.html', candidates=data, id=uid)


@app.route('/skill/<skill>')
def info3_page(skill):
    return render_template('info3.html', candidates=data, skill=skill)


if __name__ == '__main__':
    app.run()
