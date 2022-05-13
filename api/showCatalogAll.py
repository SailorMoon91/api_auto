import requests

def showCatalogAll(base_url,parentCode, spcode,**kwargs):
    url = base_url + "/catalog/showCatalogAll"
    body ={
        "spCode": spcode,
        "parentCode": parentCode
    }
    body.update(kwargs)
    r = requests.post(url, json=body)
    return r

if __name__ == "__main__":
    base_url = "http://10.0.1.156:8183/vas-rest"
    r = showCatalogAll(base_url, parentCode="f5fecedac6e0469d98f475c60084c0d1",spcode="86cd9e3e0fa440b9866d7b89021b8c51",orderByField="sequence")
    print(r.text)
