import os
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def searchEbayWithSelenium(query, maxResults=5):
    encodedQuery = urllib.parse.quote(query)
    url = f"https://www.ebay.com/sch/i.html?_nkw={encodedQuery}"

    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--window-size=1920,1080")
    chromeOptions.add_argument("--lang=en-US")
    chromeOptions.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url)
    time.sleep(3)

    items = driver.find_elements(By.CSS_SELECTOR, "li.s-item")
    results = []

    for item in items:
        try:
            titleElem = item.find_element(By.CSS_SELECTOR, ".s-item__title")
            title = titleElem.text.strip()

            if not title or "shop on ebay" in title.lower():
                continue

            priceText = item.find_element(By.CSS_SELECTOR, ".s-item__price").text.strip()
            priceClean = priceText.replace("$", "").replace(",", "").replace("KRW", "").strip()
            price = float(priceClean)

            link = item.find_element(By.CSS_SELECTOR, ".s-item__link").get_attribute("href").strip()

            results.append({
                "source": "eBay",
                "title": title,
                "price": int(price),
                "link": link
            })

            if len(results) >= maxResults:
                break
        except Exception:
            continue

    driver.quit()
    return results

def filterItemsByPriceThreshold(items):
    prices = [item["price"] for item in items if item["price"] > 0]
    if prices:
        avgPrice = sum(prices) / len(prices)
        threshold = avgPrice / 3.0
    else:
        threshold = 0

    filteredItems = [item for item in items if item["price"] > threshold]
    return filteredItems

def ebayItemResult(query, maxResults):
    items = searchEbayWithSelenium(query, maxResults)
    filteredItems = filterItemsByPriceThreshold(items)
    return filteredItems
