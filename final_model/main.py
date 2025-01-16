from flask import Flask, request, jsonify
from model import get_best_places

app = Flask(__name__)


@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    try:
        request_data = request.json
        if not request_data:
            return jsonify({"error": "Invalid or missing JSON"}), 400

        bucket_list = request_data.get('bucket_list', [])
        preferred_activities = request_data.get('preferred_activities', [])

        # Replace this with actual logic
        return jsonify(get_best_places(activities=preferred_activities, destinations=bucket_list))
    except Exception as e:
        return jsonify({"error": str(e)}), 400



if __name__ == "__main__":
    app.run(debug=True)