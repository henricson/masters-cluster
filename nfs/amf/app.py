import requests
import time
import numpy as np
from scipy.stats import t
import os

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
    std_dev_time = np.std(all_times, ddof=1)  # Use Bessel's correction
    print(f"\nMean total time: {mean_time:.2f} ms")
    print(f"Standard deviation of total time: {std_dev_time:.2f} ms")

    # Calculate the 95% confidence interval for the mean total time
    confidence_level = 0.95
    degrees_freedom = repetitions - 1
    alpha = 1 - confidence_level
    t_critical = t.ppf(1 - alpha/2, degrees_freedom)
    margin_error = t_critical * (std_dev_time / np.sqrt(repetitions))
    confidence_interval = (mean_time - margin_error, mean_time + margin_error)

    print(f"95% Confidence Interval for the mean: ({confidence_interval[0]:.2f} ms, {confidence_interval[1]:.2f} ms)")

def main():
    urls = [
        f"http://{os.environ.get('NRF_HOST', 'nrf.default.svc.cluster.local')}:80/discover-ausf",
        f"http://{os.environ.get('AUSF_HOST', 'ausf.default.svc.cluster.local')}:80/ue-authentication-info",
        f"http://{os.environ.get('AUSF_HOST', 'ausf.default.svc.cluster.local')}:80/5g-aka-confirmation",
        f"http://{os.environ.get('NRF_HOST', 'nrf.default.svc.cluster.local')}:80/discover-udm",
        f"http://{os.environ.get('UDM_HOST', 'udm.default.svc.cluster.local')}:80/slice-selection-get",
        f"http://{os.environ.get('UDM_HOST', 'udm.default.svc.cluster.local')}:80/am-subscription-get",
        f"http://{os.environ.get('UDM_HOST', 'udm.default.svc.cluster.local')}:80/sm-subscription-get",
        f"http://{os.environ.get('UDM_HOST', 'udm.default.svc.cluster.local')}:80/sdm-subscription",
        f"http://{os.environ.get('NRF_HOST', 'nrf.default.svc.cluster.local')}:80/discover-pcf",
        f"http://{os.environ.get('PCF_HOST', 'pcf.default.svc.cluster.local')}:80/am-policy-control",
        f"http://{os.environ.get('SMF_HOST', 'smf.default.svc.cluster.local')}:80/create-sm-context",
        f"http://{os.environ.get('SMF_HOST', 'smf.default.svc.cluster.local')}:80/update-sm-context",
    ]
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
