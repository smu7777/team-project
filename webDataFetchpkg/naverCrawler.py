import requests

def searchNaverShop(query: str, clientId: str, clientSecret: str, display: int = 10):
    url = "https://openapi.naver.com/v1/search/shop.json"
    headers = {
        "X-Naver-Client-Id": clientId,
        "X-Naver-Client-Secret": clientSecret
    }
    params = {
        "query": query,
        "display": display
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    return []

def filterItemsByPriceLimit(items):
    prices = []
    for item in items:
        priceStr = item.get("lprice", "").strip()
        if priceStr.isdigit():
            prices.append(int(priceStr))

    if prices:
        avgPrice = sum(prices) / len(prices)
        limit = avgPrice / 3.0
    else:
        limit = 0

    filteredItems = []
    for item in items:
        priceStr = item.get("lprice", "").strip()
        if not priceStr.isdigit():
            continue
        price = int(priceStr)
        if price > limit:
            filteredItems.append({
                "source": "Naver",
                "title": item.get("title", "").replace("<b>", "").replace("</b>", ""),
                "price": price,
                "link": item.get("link", "")
            })

    return filteredItems

def naverItemResult(query, maxResults):
    clientId = "MzsKEpdM0C7Sd6pHEJaJ"
    clientSecret = "WdnkycaTdf"
    items = searchNaverShop(query, clientId, clientSecret, maxResults)
    filteredItems = filterItemsByPriceLimit(items)
    return filteredItems
