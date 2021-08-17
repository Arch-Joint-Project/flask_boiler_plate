import json
import dataclasses
from flask import request, Blueprint, Response
from app.models import User
from app import db
from app.repositories import UserRepository
from app.controllers import UserController
import pinject

user = Blueprint("user", __name__)

obj_graph = pinject.new_object_graph(modules=None, classes=[
    UserController, UserRepository
])

user_controller = obj_graph.provide(UserController)


@user.route("/", methods=["POST"])
def create():
    data = request.json
    user = user_controller.create(data)
    response = json.dumps(dataclasses.asdict(user))
    return Response(response, mimetype="application/json", status=201)
