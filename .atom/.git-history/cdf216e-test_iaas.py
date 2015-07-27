"""
Jobs Plugin
"""
from resources.auth import requires_groups
from flask import Blueprint, redirect
import requests

from flask import Blueprint
from ..app import app
from resources.auth import requires_groups
import resources.job_manager as job_manager

import requests


API_NAME = "TEST_IAAS"
test_iaas = Blueprint('test_iaas', __name__, url_prefix='/test_iaas')
HOSTNAME = app.config.get('HOSTNAME')


@test_iaas.route('/', methods=['GET', 'POST'])
@requires_groups('all-access', 'All Access')
def index():
    """
    Display welcome message for IAAS
    """
    return "IAAS POC backend API"


@test_iaas.route('/create_image', methods=['GET', 'POST'])
@requires_groups('all-access', 'All Access')
def create_image():
    """
    Create an image for IAAS
    """
    api_toolkit_url = HOSTNAME + '/test_iaas/'
    backend_url = HOSTNAME + '/test/start'

    r = requests.post(backend_url)

    backend_response = r.text
    return job_manager.start_job(api_toolkit_url, backend_response,
                                 start_url, payload)


@test_iaas.route('/create_image_fail', methods=['GET', 'POST'])
@requires_groups('all-access', 'All Access')
def create_image_fail():
    api_toolkit_url = '127.0.0.1:5000/test_iaas/'
    start_url = '127.0.0.1:5000/test/start_no_processes'

    payload = {'key1': 'val1'}
    r = requests.post('http://' + start_url, data=payload)

    backend_response = r.text
    return job_manager.start_job(api_toolkit_url, backend_response,
                                 start_url, payload)


@test_iaas.route('/status/<int:job_id>', methods=['GET', 'POST'])
def status(job_id):
    """
    Return the status of a job <job_id>
    """
    r = requests.post(HOSTNAME + '/test/status/' + str(job_id))
    return str(r.text)


# send post request to backend api, wait for timeout and re-query
@test_iaas.route('/stop/<backend_jid>', methods=['GET', 'POST'])
# @requires_groups('all-access', 'All Access')
def stop(backend_jid):
    """
    Sends a get request to the backend API (in this case, the simulated API
    called test_api.
    """
    r = requests.post(HOSTNAME + "/test/stop/" + str(backend_jid))
    return r.text
