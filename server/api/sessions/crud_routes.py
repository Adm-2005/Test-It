# external imports
import pytz
import datetime as dt
from typing import Dict, Tuple, Any
from flask_jwt_extended import jwt_required
from pymongo import ReturnDocument, DESCENDING
from flask import request, current_app, jsonify, abort

# internal imports
from api import mongo
from api.sessions import sess_bp
from api.db.session_models import Session
from api.utils.pagination import pagination_links
from api.utils.validators import objectid_validator
from api.db.pydantic_objectid import PydanticObjectId
from api.sessions.response_services import handle_code_input, handle_image_input

@sess_bp.route('/create/<string:proj_id>', methods=['POST'])
@jwt_required()
def create_session(proj_id: str) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint to create a session inside a project.

    Args:
        proj_id: id of the project that will contain the session.
    
    Returns:
        Tuple[Dict[str, Any], int]: response, status code.
    """
    sessions = mongo.db.sessions

    try:
        _ = objectid_validator(proj_id)

        data = request.get_json()
        name = data.get('name', '').strip()
        scope = data.get('scope', '').strip()

        if not data or not name or not scope:
            abort(400, 'Missing required fields.')

        generated_response = None

        images = request.files.get('input_images')
        code = data.get('input_code')

        if images:
            generated_response = handle_image_input(images, name, scope)

        if code:
            generated_response = handle_code_input(code, name, scope)

        if not images and not code:
            abort(400, 'No input to generate test cases.')

        data['generated_response'] = generated_response

        session = Session(**data)
        session.proj_id = PydanticObjectId(proj_id)
        session.set_updated_at()

        sess_id = str(sessions.insert_one(session.to_bson()).inserted_id)
        session.id = PydanticObjectId(sess_id)

        return jsonify({
            'message': 'Session created successfully.',
            'data': {
                'session': session.to_json()
            }
        }), 201

    except Exception as e:
        current_app.logger.error('Error while creating session: %s', e)
        raise e

@sess_bp.route('/<string:id>', methods=['GET'])
@jwt_required()
def get_session(id: str) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint to fetch a session.

    Args:
        id: id of the session to be fetched.

    Returns:
        Tuple[Dict[str, Any], int]: response, status code.
    """
    sessions = mongo.db.sessions

    try:
        id_obj = objectid_validator(id)

        res = sessions.find_one({'_id': id_obj})
        if not res:
            abort(404, 'Session not found.')

        session = Session(**res)

        return jsonify({
            'message': 'Session fetched successfully.',
            'data': {
                'session': session.to_json()
            }
        }), 200
    
    except Exception as e:
        current_app.logger.error('Error while fetching session %s: %s', id, e)
        raise e

@sess_bp.route('/<string:proj_id>', methods=['GET'])
@jwt_required()
def get_all_sessions(proj_id: str) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint to fetch all sessions in a project.

    Args:
        proj_id: id of the project.

    Returns:
        Tuple[Dict[str, Any], int]: response, status code.
    """
    sessions = mongo.db.sessions
    projects = mongo.db.projects

    try:
        proj_id_obj = objectid_validator(proj_id)

        project = projects.find_one({'_id': proj_id_obj})
        if not project:
            abort(404, 'Project not found.')

        page = max(int(request.args.get('page', 1)), 1)
        per_page = max(min(int(request.args.get('per_page', 10)), 100), 1)

        query = {'proj_id': proj_id_obj}
        cursor = sessions.find(query).sort('updated_at', DESCENDING)\
        .skip(per_page * (page - 1)).limit(per_page)
        session_count = sessions.count_documents(query)

        links = pagination_links('.get_all_sessions', session_count, page, per_page)

        return jsonify({
            'message': 'Sessions fetched successfully.',
            'data': {
                'sessions': [Session(**doc).to_json() for doc in cursor],
                'links': links
            }
        }), 200

    except Exception as e:
        current_app.logger.error('Error while fetching all sessions for user %s: %s', proj_id, e)
        raise e

@sess_bp.route('/<string:id>', methods=['PUT'])
@jwt_required()
def update_session(id: str) -> Tuple[Dict[str, Any]]:
    """
    Endpoint to update a session.

    Args:
        id: id of the session to be updated.

    Returns:
        Tuple[Dict[str, Any], int]: response, status code.
    """
    sessions = mongo.db.sessions

    try:
        id_obj = objectid_validator(id)

        data = request.get_json()
        if not data:
            abort(400, 'No fields to update.')

        data['updated_at'] = dt.datetime.now(tz=pytz.timezone('Asia/Kolkata'))

        # first update to update existing name, scope and context
        # if they are provided, even if they are not provided
        # using the returned document from update to use existing values in the db
        res = sessions.find_one_and_update(
            {'_id': id_obj},
            {'$set': data},
            return_document=ReturnDocument.AFTER
        )
        if not res:
            abort(404, 'Session not found.')

        images = request.files.get('input_images', res['input_image'])
        if images:
            res['generated_response'] = handle_image_input(images, res['name'], res['scope'])

        code = data.get('code', None)
        if code: 
            res['generated_response'] = handle_code_input(code, res['name'], res['scope'])

        # final update to 
        sessions.find_one_and_update(
            {'_id': id_obj},
            {'$set': res},
            return_document=ReturnDocument.AFTER
        )

        session = Session(**res)

        return jsonify({
            'message': 'Session updated successfully.',
            'data': {
                'session': session.to_json()
            }
        }), 200

    except Exception as e:
        current_app.logger.error('Error while updating session %s: %s', id, e)
        raise e

@sess_bp.route('/<string:id>', methods=['DELETE']) 
@jwt_required()
def delete_session(id: str) -> Tuple[Dict[str, Any]]:
    """
    Endpoint to delete a session.

    Args:
        id: id of the session to be deleted.

    Returns: 
        Tuple[Dict[str, Any], int]: response, status code.
    """
    sessions = mongo.db.sessions

    try:
        id_obj = objectid_validator(id)

        res = sessions.find_one_and_delete({'_id': id_obj})
        if not res:
            abort(404, 'Session not found.')
        
        return jsonify({
            'message': 'Session deleted successfully.',
            'data': None
        }), 200

    except Exception as e:
        current_app.logger.error('Error while deleting session %s: %s', id, e)
        raise e