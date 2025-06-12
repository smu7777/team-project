from .ebayCrawler import ebayItemResult
from .gmarketCrawler import gmarketItemResult
from .naverCrawler import naverItemResult

def comparePrices(query):
    # 크롤링
    naverItems = naverItemResult(query, 30)
    ebayItems = ebayItemResult(query, 30)
    gmarketItems = gmarketItemResult(query, 30)

    # 가격 정렬 후 최저가 순으로 30개만 리턴
    allResults = naverItems + ebayItems + gmarketItems
    sortedResults = sorted(allResults, key=lambda x: x["price"])
    return sortedResults[:30]
