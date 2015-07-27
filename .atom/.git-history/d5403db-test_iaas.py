"""
Jobs Plugin
"""
from resources.auth import requires_groups
from flask import Blueprint
import requests

import resources.job_manager as job_manager

API_NAME = "TEST_IAAS"


test_iaas = Blueprint('test_iaas', __name__, url_prefix='/test_iaas')


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
    api_toolkit_url = '127.0.0.1:5000/test_iaas/'
    backend_url = '127.0.0.1:5000/test/start'

    r = requests.post('http://' + backend_url)

    backend_jid = int(r.text)
    return job_manager.start_job(api_toolkit_url, backend_jid)


@test_iaas.route('/status/<int:job_id>', methods=['GET', 'POST'])
def status(job_id):
    """
    Return the status of a job <job_id>
    """
    r = requests.post('http://localhost:5000/test/status/' + str(job_id))
    return str(r.text)


@test_iaas.route('/stop/<backend_jid>', methods=['GET', 'POST'])
# @requires_groups('all-access', 'All Access')
def stop(backend_jid):
    """
    Sends a get request to the backend API (in this case, the simulated API
    called test_api.
    """
    r = requests.post("http://localhost:5000/test/stop/" + str(backend_jid))
    return r.text
