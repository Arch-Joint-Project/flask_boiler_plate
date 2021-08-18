import json
import dataclasses
from flask import request, Blueprint, Response
from app.models import User
from app import db
from app.repositories import UserRepository
from app.controllers import UserController
import pinject

#create a blueprint instance or object for modular assembling of user-related routes and views.
user = Blueprint("user", __name__)

# we use dependency injection for object creation of classes on the fly as to
# hard coding for every new instance.
obj_graph = pinject.new_object_graph(modules=None, classes=[
    UserController, UserRepository # list all the classes that have placed an order to create objects on the fly.
])

# alright, object factory creates a UserController object for this instance of user_view.py file.
user_controller = obj_graph.provide(UserController)


#C: Create Route for our user.
@user.route("/", methods=["POST"])
def create():
    data = request.json
    the_create_user = user_controller.create(data)
    response = json.dumps(dataclasses.asdict(the_create_user))
    return Response(response, mimetype="application/json", status=201)

#R: Read Route for our user.
@user.route('/read') # default read to Read all data from database.
@user.route('/read/<int:id>', methods=["GET"]) # primary key read by ID to Read all data from database.
def read(id):



    the_id =  id if (isinstance(id,int))  else "False"  # if the id is of type int, then we call read_by_id method.
    if(the_id):

        the_read_user = user_controller.read_by_id(the_id)
        response = json.dumps(dataclasses.asdict(the_read_user))
        return Response(response, mimetype="application/json",
                        status=200)  # set headers to return content-type as json, 200 when successful.

    else:
        the_read_user = user_controller.read_all(
            the_id)  # controller handlers read operation from database using ORM.
        response = json.dumps(dataclasses.asdict(
            the_read_user))  # convert the default read data type from ORM as a list to dictionary then jsonify for client response.
        return Response(response, mimetype="application/json",
                        status=200)  # set headers to return content-type as json, 200 when successful.





#U: Update Route for our user.
# Update by id
@user.route('/update')  # default update
@user.route('/update/<int:id>', methods=["PUT"]) # update of by id route
def update(id):
    data = request.json # accept json
    the_id =  id if (isinstance(id,int))  else "False"  # if the id is of type int, then we call update_by_id
    if(the_id):

        the_update_user = user_controller.update_by_id(the_id,json.load(data)) # pass update param as dictionary
        response = json.dumps(dataclasses.asdict(the_update_user))
        return Response(response, mimetype="application/json",
                        status=200)  # set headers to return content-type as json, 200 when successful.

    else: #update all then.
        the_update_user = user_controller.update_all(
            the_id,json.load(data))  # controller handlers read operation from database using ORM.
        response = json.dumps(dataclasses.asdict(
            the_update_user))  # convert the default read data type from ORM as a list to dictionary then jsonify for client response.
        return Response(response, mimetype="application/json",
                        status=200)  # set headers to return content-type as json, 200 when successful.


#delete route
@user.route('/delete', methods=["DELETE"])
def delete():
    get_id_param = request.args.get("id") # accept incoming query params ?id.
    the_delete_user = user_controller.delete(get_id_param)
    return Response("Deleted Successfully", mimetype="application/json",status=200)

