from flask import Blueprint, request, jsonify
from Components.agent import handle_query

api = Blueprint('api', __name__)

@api.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        answer, status_code = handle_query(query)
        return jsonify(answer), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

