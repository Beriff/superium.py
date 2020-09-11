# Superium.py
superium.py is a python representation of web api for superium.net. It will be updated as the api itself is updated.

# functions
All functions are placed inside an api class.

## assetSearch(type_, page, query, limit)
returns a list of dictionaries which include asset info.

## assetInfo(id_)
returns a dictionary which includes asset info

## assetOwners(id_, limit, page)

returns a dictionary with owners of specified asset

## assetSale(id_)
returns a dictionary which includes a user and buying timestamp of specified asset

## getAppearance(id_)
returns an advanced user information, such as it's hash or rank.

## getByUsername(name)
returns a page-visible information about user

## getUser(id_)
same as getByUsername but accepts id instead of name

Learn more about web api itself at https://api.superium.net/docs