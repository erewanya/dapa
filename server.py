from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_KEYS = {
    "ytr1a": True,
    "XYZ789": True,
}

@app.route("/api/check_license")
def check_license():
    key = request.args.get("key")
    return jsonify({"valid": VALID_KEYS.get(key, False)})

if __name__ == "__main__":
    app.run()
