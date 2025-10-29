from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!doctype html>
    <html>
      <body style="text-align:center;">
          <h1>이미지 테스트</h1>
          <img src="/static/img.jpg" width="400">
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
