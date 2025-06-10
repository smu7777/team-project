from .ebayCrawler import search_ebay_with_selenium
from .gmarketCrawler import search_gmarket_with_selenium
from .NaverCrawler import SearchNaverShop

def compare_prices(query):
    # 네이버
    naver_items = SearchNaverShop(query, "MzsKEpdM0C7Sd6pHEJaJ", "WdnkycaTdf", 10)
    naver_result = []
    for item in naver_items:
        price = item.get("lprice", "")
        if price.isdigit():
            naver_result.append({
                "출처": "Naver",
                "상품명": item.get("title", "").replace("<b>", "").replace("</b>", ""),
                "가격": int(price),
                "제품 링크": item.get("link", "")
            })

    # 이베이
    ebay_items = search_ebay_with_selenium(query, 10)
    ebay_result = [{
        "출처": "eBay",
        "상품명": item["상품명"],
        "가격": item["가격"],
        "제품 링크": item["제품 링크"]
    } for item in ebay_items]

    # 지마켓
    gmarket_items = search_gmarket_with_selenium(query, 10)
    gmarket_result = [{
        "출처": "Gmarket",
        "상품명": item["상품명"],
        "가격": item["가격"],
        "제품 링크": item["제품 링크"]
    } for item in gmarket_items]

    return naver_result + ebay_result + gmarket_result
