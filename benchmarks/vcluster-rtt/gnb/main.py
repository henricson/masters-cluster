import requests
import datetime
import time

while True:
    # The URL you are sending the POST request to
    url = "http://amf-service.default.svc.cluster.local:5000/path"

    # The data you want to send in the POST request
    data = {
        "key": "value"
    }

    # Record the start time and date
    start_time = datetime.datetime.now()

    print(f"Request started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Send the POST request
    response = requests.post(url, data=data)

    # Calculate the response time
    end_time = datetime.datetime.now()
    response_time = end_time - start_time

    # Print the response time and the response status code
    print(f"Response received in: {response_time.total_seconds()} seconds")
    print(f"Response status code: {response.status_code}")

    # Wait for 10 seconds before sending the next request
    time.sleep(10)
