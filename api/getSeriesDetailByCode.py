import requests

def getSeriesDetailByCode(base_url, code, spcode,**kwargs):
    url = base_url + "/content/getSeriesDetailByCode"
    body ={
        "spCode": spcode,
        "code": code
    }
    body.update(kwargs)
    r = requests.post(url, json=body)
    return r

if __name__ == "__main__":
    base_url = "http://10.0.1.156:8183/vas-rest"
    r = getSeriesDetailByCode(base_url,code="60b1d5958b2d46e98e7706a2a5a2485f",spcode="86cd9e3e0fa440b9866d7b89021b8c59",orderByField="sequence")
    print(r.text)