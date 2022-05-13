from api.showCatalogAll import showCatalogAll
import pytest

@pytest.mark.smoke
def test_showCatalogAll_success(base_url):
    r = showCatalogAll(base_url, "f5fecedac6e0469d98f475c60084c0d1","86cd9e3e0fa440b9866d7b89021b8c59")
    print(r.text)
    assert len(r.json()["data"]) == 5

@pytest.mark.parametrize("test_input,expected",[
    ["", {"code": 8003, "message":"专区code为空"}],
    ["86cd9e3e0fa440b9866d7b89021b8c51", {"code": 0, "message": "操作成功"}]
])
def test_showCatalogAll_fail(base_url, test_input, expected):
    r = showCatalogAll(base_url, "f5fecedac6e0469d98f475c60084c0d1", test_input)
    print(r.text)
    assert r.json()["code"] == expected["code"]
    assert r.json()["message"] == expected["message"]