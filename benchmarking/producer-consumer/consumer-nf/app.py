from flask import Flask, request

app = Flask(__name__)

@app.route('/consume', methods=['POST'])
def consume_data():
    data = request.json['data']
    print(f"Received data: {data}")
    # Process data here
    return f"Data processed: {data}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

