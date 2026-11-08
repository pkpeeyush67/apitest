import pytest
from jsonschema import validate

POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}


@pytest.mark.schema
def test_post_matches_schema(session, base_url, timeout):
    r = session.get(f"{base_url}/posts/1", timeout=timeout)
    validate(instance=r.json(), schema=POST_SCHEMA)


def test_content_type_is_json(session, base_url, timeout):
    r = session.get(f"{base_url}/posts/1", timeout=timeout)
    assert "application/json" in r.headers.get("Content-Type", "")


def test_response_time_within_limit(session, base_url, timeout, max_response_seconds):
    r = session.get(f"{base_url}/posts/1", timeout=timeout)
    assert r.elapsed.total_seconds() < max_response_seconds
