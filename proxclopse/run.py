from flask import Flask
from proxclopse.routes.create import create_route
from proxclopse.routes.delete import delete_route
from proxclopse.routes.get import get_route
from proxclopse.routes.list import list_route
from proxclopse.routes.failover import failover_route
from proxclopse.routes.modify import modify_route
from proxclopse.routes.set_acl import set_acl_route
app = Flask(__name__)
app.register_blueprint(create_route)
app.register_blueprint(delete_route)
app.register_blueprint(get_route)
app.register_blueprint(list_route)
app.register_blueprint(failover_route)
app.register_blueprint(modify_route)
app.register_blueprint(set_acl_route)
app.debug = True


def run():
    app.run(host='0.0.0.0')
