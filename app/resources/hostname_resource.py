from flask_restful import Resource
from app.models.hostname_model import get_hostname

class HostnameResource(Resource):
    def get(self):
        hostname = get_hostname()
        return {"message": f'The API is running in {hostname}'}