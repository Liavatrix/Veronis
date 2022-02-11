from dataclasses import dataclass
from datetime import datetime

from sanic import Sanic
from sanic.response import json
from sanic_jwt import Initialize, protected

from user import Authenticate
from jsonNormalizer import JsonNormalizer


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    return Authenticate.authenticate(username, password)


app = Sanic("VeronisExercise")
Initialize(app, authenticate=authenticate)


@app.route('/')
async def test(request):
    return json({'hello': 'world'})


@app.route('/normalize')
@protected()
async def protected_route(request):
    return json(JsonNormalizer.normalize(request.json))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8888)
