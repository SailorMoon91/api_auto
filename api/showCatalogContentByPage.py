import requests

def showCatalogContentByPage(base_url,code, spcode, **kwargs):
    url = base_url + "/catalog/showCatalogContentByPage"
    body ={
        "spCode": spcode,
        "code": code
    }
    body.update(kwargs)
    r = requests.post(url, json=body)
    return r

if __name__ == "__main__":
    base_url = "http://10.0.2.102:9998/vas-rest"
    r = showCatalogContentByPage(base_url, code="9b52def1a44143faaa84bd3ce3c8a00c",spcode="71e1545719c54c468b7ee6033121f551",orderByField="sequence")
    print(r.text)
    count=r.json()["data"]["totalCount"]
    print(count)