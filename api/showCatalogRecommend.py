import requests

def showCatalogRecommend(base_url, parentCode, spcode,**kwargs):
    url = base_url + "/catalog/showCatalogRecommend"
    body ={
        "spCode": spcode,
        "parentCode": parentCode
    }
    body.update(kwargs)
    r = requests.post(url, json=body)
    return r

if __name__ == "__main__":
    base_url = "http://10.0.1.156:8183/vas-rest"
    r = showCatalogRecommend(base_url, parentCode="f5fecedac6e0469d98f475c60084c0d1",spcode="86cd9e3e0fa440b9866d7b89021b8c59",orderByField="sequence")
    data_len = len(r.json()["data"])
    print(data_len)