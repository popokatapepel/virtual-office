import logging
import os

from random import randint
from flask import Flask, redirect, url_for, jsonify, request, session
from flask_dance.contrib.google import make_google_blueprint, google
from json import dumps

logging.basicConfig(level=logging.DEBUG)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

GOOGLE_CLIENT_ID = '813328546679-6pjo7e8bbulkevrfjpjoj1pka9vgrh79.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '5YK2VbZbAchrnbUI0r3NuGPU'

app = Flask(__name__)
app.secret_key = "supersekrit"
blueprint = make_google_blueprint(
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    scope=[
        "https://www.googleapis.com/auth/plus.me",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/drive"
    ]
)
app.register_blueprint(blueprint, url_prefix="/login")


@app.route("/")
def index():
    print(request.headers.get('User-Agent'))
    if not google.authorized:
        return redirect(url_for("google.login"))
    userinfo = google.get("/oauth2/v2/userinfo")
    assert userinfo.ok, userinfo.text
    drive = google.get("/drive/v3/about?fields=maxUploadSize")
    assert drive.ok, drive.text
    drive1 = google.get("/drive/v3/files")
    return jsonify(drive.json())
    # return "You are {email} on Google".format(email=userinfo.json()["email"])


@app.route('/upload')
def upload():
    fname = 'filetoupload.jpeg'
    with open(fname, 'rb') as f:
        contents = f.read()

    upload_response = google.post('/upload/drive/v3/files', headers=dict(uploadType='media'), data=contents)

    assert upload_response.ok, upload_response.text

    print(upload_response.json())
    session['fid']=upload_response.json()['id']

    update_uri = 'https://www.googleapis.com/drive/v3/files/' + upload_response.json()['id']
    headers = {'content-type': 'application/json'}
    payload = {"name": fname}

    update_resp = google.patch(update_uri, data=dumps(payload), headers=headers)

    assert update_resp.ok, update_resp.text

    return jsonify(update_resp.json())


@app.route('/download')
def download():
    """
    this method downloads the same file as uploaded
    :return:
    """

    update_uri = '/drive/v3/files/' + session['fid'] + '?alt=media'

    down_resp = google.get(update_uri)

    assert down_resp.ok, down_resp.text

    fname = str(randint(1000, 9999)) + '.jpg'
    with open(fname, 'wb') as f:
        f.write(down_resp.content)


    return down_resp.text

if __name__ == "__main__":
    app.run(debug=True)
