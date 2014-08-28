from flask import Blueprint, jsonify, request, abort
from proxclopse.common.constants import BASE_URI

"""
Update acl blueprint route.
"""
set_acl_route = Blueprint('set_acl', __name__)

"""
Update acl's on a proxclopse instance.
Example HTTP message:
PUT /v1/create HTTP/1.1
"""


@set_acl_route.route(BASE_URI + '<instance_id>/set_acl', methods=['POST'])
def set_acl_call(instance_id):
    return jsonify(id='412459873247234',
                   ip_address='192.168.1.2')
