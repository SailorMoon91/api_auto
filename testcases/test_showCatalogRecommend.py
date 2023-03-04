from api.showCatalogRecommend import showCatalogRecommend
import pytest

@pytest.mark.smoke
def test_showCatalogRecommend_success(base_url):
    r = showCatalogRecommend(base_url, "1b9052ac24e54967ac4dc00cc1f398a2", "71e1545719c54c468b7ee6033121f551")
    print(r.text)
    assert len(r.json()["data"]) == 5

@pytest.mark.parametrize("test_input,expected",[
    ["", {"code": 8003, "message":"专区code为空"}],
    ["86cd9e3e0fa440b9866d7b89021b8c51", {"code": 0, "message": "操作成功"}]
])
def test_showCatalogRecommend_fail(base_url,test_input,expected):
    r = showCatalogRecommend(base_url, "1b9052ac24e54967ac4dc00cc1f398a2", test_input)
    print(r.text)
    assert r.json()["code"] == expected["code"]
    assert r.json()["message"] == expected["message"]