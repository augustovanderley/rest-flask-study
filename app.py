from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec, Response
from pydantic import BaseModel

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Live de Python')
spec.register(server)

class Pessoa(BaseModel):
    id:int
    nome: str
    idade: int

@server.get('/pessoas')
@spec.validate(resp=Response(HTTP_200=Pessoa))
def pegar_pessoas():
    return "Programaticamente falando"

server.run()