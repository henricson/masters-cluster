from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/path', methods=['POST'])
def handle_post():
    # Get data sent with POST request
    data = request.json

    # Log the current time and the received data
    app.logger.info(f"Received at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    app.logger.info(f"Data received: {data}")

    # Respond with a JSON object
    response = {
        'message': 'POST request processed successfully!',
        'yourData': data
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, port=80)
