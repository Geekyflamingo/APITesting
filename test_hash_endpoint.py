from APITesting.src.utils import get_hash_by_job, post_hash, successful_response, get_hash_invalid
import pytest
import re

class TestGetHash(object):

    def test_get_without_id(self):
        response, status = get_hash_invalid()
        assert successful_response(status) is False and response.text == "GET Not Supported\n"

    def test_get_hash_with_existing_id(self):
        """
        Running a post before this test to ensure there is at least 1 id for the sake of time.
        To do this correctly, before and after hooks would be used to spin up and take down endpoints
        as well as do an initial request to the post so there is at least one correct id.
        """
        post_hash("{\"password\":\"angerymonkey\"}")
        response, status = get_hash_by_job(1)
        reg = r'^(\w|=|/){64,128}$'
        assert successful_response(status) is True and re.match(reg,response.text)

    def test_get_hash_with_a_non_existent_id(self):
        non_existent_id = -1
        response, status = get_hash_by_job(non_existent_id)
        assert successful_response(status) is False and response.text == "Invalid Input\n"

class TestPostHash(object):

    def test_empty_payload(self):
        response, status = post_hash("")
        assert  successful_response(status) is False and response.text == "Malformed Input\n"

    def test_blank_password(self):
        response, status = post_hash("{\"password\":\"\"}")
        assert successful_response(status) is True and re.match('\d+',response.text)

    def test_malformed_key(self):
        response, status = post_hash("{\"invalid_key\":\"mutton\"}")
        assert successful_response(status) is False and re.match('\d+',response.text)

    def test_post_hash_payload_returns_immediately(self):
        response, status = post_hash("{\"password\":\"angerymonkey\"}")
        time = response.elapsed.total_seconds()
        assert time < 0.5
