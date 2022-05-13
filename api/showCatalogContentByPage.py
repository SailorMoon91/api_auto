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
    base_url = "http://10.0.1.156:8183/vas-rest"
    r = showCatalogContentByPage(base_url, code="f613c694c70d4a7bb534ea3bf5300a0a",spcode="86cd9e3e0fa440b9866d7b89021b8c59",orderByField="sequence")
    print(r.text)