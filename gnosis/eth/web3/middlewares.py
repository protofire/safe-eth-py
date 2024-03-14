import time
from threading import Lock

from web3 import Web3


class ThrottleMiddleware:
    def __init__(self, web3: Web3, requests_per_second):
        self.web3 = web3
        self.requests_per_second = requests_per_second - 1
        self.lock = Lock()
        self.last_request_time = 0
        self.min_time_between_requests = 1 / requests_per_second

    def middleware(self, method, params):
        with self.lock:
            current_time = time.time()
            time_since_last_request = current_time - self.last_request_time
            if time_since_last_request < self.min_time_between_requests:
                # Calculate the remaining time to sleep
                time_to_sleep = self.min_time_between_requests - time_since_last_request
                time.sleep(time_to_sleep)
            self.last_request_time = time.time()

        return self.web3.provider.make_request(method, params)