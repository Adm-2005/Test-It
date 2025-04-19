# external imports
import pytz
import datetime as dt
from typing import Dict, Tuple, Any
from pymongo import ReturnDocument, DESCENDING
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)
from flask import request, current_app, abort, jsonify

# internal imports
from api import mongo
from api.projects import proj_bp
from api.db.project_models import Project
from api.utils.pagination import pagination_links
from api.utils.validators import objectid_validator
from api.db.pydantic_objectid import PydanticObjectId

@proj_bp.route('/create', methods=['POST'])
@jwt_required()
def create_project() -> Tuple[Dict[str, Any], int]:
    """
    Endpoint to create projects.

    Returns:
        Tuple[Dict[str, Any], int]: response, status code.
    """    
    projects = mongo.db.projects

    try:
        user_id = get_jwt_identity()

        data = request.get_json()
        
        if not data or not data.get('name'):
            abort(400, 'Missing required fields.')

        project = Project(**data)
        project.user_id = PydanticObjectId(user_id)
        project.set_updated_at()

        proj_id = str(projects.insert_one(project.to_bson()).inserted_id)
        project.id = proj_id
        project.user_id = str(project.user_id) # converting back to string to allow json serialization

        return jsonify({
            'message': 'Project created successfully.',
            'data': {
                'project': project.to_json()
            }
        }), 201
        
    except Exception as e:
        current_app.logger.error('Error while creating project: %s', e)
        raise e

@proj_bp.route('/<string:id>', methods=['GET'])
@jwt_required()
def get_project(id: str) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint to fetch a project.

    Args:
        id: id of the project to be fetched.

    Returns:
        Tuple[Dict[str, Any], int]: response, status code.
    """    
    projects = mongo.db.projects

    try:
        id_obj = objectid_validator(id)

        res = projects.find_one({'_id': id_obj})
        if not res:
            abort(404, 'Project not found.')

        project = Project(**res)

        return jsonify({
            'message': 'Project fetched successfully.',
            'data': {
                'project': project.to_json()
            }
        }), 200

    except Exception as e:
        current_app.logger.error('Error while fetching project %s: %s', id, e)
        raise e

@proj_bp.route('/<string:user_id>', methods=['GET'])
@jwt_required()
def get_all_projects(user_id: str) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint to fetch all projects of an user.

    Args:
        user_id: id of the user.

    Returns:
        Tuple[Dict[str, Any], int]: response, status code.
    """    
    users = mongo.db.users
    projects = mongo.db.projects

    try:
        user_id_obj = objectid_validator(user_id)

        current_user_id = get_jwt_identity()

        user = users.find_one({'_id': user_id_obj})
        if not user:
            abort(404, 'User not found.')

        if str(user['_id']) != current_user_id:
            abort(403, 'User ID mismatch.')

        page = max(int(request.args.get('page')), 1)
        per_page = max(min(int(request.args.get('per_page')), 100), 1)

        query = {'user_id': user_id_obj}
        cursor = projects.find(query)\
            .sort('created_at', DESCENDING).skip(per_page * (page - 1)).limit(per_page)
        project_count = projects.count_documents(query)

        links = pagination_links('.get_all_projects', project_count, page, per_page)

        return jsonify({
            'message': 'Projects fetched successfully.',
            'data': {
                'projects': [Project(**doc).to_json() for doc in cursor],
                'links': links
            }
        }), 200

    except Exception as e:
        current_app.logger.error('Error while fetching all projects for user %s: %s', user_id, e)
        raise e

@proj_bp.route('/<string:id>', methods=['PUT'])
@jwt_required()
def update_project(id: str) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint to update projects.

    Args:
        id: id of the project to be updated.

    Returns:
        Tuple[Dict[str, Any], int]: response, status code.
    """    
    projects = mongo.db.projects

    try:
        id_obj = objectid_validator(id)

        data = request.get_json()

        if not data:
            abort(400, 'No fields to update.')
        data['updated_at'] = dt.datetime.now(tz=pytz.timezone('Asia/Kolkata'))

        res = projects.find_one_and_update(
            {'_id': id_obj}, 
            {'$set': data}, 
            return_document=ReturnDocument.AFTER
        )

        if not res:
            abort(404, 'Project not found.')

        project = Project(**res)

        return jsonify({
            'message': 'Project updated successfully.',
            'data': {
                'project': project.to_json()
            } 
        }), 200
    
    except Exception as e:
        current_app.logger.error('Error while updating project %s: %s', id, e)
        raise e

@proj_bp.route('/<string:id>', methods=['DELETE'])
@jwt_required()
def delete_project(id: str) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint to delete projects.

    Args:
        id: id of the project to be deleted.

    Returns:
        Tuple[Dict[str, Any], int]: response, status code.
    """    
    projects = mongo.db.projects

    try:
        id_obj = objectid_validator(id)

        proj = projects.find_one_and_delete({'_id': id_obj})
        if not proj:
            abort(404, 'Project not found.')

        return jsonify({
            'message': 'Project deleted successfully.',
            'data': None
        }), 200

    except Exception as e:
        current_app.logger.error('Error while deleting project: %s', e)
        raise e