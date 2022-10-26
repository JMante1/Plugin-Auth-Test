# Plugin-Auth-Test
A very small test plugin to test the authorisation interface is working for SynBioHub. Could be the basis for other python based authorisation plugins. The plugin has a status, login, refresh, and logout endpoint. The login, refresh, and logout endpoints returns the format required for an API request to the relevant endpoints. It can be tested using the server found at: https://github.com/SynBioHub/Auth-Testing

# Install
## Using docker
Run `docker run --publish 8101:5000 --detach --name python-auth-test-plug synbiohub/plugin-auth-test:snapshot`
Check it is up using localhost:8101.  

## Using Python
Run `pip install -r requirements.txt` to install the requirements. Then run `FLASK_APP=app python -m flask run`. A flask module will run at localhost:5000/.
