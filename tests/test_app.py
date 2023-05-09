import httpx


def test_add():
    assert (1 + 1) == 2


def test_get():
    resp = httpx.get("http://localhost:8000")
    assert resp.status_code == 200


def test_post():
    payload = '{"h1_color": "#ff0000"}'
    resp = httpx.post("http://localhost:8000", content=payload)
    assert resp.status_code == 200


def test_put():
    resp = httpx.put("http://localhost:8000/green")
    assert resp.status_code == 200


def test_delete():
    resp = httpx.delete("http://localhost:8000")
    assert resp.status_code == 200
