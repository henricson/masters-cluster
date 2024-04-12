import requests
import time
import numpy as np

def measure_request_time(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        print(f"Requested {url}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")
    end_time = time.time()
    return (end_time - start_time) * 1000  # Return time in milliseconds

def measure_requests(urls, repetitions=5):
    all_times = []  # Store total times for each repetition

    for i in range(repetitions):
        print(f"\nIteration {i+1}/{repetitions}")
        iteration_times = []

        for url in urls:
            time_taken = measure_request_time(url)
            iteration_times.append(time_taken)
            print(f"Time taken: {time_taken:.2f} ms")

        total_time = sum(iteration_times)
        all_times.append(total_time)
        print(f"Total time for iteration {i+1}: {total_time:.2f} ms")

    # Calculate and print the mean and standard deviation of all total times
    mean_time = np.mean(all_times)
    std_dev_time = np.std(all_times)
    print(f"\nMean total time: {mean_time:.2f} ms")
    print(f"Standard deviation of total time: {std_dev_time:.2f} ms")

def main():
    urls = [
        "http://nrf.default.svc.cluster.local:80/discover-ausf",
        "http://ausf.default.svc.cluster.local:80/ue-authentication-info",
        "http://ausf.default.svc.cluster.local:80/5g-aka-confirmation",
        "http://nrf.default.svc.cluster.local:80/discover-udm",
        "http://udm.default.svc.cluster.local:80/slice-selection-get",
        "http://udm.default.svc.cluster.local:80/am-subscription-get",
        "http://udm.default.svc.cluster.local:80/sm-subscription-get",
        "http://udm.default.svc.cluster.local:80/sdm-subscription",
        "http://nrf.default.svc.cluster.local:80/discover-pcf",
        "http://pcf.default.svc.cluster.local:80/am-policy-control",
        "http://smf.default.svc.cluster.local:80/create-sm-context",
        "http://smf.default.svc.cluster.local:80/update-sm-context",
    ]  # Sequentially call these URLs

    while True:
        print("\nWelcome to the Interactive Request Timing CLI")
        print("1: Run measurements")
        print("2: Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            repetitions = input("Enter number of repetitions for the measurements: ")
            try:
                repetitions = int(repetitions)
                measure_requests(urls, repetitions)
            except ValueError:
                print("Invalid number of repetitions. Please enter a valid integer.")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please enter 1 or 2.")

if __name__ == '__main__':
    main()
