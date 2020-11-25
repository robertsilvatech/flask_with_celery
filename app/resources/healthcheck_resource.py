from flask_restful import Resource

class HealthcheckResource(Resource):
    def get(self):
        return {"message": "API is alive"}