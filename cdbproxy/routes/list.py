from flask import Blueprint, jsonify, request, abort
from cdbproxy.common.constants import BASE_URI

"""
List blueprint route.
"""
list_route = Blueprint('list', __name__)

"""
List all cdbproxy instances.
Example HTTP message:
GET /v1/list HTTP/1.1
"""


@list_route.route(BASE_URI + 'list', methods=['GET'])
def create_call():
    return jsonify(instances=['2341241343','34456346345'])
