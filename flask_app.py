# 3rd-party
from flask import Flask
from flask_cors import CORS

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask_restplus import Api, Resource, reqparse

# Flask App 생성
app = Flask('app name')
app.config['DEBUG'] = True
app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

# CORS 설정
CORS(app)

# Flask-rest Api 생성
api = Api(app, version='1.0', title='app 제목', description='app 설명')

model = lambda x: x[::-1]  # 모델 초기화

args_parser = reqparse.RequestParser()
args_parser.add_argument('query', location='form', type=str, default="", help='질의문. 한 문장으로 입력해주세요.')

@api.route('/forward')
@api.doc(parser=args_parser)
class ServeModel(Resource):
    def post(self):
        args = args_parser.parse_args()
        query = args['query']
        return model(query)

if __name__ == '__main__':
    app.run(port='41069', host='0.0.0.0')