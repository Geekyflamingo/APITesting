from APITesting.src.utils import get_stats, is_json, successful_response, get_stats_data_passed, post_stats
import pytest
import re

class TestGetStats(object):
    def test_get_stats_response_successful(self):
        response, status = get_stats()
        assert successful_response(status) is True

    def test_get_stats_response_is_json(self):
        response, status = get_stats()
        assert is_json(response.text)

    def test_get_stats_AverageTime_in_milliseconds(self):
        response, status = get_stats()
        ttr = response.json()["AverageTime"]
        # By description should take ~5000 seconds to run
        assert ttr >= 5000 and ttr <= 6000

    def test_get_stats_TotalRequests_since_server_started(self):
        response, status = get_stats()
        tot_req = response.json()["TotalRequests"]
        # Depends on manual runs but minimum is 1-10 from this suite
        assert tot_req >= 1 # and tot_req <= 10

    def test_get_stats_with_data_unsuccessful(self):
        response, status = get_stats_data_passed()
        assert successful_response(status) is False

class TestPostStats(object):
    def test_post_stats_response_unsuccessful(self):
        response, status = post_stats()
        assert successful_response(status) is False
