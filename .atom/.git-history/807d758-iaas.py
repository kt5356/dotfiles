"""
Jobs Plugin
"""
from resources.auth import requires_groups
from flask import Blueprint
import requests

import resources.job_manager as job_manager

API_NAME = "IAAS"


iaas = Blueprint('iaas', __name__, url_prefix='/iaas')


@iaas.route('/', methods=['GET', 'POST'])
@requires_groups('all-access', 'All Access')
def index():
    """
    Display welcome message for IAAS
    """
    return "IAAS POC backend API"


@iaas.route('/create_image', methods=['GET', 'POST'])
@requires_groups('all-access', 'All Access')
def create_image():
    """
    Create an image for IAAS
    """
    api_toolkit_url = '127.0.0.1:5000/iaas/'
    backend_url = '127.0.0.1:5000/test/start'

    payload = {'key1': 'val1'}
    r = requests.post('http://' + backend_url, data=payload)

    backend_jid = int(r.text)
    return job_manager.start_job(api_toolkit_url, backend_jid)


@iaas.route('/status/<int:job_id>', methods=['GET', 'POST'])
def status(job_id):
    r = requests.post('http://localhost:5000/test/status/' + str(job_id))
    return str(r.text)


# send post request to backend api, wait for timeout and re-query
@iaas.route('/stop/<backend_jid>', methods=['GET', 'POST'])
# @requires_groups('all-access', 'All Access')
def stop(backend_jid):
    """
    Sends a get request to the backend API (in this case, the simulated API
    called test_api.
    """
    r = requests.post("http://localhost:5000/test/stop/" + str(backend_jid))
    return r.text
