import pytest


@pytest.mark.smoke
def test_list_posts_returns_200_and_list(session, base_url, timeout):
    r = session.get(f"{base_url}/posts", timeout=timeout)
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, list) and len(body) > 0


def test_get_single_post(session, base_url, timeout):
    r = session.get(f"{base_url}/posts/1", timeout=timeout)
    assert r.status_code == 200
    assert r.json()["id"] == 1


def test_get_missing_post_returns_404(session, base_url, timeout):
    r = session.get(f"{base_url}/posts/999999", timeout=timeout)
    assert r.status_code == 404


def test_create_post(session, base_url, timeout):
    payload = {"title": "hello", "body": "world", "userId": 1}
    r = session.post(f"{base_url}/posts", json=payload, timeout=timeout)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == "hello"
    assert "id" in body


def test_update_post(session, base_url, timeout):
    payload = {"id": 1, "title": "updated", "body": "text", "userId": 1}
    r = session.put(f"{base_url}/posts/1", json=payload, timeout=timeout)
    assert r.status_code == 200
    assert r.json()["title"] == "updated"


def test_delete_post(session, base_url, timeout):
    r = session.delete(f"{base_url}/posts/1", timeout=timeout)
    assert r.status_code == 200


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_filter_posts_by_user(session, base_url, timeout, user_id):
    r = session.get(f"{base_url}/posts", params={"userId": user_id}, timeout=timeout)
    assert r.status_code == 200
    assert all(p["userId"] == user_id for p in r.json())
