"""
Jobs Plugin
"""
from resources.auth import requires_groups
from flask import Blueprint, jsonify
import requests
from ..error import Unavailable

import resources.job_manager as job_manager

API_NAME = "IAAS"


iaas = Blueprint('iaas', __name__, url_prefix='/iaas')
IAAS_URL = 'http://127.0.0.1:3000'


@iaas.route('/quickbuild/<rpmname>', methods=['GET', 'POST'])
@requires_groups('all-access', 'All Access')
def quickbuild(rpmname):
    """
    Contact the IAAS server and make a request to build an image.
    """
    try:
        r = requests.post(IAAS_URL + '/quickbuild/' + rpmname)
    except requests.ConnectionError:
        raise Unavailable
    return jsonify(r.json())
