# app/views/user_views.py
from flask import Blueprint, jsonify, request
from ..controllers import user_controller

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = user_controller.get_all_users()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.json
    new_user = user_controller.create_user(data)
    return jsonify({'id': new_user.id, 'name': new_user.name, 'email': new_user.email}), 201
