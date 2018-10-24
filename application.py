from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
import os


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
    ]
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["email"])

if __name__ == "__main__":
    app.run()