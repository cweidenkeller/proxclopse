from flask import Blueprint, jsonify, request, abort
from cdbproxy.common.constants import BASE_URI

"""
Delete blueprint route.
"""
delete_route = Blueprint('delete', __name__)

"""
Create a cdbproxy instance.
Example HTTP message:
DELETE /v1/<instance_id> HTTP/1.1
"""


@delete_route.route(BASE_URI + '<instance_id>', methods=['DELETE'])
def delete_call(instance_id):
    return jsonify(instance_id=instance_id)
