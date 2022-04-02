import os

from flask import Flask, render_template, request, make_response, redirect, url_for

import DB_manager
import MainAnalyzer
import base64

import generate_graph_from_list
import generate_random_id

UPLOAD_FOLDER = './upload'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST', 'GET'])
def sign_in():
    if are_cookies_valid():
        return redirect(url_for('homepage'))
    if request.method == 'GET':
        return render_template('sign_in.html')
    else:  # request.method == 'POST'
        user_email = request.form['email']
        result = DB_manager.sign_in(user_email)
        if result:
            resp = make_response(homepage(name=result['name'], preferred_color=result['preferred_color']))
            resp.set_cookie('name', result['name'])
            resp.set_cookie('email', result['email'])
            resp.set_cookie('preferred_color', result['preferred_color'])
            return resp
        else:
            return render_template('sign_in.html')


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if are_cookies_valid():
        return redirect(url_for('homepage'))

    if request.method == 'GET':
        return render_template('sign_up.html')
    else:  # request.method == 'POST'
        user_name = request.form['name']
        user_email = request.form['email']
        user_preferred_color = request.form['preferred_color']
        if DB_manager.sign_up(user_name, user_email, user_preferred_color):
            resp = make_response(render_template('homepage.html',
                                                 name=user_name,
                                                 preferred_color=user_preferred_color))
            resp.set_cookie('name', user_name)
            resp.set_cookie('email', user_email)
            resp.set_cookie('preferred_color', user_preferred_color)
            return resp
        else:
            return redirect('sign_up.html')


@app.route('/logout', methods=['GET'])
def logout():
    resp = make_response(render_template('sign_in.html'))
    resp.delete_cookie('name')
    resp.delete_cookie('email')
    resp.delete_cookie('preferred_color')
    return resp


@app.route('/homepage', methods=['GET'])
def homepage(**kwargs):
    if are_cookies_valid():
        return render_template('homepage.html', **kwargs)
    return redirect(url_for('sign_in'))


@app.route('/upload_img', methods=['POST'])
def upload_img():
    if 'myfile' not in request.files:
        return redirect(url_for('logout'))
    myfile = request.files['myfile']
    file_extension = myfile.filename[myfile.filename.rfind('.'):]
    rand_id = generate_random_id.generate_id(8)
    path = os.path.join(app.config['UPLOAD_FOLDER'], rand_id + file_extension)
    myfile.save(path)
    dominant_emotion = go_to_analyzer(request.cookies.get('email'), path)

    # After analyzing same image is with emotion in same path
    img_base64_string = img_to_base64(path)
    img_base64_string = 'data:image/png;base64,' + img_base64_string
    return render_template('image_preview.html', img_src=img_base64_string, emotion=dominant_emotion)


@app.route('/camera_img', methods=['POST'])
def camera_img():
    rand_id = generate_random_id.generate_id(8)
    image_content = request.form['base64'].replace('data:image/png;base64,', '').encode()
    path = os.path.join(app.config['UPLOAD_FOLDER'], f'{rand_id}.png')
    img = base64_to_img(image_content)
    with open(path, 'wb') as f:
        f.write(img)
    dominant_emotion = go_to_analyzer(request.cookies.get('email'), path)

    # After analyzing same image is with emotion in same path
    img_base64_string = img_to_base64(path)
    img_base64_string = 'data:image/png;base64,' + img_base64_string
    return render_template('image_preview.html', img_src=img_base64_string, emotion=dominant_emotion)


def base64_to_img(image_content):
    return base64.decodebytes(image_content)


def img_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
    os.remove(image_path)
    return encoded_string.decode()


def go_to_analyzer(email, image_path):
    return MainAnalyzer.analyze_and_update(email, image_path)


@app.route('/view_graph', methods=['GET'])
def view_graph():
    path = generate_graph_from_list.generate_graph(request.cookies.get('name'), request.cookies.get('email'))

    img_base64_string = img_to_base64(path)
    img_base64_string = 'data:image/png;base64,' + img_base64_string
    return render_template('daily_graph.html', img_src=img_base64_string)


def are_cookies_valid():
    cookie_name = request.cookies.get('name')
    cookie_email = request.cookies.get('email')
    cookie_preferred_color = request.cookies.get('preferred_color')
    if None not in [cookie_name, cookie_email, cookie_preferred_color]:
        return DB_manager.exists(cookie_name, cookie_email, cookie_preferred_color)
    return False


if __name__ == '__main__':
    app.run(debug=True)
