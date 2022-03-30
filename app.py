from flask import Flask, render_template, request

import DB_manager

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html')
    else:  # request.method == 'POST'
        user_email = request.form['email']
        if DB_manager.sign_in(user_email):
            return render_template('homepage.html')
        else:
            return render_template('sign_in.html')


@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


if __name__ == '__main__':
    app.run(debug=True)
