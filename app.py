from flask import Flask


app = Flask(__name__)


@app.route("/status")
def status():
    return("The Authorisation Test Plugin Flask Server is up and running")


@app.route("/run", methods=["GET"])
def run():
    resp = {}

    # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~~~~
    login_url = "www.examples.org"
    login_data = {'email': '<email>', 'username':'<username>','password' : '<password>'}
    login_headers = {'Accept': 'text/plain'}
    login_params = {'email':{'type': 'email', 'description': 'This is the email used for login', 'options': [], 'default': [], 'restrictions': {}},
                    'password': {'type': 'password', 'description': 'This is your password', 'options': [], 'default': [], 'restrictions': {}},
                    'username': {'type': 'text', 'description': 'This is the username for yoru account', 'options': [], 'default': [], 'restrictions': {}}
                   }
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    resp['login_url'] = login_url
    resp['login_data'] = login_data
    resp['login_headers'] = login_headers
    resp['login_parameters'] = login_params
    return resp
