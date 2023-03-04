import requests

def showCatalogAll(base_url,parentCode, spcode,**kwargs):
    url = base_url + "/catalog/showCatalogAll"
    body = {
        "spCode": spcode,
        "parentCode": parentCode
    }
    body.update(kwargs)
    r = requests.post(url, json=body)
    return r

if __name__ == "__main__":
    base_url = "http://10.0.2.102:9998/vas-rest"
    r = showCatalogAll(base_url, parentCode="ecb319c70ba445d58ba4e128e041063a", spcode="71e1545719c54c468b7ee6033121f551",orderByField="sequence")
    print(r.text)
