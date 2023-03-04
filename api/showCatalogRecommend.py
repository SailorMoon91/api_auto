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
    base_url = "http://10.0.2.102:9998/vas-rest"
    r = showCatalogRecommend(base_url, parentCode="1b9052ac24e54967ac4dc00cc1f398a2",spcode="71e1545719c54c468b7ee6033121f551",orderByField="sequence")
    data_len = len(r.json()["data"])
    print(data_len)