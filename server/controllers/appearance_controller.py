from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.app import db
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from sqlalchemy.exc import SQLAlchemyError

appearance_bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@appearance_bp.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()

    
    required_fields = ['guest_id', 'episode_id', 'rating']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields: guest_id, episode_id, rating'}), 400

    if not isinstance(data['rating'], int):
        return jsonify({'error': 'Rating must be an integer'}), 400

    
    if not Guest.query.get(data['guest_id']) or not Episode.query.get(data['episode_id']):
        return jsonify({'error': 'Invalid guest or episode ID'}), 404

    try:
        appearance = Appearance(**data)
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except ValueError as e:
       
        return jsonify({'error': str(e)}), 400
    except SQLAlchemyError as e:
        
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}), 500