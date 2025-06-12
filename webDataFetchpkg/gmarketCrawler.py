import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def searchGmarketWithSelenium(query, maxResults=5):
    encodedQuery = urllib.parse.quote(query)
    url = f"https://browse.gmarket.co.kr/search?keyword={encodedQuery}"

    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--window-size=1920,1080")
    chromeOptions.add_argument("--lang=ko-KR")
    chromeOptions.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url)
    time.sleep(3)

    items = driver.find_elements(By.CSS_SELECTOR, "div.box__item-container")
    results = []

    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, "span.text__item").text.strip()
            priceText = item.find_element(By.CSS_SELECTOR, "strong.text__value").text.strip().replace(",", "")
            price = int(priceText)
            link = item.find_element(By.CSS_SELECTOR, "a.link__item").get_attribute("href").strip()

            results.append({
                "source": "Gmarket",
                "title": title,
                "price": price,
                "link": link
            })

            if len(results) >= maxResults * 2:  # 넉넉히 가져옴
                break
        except Exception:
            continue

    driver.quit()
    return results

def filterItems(items):
    prices = [item["price"] for item in items if item["price"] > 0]
    if prices:
        avgPrice = sum(prices) / len(prices)
        threshold = avgPrice / 3.0
    else:
        threshold = 0

    filteredItems = [item for item in items if item["price"] > threshold]
    return filteredItems

def gmarketItemResult(query, maxResults):
    items = searchGmarketWithSelenium(query, maxResults)
    filteredItems = filterItems(items)
    return filteredItems
