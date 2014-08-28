from flask import Blueprint, jsonify, request, abort
from proxclopse.common.constants import BASE_URI

"""
Create blueprint route.
"""
create_route = Blueprint('create', __name__)

"""
Create a proxclopse instance.
Example HTTP message:
PUT /v1/create HTTP/1.1
"""


@create_route.route(BASE_URI + 'create', methods=['POST'])
def create_call():
    return jsonify(id='412459873247234',
                   ip_address='192.168.1.2')
