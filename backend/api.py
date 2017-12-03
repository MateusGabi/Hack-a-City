from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import nltk
from flask_cors import CORS
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': '172.50.5.140', 'port': 9200}])

app = Flask(__name__)
api = Api(app)
CORS(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

IncidentesDados = {
    '1' : {
            'x': '10000.0',
            'y': '2000.0',
            'incidente': 'roubo',

        },
    '2' : {
            'x': '40000.0',
            'y': '7000.0',
            'incidente': 'briga de rua',

        }
}

IncidentesOcorridos = { 
    'ocorrencias' : [
        {
            'bairro': 'vila coophamorena',
            'ano': 2011, 
            'latitude': -20.4665648,
            'dia': '15',
            'tipo': 'trafico de drogas', 
            'longitude': -54.6031665,
            'objeto': 'celular',
            'hora': 17,
            'diaDaSemana': 'sexta-feira',
            'mes': 7
        }, 
        {
            'bairro': 'vila olga',
            'ano': 2011,
            'latitude': -20.4650274,
            'dia': '15',
            'tipo': 'furto', 
            'longitude': -54.6262041,
            'objeto': 'produtos',
            'hora': 6, 
            'diaDaSemana': 'quarta-feira', 
            'mes': 6
        }
        ] 
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

class InfoTotal(Resource):
    def get(self):
        dado = {}
        dado['total'] = es.search(index='bos', body={
				        'size' : 0,
				        'query': {
				            'match_all' : {}
				       }
				   }
				)['hits']['total']

        dado['incidentes'] = []

        dado['incidentes'].append({'roubo':  es.search(index='bos', body={"filter": 
                {"match": 
                    {"fact": "roubo"}
                }
            }, size=0
        )['hits']['total']})

        dado['incidentes'].append({'furto': es.search(index='bos', body={"filter": 
                {"match": 
                    {"fact": "furto"}
                }
            }, size=0
        )['hits']['total']})

        dado['incidentes'].append({'homicidio': es.search(index='bos', body={"filter": 
                {"match": 
                    {"fact": "homicidio"}
                }
            }, size=0
        )['hits']['total']})

        dado['incidentes'].append({'tentativa de homicidio': es.search(index='bos', body={"filter": 
                {"match": 
                    {"fact":{

                        "query":"tentativa de homicidio",
                    "operator" : "and"	
                    }
                    }
                    
                }
            }, size=0
        )['hits']['total']})

        dado['incidentes'].append({"trafico de drogas": es.search(index='bos', body={"filter": 
                {"match": 
                    {"fact":{

                        "query":"trafico de drogas",
                    "operator" : "and"	
                    }
                    }
                    
                }
            }, size=0
        )['hits']['total']})

        return dado

class Incidentes(Resource):
    def get(self):
        return IncidentesOcorridos

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Incidentes, '/incidentes')
api.add_resource(InfoTotal, '/info/total')


if __name__ == '__main__':
    app.run(debug=True)