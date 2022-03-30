from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('sign_in.html')
@app.route()
def sign_in():
    return None

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


if __name__ == '__main__':
    app.run(debug=True)
