from flask import Blueprint, jsonify, request, abort
from proxclopse.common.constants import BASE_URI

"""
Get blueprint route.
"""
get_route = Blueprint('get', __name__)

"""
Get a proxclopse instance.
Example HTTP message:
GET /v1/<instance_id> HTTP/1.1
"""


@get_route.route(BASE_URI + '<instance_id>', methods=['GET'])
def get_call(instance_id):
    return jsonify(instance_id=instance_id,
                   ip='192.168.1.1',
                   nodes=['192.168.1.2', '192.168.1.3'])
