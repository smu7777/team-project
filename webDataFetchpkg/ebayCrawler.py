import os
import csv
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def search_ebay_with_selenium(query, max_results=5):
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.ebay.com/sch/i.html?_nkw={encoded_query}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)

    items = driver.find_elements(By.CSS_SELECTOR, "li.s-item")
    results = []

    for item in items:
        try:
            title_elem = item.find_element(By.CSS_SELECTOR, ".s-item__title")
            title = title_elem.text.strip()

            if not title or "shop on ebay" in title.lower():
                continue

            price_text = item.find_element(By.CSS_SELECTOR, ".s-item__price").text.strip()
            price_clean = price_text.replace("$", "").replace(",", "").replace("KRW", "").strip()
            price = float(price_clean)

            link = item.find_element(By.CSS_SELECTOR, ".s-item__link").get_attribute("href").strip()

            results.append({
                "상품명": title,
                "가격": int(price),
                "제품 링크": link
            })

            if len(results) >= max_results:
                break
        except Exception:
            continue

    driver.quit()
    return results

def save_filtered_csv(items, directory, filename):
    prices = [item["가격"] for item in items if item["가격"] > 0]
    if prices:
        avg_price = sum(prices) / len(prices)
        threshold = avg_price / 3.0
    else:
        threshold = 0

    filtered_items = [item for item in items if item["가격"] > threshold]
    sorted_items = sorted(filtered_items, key=lambda x: x["가격"])

    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)

    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["상품명", "가격", "제품 링크"])
        for item in sorted_items:
            writer.writerow([item["상품명"], item["가격"], item["제품 링크"]])

    return path, sorted_items

def print_lowest_items(items):
    if not items:
        print("검색 결과가 없습니다.")
        return

    print("\n=== 동일 상품명 중 최저가 항목 ===")
    print(f"{'상품명':<40} {'가격':<10} {'제품 링크'}")
    print("-" * 80)
    for item in items:
        name = item["상품명"]
        price = item["가격"]
        link = item["제품 링크"]
        short_name = name if len(name) <= 40 else name[:37] + "..."
        print(f"{short_name:<40} {price:<10} {link}")
    print("-" * 80)

def main():
    query = input("검색어를 입력하세요: ").strip()
    if not query:
        print("검색어가 비어 있습니다.")
        return

    items = search_ebay_with_selenium(query)
    if not items:
        print("검색 결과가 없습니다.")
        return

    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_dir = os.path.join(base_dir, "Data")
    csv_filename = "ProductPrice.csv"
    csv_path, filtered_items = save_filtered_csv(items, csv_dir, csv_filename)

    print_lowest_items(filtered_items)
    print(f"\n결과가 CSV 파일로 저장되었습니다: {csv_path}\n")

    print("=== 전체 출력 결과 ===")
    for item in filtered_items:
        print(f"{item['상품명']}\n가격: {item['가격']}\n링크: {item['제품 링크']}\n")

if __name__ == "__main__":
    main()
