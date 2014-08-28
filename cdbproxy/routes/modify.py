from flask import Blueprint, jsonify, request, abort
from cdbproxy.common.constants import BASE_URI

"""
Get blueprint route.
"""
modify_route = Blueprint('modify', __name__)

"""
Modify a cdbproxy instance.
Example HTTP message:
POST /v1/<instance_id> HTTP/1.1
"""


@modify_route.route(BASE_URI + '<instance_id>', methods=['POST'])
def modify_call(instance_id):
    return jsonify(instance_id=instance_id,
                   ip='192.168.1.1',
                   nodes=['192.168.1.2', '192.168.1.3'])
