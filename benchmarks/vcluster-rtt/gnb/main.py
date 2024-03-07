import requests
import datetime

# The URL you are sending the POST request to
url = "http://amf-service.default.svc.cluster.local"

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
