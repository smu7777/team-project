from .ebayCrawler import ebayItemResult
from .gmarketCrawler import gmarketItemResult
from .naverCrawler import naverItemResult

def comparePrices(query):
    # 네이버
    naverItems = naverItemResult(query, 30)
    naverResults = []
    for item in naverItems:
        price = item.get("가격", 0)
        if isinstance(price, int) and price > 0:
            naverResults.append({
                "source": "Naver",
                "title": item.get("상품명", ""),
                "price": price,
                "link": item.get("제품 링크", "")
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

    # 가격 정렬 후 최저가 순으로 30개만 리턴
    allResults = naverResults + ebayResults + gmarketResults
    sortedResults = sorted(allResults, key=lambda x: x["price"])
    return sortedResults[:30]
