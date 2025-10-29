import random
from flask import Flask, render_template

app = Flask(__name__)

GOOGLE_DRIVE_LINK = "https://drive.google.com/drive/folders/1aWweDKCRF_vrehtr3JQlUwTCTA9Llznv"

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/ran')
def ran():
    return '랜덤 숫자 추출 : <strong>'+str(random.random())+'</strong>'

@app.route('/read/<id>')
def read(id):
    print(id)
    return 'id 값은 바로바로 : ' + id

@app.route('/download')
def download():
    return render_template('download.html', link=GOOGLE_DRIVE_LINK)

@app.route('/web')
def web():
    return render_template('web.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
