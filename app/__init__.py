import os
from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse
from app.resources.healthcheck_resource import HealthcheckResource
from app.resources.hello_resource import HelloResource
from app.resources.hostname_resource import HostnameResource


def create_app():
    app = Flask(__name__)
    api = Api(app)

    #app.config['ENV'] = 'devolopment'
    #app.config['DEBUG'] = True

    if 'FLASK_CONFIG' in os.environ.keys():
        app.config.from_object('app.settings.' + os.environ['FLASK_CONFIG'])
    else:
        app.config.from_object('app.settings.Development')

    api.add_resource(HealthcheckResource, '/healthcheck')
    api.add_resource(HelloResource, '/nome/<string:nome>')
    api.add_resource(HostnameResource, '/hostname')

    return app