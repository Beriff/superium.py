import ast
import requests

class api:
    def assetSearch(type_=False, page=False, query=False, limit=False):
        url = "https://api.superium.net/asset/catalog?"
        
        if type_:
            url = url + f"type={type_}&"

        if page:
            url = url + f"page={page}&"

        if query:
            query = query.replace(" ", "%20")
            url = url + f"q={query}&"

        if limit:
            url = url + f"limit={limit}"

        toDict = requests.get(url).text
        return ast.literal_eval(toDict)


    def assetInfo(id_):
        id_ = str(id_)
        url = "https://api.superium.net/asset/info?id=" + id_
        toDict = requests.get(url).text
        return ast.literal_eval(toDict)

    def assetOwners(id_, limit=False, page=False):
        id_ = str(id_)
        url = "https://api.superium.net/asset/owners?id=" + id_ + "&"

        if limit:
            url = url + f"limit={limit}&"
        
        if page:
            url = url + f"page={page}"

        toDict = requests.get(url).text
        return ast.literal_eval(toDict)

    def assetSale(id_):
        id_ = str(id_)
        url = "https://api.superium.net/asset/sales?id=" + id_

        toDict = requests.get(url).text
        return ast.literal_eval(toDict)

    def getAppearance(id_):
        id_ = str(id_)
        url = "https://api.superium.net/users/getappearance?id=" + id_

        toDict = requests.get(url).text
        return ast.literal_eval(toDict)

    def getByUsername(name):
        url = f"https://api.superium.net/users/getbyusername?username={name}"

        toDict = requests.get(url).text
        return ast.literal_eval(toDict)

    def getUser(id_):
        url = f"https://api.superium.net/users/user?id={id_}"

        toDict = requests.get(url).text
        return ast.literal_eval(toDict)
