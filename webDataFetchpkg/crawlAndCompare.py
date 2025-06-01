from playwright.sync_api import sync_playwright

# 네이버 쇼핑 크롤링 함수
def crawl_naver(query, context):
    page = context.new_page()
    url = f"https://search.shopping.naver.com/search/all?query={query}"
    page.goto(url)

    try:
        page.wait_for_timeout(3000)
        page.screenshot(path="naver_debug.png")

        title_elem = page.query_selector("div.product_title__BXAaB a")
        price_elem = page.query_selector("span.price_num__S2p_v")

        title = title_elem.inner_text() if title_elem else "상품명 없음"
        price = price_elem.inner_text() if price_elem else "가격 없음"
    except Exception as e:
        page.screenshot(path="naver_error.png")
        print("[네이버쇼핑 오류]", e)
        title = "상품명 없음"
        price = "가격 없음"
    page.close()
    return ("네이버쇼핑", title, price)

# 11번가 크롤링 함수
def crawl_11st(query, context):
    page = context.new_page()
    url = f"https://search.11st.co.kr/Search.tmall?kwd={query}"
    page.goto(url)

    try:
        page.wait_for_timeout(3000)
        page.screenshot(path="11st_debug.png")

        product_elem = page.query_selector("div.c_card_box")
        title_elem = product_elem.query_selector("div.name") if product_elem else None
        price_elem = product_elem.query_selector("strong.value") if product_elem else None

        title = title_elem.inner_text() if title_elem else "상품명 없음"
        price = price_elem.inner_text() if price_elem else "가격 없음"
    except Exception as e:
        page.screenshot(path="11st_error.png")
        print("[11번가 오류]", e)
        title = "상품명 없음"
        price = "가격 없음"
    page.close()
    return ("11번가", title, price)

# 아마존 크롤링 함수
def crawl_amazon(query, context):
    page = context.new_page()
    url = f"https://www.amazon.com/s?k={query}"
    page.goto(url)

    try:
        page.wait_for_timeout(3000)
        page.screenshot(path="amazon_debug.png")

        product_elem = page.query_selector("div.s-main-slot div[data-component-type='s-search-result']")
        title_elem = product_elem.query_selector("h2 span") if product_elem else None
        price_elem = product_elem.query_selector(".a-price .a-offscreen") if product_elem else None

        title = title_elem.inner_text() if title_elem else "상품명 없음"
        price = price_elem.inner_text() if price_elem else "가격 없음"
    except Exception as e:
        page.screenshot(path="amazon_error.png")
        print("[Amazon 오류]", e)
        title = "상품명 없음"
        price = "가격 없음"
    page.close()
    return ("Amazon", title, price)

# eBay 크롤링 함수
def crawl_ebay(query, context):
    page = context.new_page()
    url = f"https://www.ebay.com/sch/i.html?_nkw={query}"
    page.goto(url)

    try:
        page.wait_for_timeout(3000)
        page.screenshot(path="ebay_debug.png")

        title_elem = page.query_selector("li.s-item h3.s-item__title")
        price_elem = page.query_selector("li.s-item span.s-item__price")

        title = title_elem.inner_text() if title_elem else "상품명 없음"
        price = price_elem.inner_text() if price_elem else "가격 없음"
    except Exception as e:
        page.screenshot(path="ebay_error.png")
        print("[eBay 오류]", e)
        title = "상품명 없음"
        price = "가격 없음"
    page.close()
    return ("eBay", title, price)

# 메인 비교 함수
def compare_prices(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

        results = [
            crawl_naver(query, context),
            crawl_11st(query, context),
            crawl_amazon(query, context),
            crawl_ebay(query, context)
        ]

        browser.close()
        return results

# 실행 부분
if __name__ == "__main__":
    query = input("🔍 검색할 상품명을 입력하세요: ")
    results = compare_prices(query)

    print("\n📊 가격 비교 결과:")
    for site, title, price in results:
        print(f"\n[{site}]\n상품명: {title}\n가격: {price}")