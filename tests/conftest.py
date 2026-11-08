import os

import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def timeout():
    return float(os.getenv("TIMEOUT_SECONDS", "10"))


@pytest.fixture(scope="session")
def max_response_seconds():
    return float(os.getenv("MAX_RESPONSE_SECONDS", "2.0"))


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Accept": "application/json"})
    yield s
    s.close()
