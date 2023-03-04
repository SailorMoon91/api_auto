from api.showCatalogAll import showCatalogAll
import pytest

@pytest.mark.smoke
def test_showCatalogAll_success(base_url):
    r = showCatalogAll(base_url, "ecb319c70ba445d58ba4e128e041063a","71e1545719c54c468b7ee6033121f551")
    print(r.text)
    assert len(r.json()["data"]) == 11

@pytest.mark.parametrize("test_input,expected",[
    ["", {"code": 8003, "message":"专区code为空"}],
    ["71e1545719c54c468b7ee6033121f551", {"code": 0, "message": "操作成功"}]
])
def test_showCatalogAll_fail(base_url, test_input, expected):
    r = showCatalogAll(base_url, "ecb319c70ba445d58ba4e128e041063a", test_input)
    print(r.text)
    assert r.json()["code"] == expected["code"]
    assert r.json()["message"] == expected["message"]