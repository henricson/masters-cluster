import requests
import time
import threading
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor

urls = ["http://nrf.svc.cluster.default/discover/ausf",
        "http://ausf.svc.cluster.default/ue-authentication-info",
        "http://ausf.svc.cluster.default/ue-aka-confirmation",
        "http://nrf.svc.cluster.default/discover/udm",
        "http://udm.svc.cluster.default/slice-selection",
        "http://udm.svc.cluster.default/am-subscription",
        "http://udm.svc.cluster.default/sm-subscription",
        "http://udm.svc.cluster.default/sdm-subscription",
        "http://nrf.svc.cluster.default/discover/pcf",
        "http://pcf.svc.cluster.default/am-policy-control",
        "http://smf.svc.cluster.default/create-sm-context",
        "http://smf.svc.cluster.default/update-sm-context",
        ]  # Sequencially call these

requests_per_minute = 120
total_requests = 120
output_file = "response_times.txt"

# Queue for storing URLs to be requested
request_queue = Queue()
# Queue for storing response times
response_times_queue = Queue()

def make_request(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Requested {url}, Status Code: {response.status_code}, Time Taken: {time_taken}")
    response_times_queue.put(time_taken)

def worker():
    while True:
        try:
            url = request_queue.get_nowait()
            make_request(url)
            request_queue.task_done()
        except Empty:
            break

def write_to_file(output_file):
    with open(output_file, "a") as file:
        while True:
            time_taken = response_times_queue.get()
            if time_taken is None:  # None is our signal to stop the thread
                break
            file.write(f"{time_taken}\n")
            response_times_queue.task_done()

# Load the request queue
for _ in range(total_requests):
    for url in urls:
        request_queue.put(url)

# Number of threads in the pool depends on your machine and network capabilities
num_threads = 10  # Adjust based on your requirements and capabilities

# Start the file writing thread
file_writer_thread = threading.Thread(target=write_to_file, args=(output_file,), daemon=True)
file_writer_thread.start()

# Start worker threads
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    for _ in range(num_threads):
        executor.submit(worker)

# Wait for all items in the request queue to be processed
request_queue.join()

# Signal the file writer thread to stop
response_times_queue.put(None)
file_writer_thread.join()  # Wait for the file writer thread to finish

print("All requests made and response times stored.")