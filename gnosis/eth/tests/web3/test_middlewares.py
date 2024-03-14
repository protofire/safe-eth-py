import time
import unittest
from unittest.mock import Mock

from gnosis.eth.web3 import ThrottleMiddleware


class TestThrottleMiddleware(unittest.TestCase):
    def setUp(self):
        self.mock_web3 = Mock()
        self.mock_web3.provider.make_request = Mock(return_value='response')
        self.throttle_middleware = ThrottleMiddleware(
            self.mock_web3,
            requests_per_second=2  # Set requests per second to 2 for testing
        )

    def test_throttle_middleware(self):
        # Number of requests to send
        num_requests = 5

        # Simulate making multiple requests
        start_time = time.time()
        for _ in range(num_requests):
            self.throttle_middleware.middleware('method', ['params'])
        end_time = time.time()

        # Calculate the elapsed time
        elapsed_time = end_time - start_time

        # Calculate the average requests per second
        avg_requests_per_second = num_requests / elapsed_time

        # Verify that the average requests per second is less than 3
        self.assertLess(avg_requests_per_second, 3)

        # Check that make_request was called num_requests times
        self.assertEqual(self.mock_web3.provider.make_request.call_count, num_requests)
