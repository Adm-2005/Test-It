# external imports
from flask import Flask, jsonify

def register_error_handlers(app: Flask) -> None:
    """
    Registers error handlers to the application instance.

    Args:
        app: flask application instance
 
    """
    # errors raised using abort(status_code, description)
    @app.errorhandler(400)
    def bad_request(error):
        response = {
            'status_code': 400,
            'message': 'Bad Request.',
            'error': str(error)
        }
        return jsonify(response), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        response = {
            'status_code': 401,
            'message': 'Unauthorized Request.',
            'error': str(error)
        }
        return jsonify(response), 401
    
    @app.errorhandler(402)
    def payment_required(error):
        response = {
            'status_code': 402,
            'message': 'Payment Required.',
            'error': str(error)
        }
        return jsonify(response), 402
    
    @app.errorhandler(403)
    def forbidden(error):
        response = {
            'status_code': 403,
            'message': 'Forbidden Request.',
            'error': str(error)
        }
        return jsonify(response), 403
    
    @app.errorhandler(404)
    def not_found(error):
        response = {
            'status_code': 404,
            'message': 'Resource Not Found.',
            'error': str(error)
        }
        return jsonify(response), 404
    
    # errors raised using raise(error)
    @app.errorhandler(Exception)
    def unknown_error(error):
        response = {
            'status_code': 500,
            'message': 'Internal Server Error.',
            'error': str(error)
        }
        return jsonify(response), 500