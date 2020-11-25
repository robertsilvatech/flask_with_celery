from flask_restful import Resource
from flask_restful import reqparse
from app import celery_runner

class HelloResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('idade', type=str, required=True, help='This field is missing')

    def get(self, nome):
        message = f'Hello {nome}'
        task = celery_runner.hello.delay(message)
        return {"message": 'Aguarde o seu nome será escrito no arquivo file.txt'}

    def post(self, nome):
        data = Hello.parser.parse_args()
        idade = data['idade']
        return {"message": f'Ola o {nome} possui {idade} anos'}

