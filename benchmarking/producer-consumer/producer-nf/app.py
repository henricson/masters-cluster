from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/produce', methods=['GET'])
def produce_data():
    data = "Hello from Producer NF"
    # Replace this URL with the actual service address of the Consumer NF in your cluster
    consumer_url = "http://consumer-nf-service:80/consume"
    response = requests.post(consumer_url, json={'data': data})
    return f"Data sent to Consumer NF: {response.text}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
