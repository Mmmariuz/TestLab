from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/fact", methods=["GET"])
def give_fact():
    return jsonify({"fact": "Flamingoer kan bare spise med hodet opp-ned!"})

if __name__ == "__main__":
    app.run()
    
import os

port = int(os.environ.get("PORT", 5000))

app.run(host="0.0.0.0", port=port)

