from flask import Flask, jsonify

app = Flask(__name__)

shipments = [
    {"id": 1, "origin": "Dar es Salaam", "destination": "Nairobi", "status": "In Transit"},
    {"id": 2, "origin": "New York", "destination": "London", "status": "Delayed"},
    {"id": 3, "origin": "Tokyo", "destination": "Sydney", "status": "Delivered"}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Amazon Unified Solver - Logistics Dashboard",
        "endpoints": {
            "/shipments": "List all shipments",
            "/shipment/<id>": "Get shipment details by ID"
        }
    })

@app.route('/shipments')
def list_shipments():
    return jsonify(shipments)

@app.route('/shipment/<int:id>')
def shipment_detail(id):
    shipment = next((s for s in shipments if s["id"] == id), None)
    if shipment:
        return jsonify(shipment)
    else:
        return jsonify({"error": "Shipment not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
