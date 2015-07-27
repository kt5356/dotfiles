"""
Help plugin
"""
from ..auth import requires_groups
from ..views import get_routes
from flask import Blueprint, jsonify

help = Blueprint('help', __name__, url_prefix='/help')

@help.route('/', methods=['GET', 'POST'])
@requires_groups('all-access')
def show_help():
    """
    Display all available page routes.
    """
    routes = get_routes()
    return jsonify(pages=routes)

@help.route('/<api_name>', methods=['GET', 'POST'])
@requires_groups('all-access')
def api_help(api_name):
    """
    Display all available page routes whose name partially
    match the <api_name> supplied in the URL.
    """
    routes = get_routes()
    matching = [s for s in routes if api_name in s]
    return jsonify(pages=matching)

@help.route('/hello', methods=['GET', 'POST'])
@requires_groups('all-access')
def hello():
    """
    Display all available page routes whose name partially
    match the <api_name> supplied in the URL.
    """
    return "hello"
