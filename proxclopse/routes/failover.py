from flask import Blueprint, jsonify, request, abort
from proxclopse.common.constants import BASE_URI

"""
Get blueprint route.
"""
failover_route = Blueprint('failover', __name__)

"""
Failover a proxclopse instance.
Example HTTP message:
POST /v1/<instance_id>/failover HTTP/1.1
"""


@failover_route.route(BASE_URI + '<instance_id>/failover', methods=['POST'])
def failover_call(instance_id):
    return jsonify(instance_id=instance_id,
                   status=True)
