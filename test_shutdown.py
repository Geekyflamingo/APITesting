from APITesting.src.utils import shutdown,get_hash_by_job, post_hash, successful_response
import pytest
import re

@pytest.mark.last
class TestShutdown(object):
    def test_shutdown_successfully(self):
        response, status = shutdown()
        assert successful_response(status) is True

# TODO: def test_remaining_password_hashing_allowed_to_complete_during_shutdown(self): and def test_new_requests_rejected_during_shutdown(self):
