import requests

def getProgramsBySeriesCode(base_url,code,spcode,**kwargs):
    url = base_url + "/content/getProgramsBySeriesCode"
    body ={
        "spCode": spcode,
        "code": code
    }
    body.update(kwargs)
    r = requests.post(url, json=body)
    return r

if __name__ == "__main__":
    base_url = "http://10.0.2.102:9998/vas-rest"
    r = getProgramsBySeriesCode(base_url, code="MGTV985f0f4543c6a86082a2810dd4f0", spcode="71e1545719c54c468b7ee6033121f551",orderByField="sequence")
    print(r.text)
    count = r.json()["data"]["totalCount"]
    print(count)