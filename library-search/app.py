import os
import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

CALIL_API_KEY = os.environ.get("CALIL_API_KEY", "727b9ece079b2548b4734a69506e195f")
CALIL_LIBRARY_URL = "https://api.calil.jp/library"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/libraries")
def get_libraries():
    lat = request.args.get("lat")
    lng = request.args.get("lng")
    pref = request.args.get("pref", "")
    city = request.args.get("city", "")
    limit = request.args.get("limit", "10")

    params = {
        "appkey": CALIL_API_KEY,
        "format": "json",
        "limit": limit,
    }

    if lat and lng:
        params["geocode"] = f"{lng},{lat}"
    if pref:
        params["pref"] = pref
    if city:
        params["city"] = city

    try:
        response = requests.get(CALIL_LIBRARY_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return jsonify({"libraries": data, "count": len(data)})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
