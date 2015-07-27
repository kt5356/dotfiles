#!/usr/bin/env python
""" Basic API front end.
"""

from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
from flask import abort
from flask import redirect
from utils import requires_auth
from jenkins_job import request_build
from os import path
from tempfile import mktemp
from repo import IAASRepo

APP = Flask(__name__)


@APP.route('/quickbuild/<rpmname>', methods=['POST'])
@requires_auth
def quickbuild_image(rpmname):
    """ Shortcut method to quickly allow the creation of an image with an rpm.

    This will generate a job for Jenkins with the rpm passed in as a parameter.
    A link to the

    :param rpmname: The name of the rpm to use in the images
    :type rpmname: str
    :reqheader Authorization: Basic HTTP authentication
    :statuscode 303: The uri to the Jenkins job.
    :statuscode 401: Authentication Required
    :statuscode 404: RPM was not found in the repo.
    """

    repo = IAASRepo(APP.config.get('REPO_DIR'))
    if rpmname not in repo.list():
        abort(404)

    build_url = request_build(
        APP.config.get('JENKINS_URL'),
        APP.config.get('JENKINS_USER'),
        APP.config.get('JENKINS_PASS'),
        APP.config.get('JENKINS_JOB'),
        {'RPM': rpmname}
    )

    return redirect(build_url, code=303)


@APP.route('/repo/', methods=['GET'])
@requires_auth
def repo_list():
    """ Returns a list of rpm names in json format

    .. code-block:: javascript

        {
            "rpms": [
                "rpm1.rpm",
                "rpm2.rpm",
                .......
            ]
        }

    For security reasons, this is returned in as a dict rather than a list.
    See http://flask.pocoo.org/docs/0.10/security/#json-security

    :reqheader Authorization: Basic HTTP authentication
    :statuscode 200: List of available RPM files.
    :statuscode 401: Authentication Required.
    """
    repo = IAASRepo(APP.config.get('REPO_DIR'))
    return jsonify(rpms=repo.list())


@APP.route('/repo/', methods=['POST'])
@requires_auth
def repo_add_rpm():
    """ Upload a RPM to the repo.

    Accepts multipart/form-data request. To upload using `curl` use:

    .. code-block:: bash

        curl -F 'test=@example.rpm' http://$url/repo/

    :form rpm: The contents of the RPM file.
    :reqheader Authorization: Basic HTTP authentication
    :statuscode 201: URI to newly created rpm
    :statuscode 303: The rpm alread exists at the returned URI
    :statuscode 401: Authentication Required
    """
    filedata = request.files['rpm']
    temp_rpm = mktemp()
    if filedata:
        filedata.save(temp_rpm)
        repo = IAASRepo(APP.config.get('REPO_DIR'))
        name = repo.add(temp_rpm)
        return '%s\n' % name
    else:
        return 'nope\n'


@APP.route('/repo/<rpmname>', methods=['GET'])
@requires_auth
def repo_get_rpm(rpmname):
    """Return a named rpm

    :param rpmname: The name of the rpm to return
    :type rpmname: str
    :reqheader Authorization: Basic HTTP authentication
    :statuscode 200: RPM successfully returned
    :statuscode 401: Authentication Required
    :statuscode 404: RPM not found
    """
    repo = IAASRepo(APP.config.get('REPO_DIR'))
    if rpmname in repo.list():
        return send_file(
            path.join(repo.repodir, rpmname),
            mimetype='application/x-rpm',
            as_attachment=True,
            attachment_filename=rpmname
        )
    else:
        abort(404)


@APP.route('/template/', methods=['GET'])
@requires_auth
def job_get_list():
    """ Return a list of known jobs for the user

    .. code-block:: javascript

        {
            "jobs": [
                {'id': identifier, 'status': status},
                {'id': identifier, 'status': status},
                ...
            ]
        }

    :reqheader Authorization: Basic HTTP authentication.
    :statuscode 200: List of available RPM files.
    :statuscode 401: Authentication Required
    """


@APP.errorhandler(404)
def custom404(error):
    """ Custom JSON 404
    """
    return jsonify(text=str(error)), 404


@APP.after_request
def gnu_terry_pratchett(resp):
    """ http://www.gnuterrypratchett.com
    """
    resp.headers.add("X-Clacks-Overhead", "GNU Terry Pratchett")
    return resp

if __name__ == '__main__':
    APP.config.from_envvar('API_CONFIG')
    APP.run()
