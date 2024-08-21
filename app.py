from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all origins

@app.route('/order', methods=['GET'])
def create_order():
    order_id = request.args.get('orderId')
    
    return jsonify({'status': 'Order confirmed', 'order_id': order_id}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
