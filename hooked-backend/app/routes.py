from flask import Blueprint, request, jsonify
from app.services import get_recommendations

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/recommend', methods=['GET'])
def recommend():
    track_id = request.args.get('track_id')
    if not track_id:
        return jsonify({"error": "Missing track_id"}), 400
    
    recommendations = get_recommendations(track_id)
    return jsonify(recommendations)
