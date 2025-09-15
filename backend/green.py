from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/weather', methods=['GET'])
def get_weather():
    # Dummy data; in production, replace with real API fetch
    weather = {
        "current": {
            "temperature": "28°C",
            "condition": "Partly Cloudy",
            "location": "Pune, Maharashtra",
            "humidity": "65%",
            "wind": "12 km/h",
            "rain": "20%",
            "farming_status": "Good for farming"
        },
        "forecast": [
            {"day": "Tomorrow", "temp": "30°/22°"},
            {"day": "Day 3", "temp": "26°/20°"},
            {"day": "Day 4", "temp": "27°/21°"}
        ]
    }
    return jsonify(weather)

@app.route('/api/crop_status', methods=['GET'])
def get_crop_status():
    crop_status = {
        "crop": "धान (Rice)",
        "growth_stage": "Flowering",
        "days_to_harvest": 45,
        "expected_yield": "Good"
    }
    return jsonify(crop_status)

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    recs = [
        {
            "type": "Irrigation",
            "title": "💧 Irrigation Alert",
            "details": "Water your rice field today. Soil moisture is optimal.",
            "highlight_color": "blue"
        },
        {
            "type": "Fertilizer",
            "title": "🌱 Fertilizer Due",
            "details": "Apply nitrogen-based fertilizer within the next 2 days.",
            "highlight_color": "orange"
        }
    ]
    return jsonify(recs)

@app.route('/api/quick_actions', methods=['GET'])
def get_quick_actions():
    actions = [
        {"icon": "🌱", "label": "Crop Advice"},
        {"icon": "🧪", "label": "Soil Test"},
        {"icon": "💬", "label": "Ask Expert"},
        {"icon": "🔔", "label": "Alerts"}
    ]
    return jsonify(actions)

# Example endpoint for "Ask Expert"
@app.route('/api/ask_expert', methods=['POST'])
def ask_expert():
    user_question = request.json.get("question", "")
    # In production, integrate with expert system/chats
    answer = "Thank you for your question. Our agronomist will reply soon."
    return jsonify({"answer": answer})

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    alerts = [
        {"message": "Heavy rainfall expected later this week."},
        {"message": "Market price update: Rice is trending higher."}
    ]
    return jsonify(alerts)

# Run server
if __name__ == '__main__':
    app.run(debug=True)
