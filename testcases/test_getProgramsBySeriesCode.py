from api.getProgramsBySeriesCode import getProgramsBySeriesCode
import pytest

@pytest.mark.smoke
def test_getProgramsBySeriesCode_success(base_url):
    r = getProgramsBySeriesCode(base_url, "MGTV985f0f4543c6a86082a2810dd4f0","71e1545719c54c468b7ee6033121f551")
    print(r.text)
    assert len(r.json()["data"]) == 11

@pytest.mark.parametrize("test_input,expected",[
    ["", {"code": 8003, "message":"专区code为空"}],
    ["71e1545719c54c468b7ee6033121f551", {"code": 1, "message": "操作成功"}]
])
def test_getProgramsBySeriesCode_fail(base_url, test_input, expected):
    r = getProgramsBySeriesCode(base_url, "ecb319c70ba445d58ba4e128e041063a", test_input)
    print(r.text)
    assert r.json()["code"] == expected["code"]
    assert r.json()["message"] == expected["message"]