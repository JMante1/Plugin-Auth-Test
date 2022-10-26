from flask import Flask


app = Flask(__name__)


@app.route("/status")
def status():
    return("The Authorisation Test Plugin Flask Server is up and running")


@app.route("/login", methods=["GET"])
def login():
    resp = {}

    # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~~~~
    login_url = "https://authtesting.synbiohub.org/loggedinAPI"
    login_data = {'email': '<email>', 'username':'<username>','password' : '<password>'}
    login_headers = {'Accept': 'text/plain'}
    login_params = {'email':{'type': 'email', 'description': 'This is the email used for login', 'options': [], 'default': [], 'restrictions': {}},
                    'password': {'type': 'password', 'description': 'This is your password', 'options': [], 'default': [], 'restrictions': {}},
                    'username': {'type': 'text', 'description': 'This is the username for your account', 'options': [], 'default': [], 'restrictions': {}}
                   }
    token_params = {'access':'login_token', 'refresh':'refresh_token'}
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    resp['login_url'] = login_url
    resp['login_data'] = login_data
    resp['login_headers'] = login_headers
    resp['login_parameters'] = login_params
    resp['token_parameters'] = token_params
    return resp

@app.route("/refresh", methods=["GET"])
def refresh():
    resp = {}

    # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~~~~
    refresh_exists = True
    refresh_url = "https://authtesting.synbiohub.org/refresh"
    refresh_data = {'refresh_token':'<refresh>'}
    refresh_headers = {}
    refresh_token_name = 'refresh_token'
    token_params = {'access':"login_token"}
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if refresh_exists:
        resp['refresh_url'] = refresh_url
        resp['refresh_data'] = refresh_data
        resp['refresh_headers'] = refresh_headers
        resp['refresh_token_name'] = refresh_token_name
        resp['token_parameters'] = token_params
        return resp
    else:
        return 'This login does not provide refresh tokens', 503

@app.route("/logout", methods=["GET"])
def logout():
    resp = {}

    # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~~~~
    logout_exists = True
    logout_url = "https://authtesting.synbiohub.org/logoutAPI"
    logout_data = {'login_token':'<login_token>'}
    logout_headers = {}
    login_token_name = 'login_token'
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if logout_exists:
        resp['logout_url'] = logout_url
        resp['logout_data'] = logout_data
        resp['logout_headers'] = logout_headers
        resp['login_token_name'] = login_token_name
        return resp
    else:
        return 'This login does not provide a logout endpoint', 503
