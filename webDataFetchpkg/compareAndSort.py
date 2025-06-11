from .ebayCrawler import ebayItemResult
from .gmarketCrawler import gmarketItemResult
from .naverCrawler import naverItemResult

def comparePrices(query):
    # 네이버
    naverItems = naverItemResult(query, 30)
    naverResults = []
    for item in naverItems:
        price = item.get("lprice", "")
        if price.isdigit():
            naverResults.append({
                "source": "Naver",
                "title": item.get("title", "").replace("<b>", "").replace("</b>", ""),
                "price": int(price),
                "link": item.get("link", "")
            })

    # 이베이
    ebayItems = ebayItemResult(query, 30)
    ebayResults = []
    for item in ebayItems:
        ebayResults.append({
            "source": "eBay",
            "title": item["상품명"],
            "price": item["가격"],
            "link": item["제품 링크"]
        })

    # 지마켓
    gmarketItems = gmarketItemResult(query, 30)
    gmarketResults = []
    for item in gmarketItems:
        gmarketResults.append({
            "source": "Gmarket",
            "title": item["상품명"],
            "price": item["가격"],
            "link": item["제품 링크"]
        })

    # 가격 정렬 후 최저가 순으로 20개만 리턴
    allResults = naverResults + ebayResults + gmarketResults
    sortedResults = sorted(allResults, key=lambda x: x["price"])
    return sortedResults[:20]
