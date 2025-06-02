import requests
import os
import csv

# 네이버 쇼핑 검색 API 호출
def SearchNaverShop(Query: str, ClientId: str, ClientSecret: str, Display: int = 10):
    NaverUrl = "https://openapi.naver.com/v1/search/shop.json"
    Headers = {
        "X-Naver-Client-Id": ClientId,
        "X-Naver-Client-Secret": ClientSecret
    }
    Params = {
        "query": Query,
        "display": Display
    }
    Response = requests.get(NaverUrl, headers=Headers, params=Params)
    if Response.status_code == 200:
        Data = Response.json()
        return Data.get("items", [])
    return []

# CSV 저장 및 평균 가격 기반 필터링
def SaveFilteredCsv(Items: list, CsvDir: str, CsvFilename: str):
    # 유효한 가격을 수집하여 평균과 임계값 계산
    PriceList = []
    for Item in Items:
        LPriceStr = Item.get("lprice", "").strip()
        if LPriceStr.isdigit():
            PriceList.append(int(LPriceStr))
    if PriceList:
        AvgPrice = sum(PriceList) / len(PriceList)
        Threshold = AvgPrice / 3.0
    else:
        Threshold = 0

    # 임계값 이하 항목 제외
    FilteredItems = []
    for Item in Items:
        LPriceStr = Item.get("lprice", "").strip()
        if not LPriceStr.isdigit():
            continue
        Price = int(LPriceStr)
        if Price <= Threshold:
            continue
        FilteredItems.append(Item)

    # 최저가 오름차순 정렬
    SortedItems = sorted(
        FilteredItems,
        key=lambda x: int(x.get("lprice", "0"))
    )

    # 디렉토리 생성
    if not os.path.exists(CsvDir):
        os.makedirs(CsvDir, exist_ok=True)

    FullPath = os.path.join(CsvDir, CsvFilename)

    # CSV 쓰기
    with open(FullPath, "w", encoding="utf-8-sig", newline="") as FileHandle:
        Writer = csv.writer(FileHandle, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
        Writer.writerow(["상품명", "최저가", "제품 사이트"])
        for Item in SortedItems:
            RawTitle = Item.get("title", "")
            CleanTitle = RawTitle.replace("<b>", "").replace("</b>", "")
            LPrice = Item.get("lprice", "")
            Link = Item.get("link", "")
            Writer.writerow([CleanTitle, LPrice, Link])

    return FullPath

# 동일 상품명 중 최저가 출력
def FilterLowestPriceFromCsv(InputCsvPath: str):
    LowestPriceDict = {}
    with open(InputCsvPath, "r", encoding="utf-8-sig", newline="") as FileHandle:
        Reader = csv.DictReader(FileHandle)
        for Row in Reader:
            ProductName = Row.get("상품명", "").strip()
            PriceStr = Row.get("최저가", "").strip()
            ProductSite = Row.get("제품 사이트", "").strip()
            if not ProductName or not PriceStr.isdigit():
                continue
            Price = int(PriceStr)
            if (ProductName not in LowestPriceDict) or (Price < LowestPriceDict[ProductName][0]):
                LowestPriceDict[ProductName] = (Price, ProductSite)

    print("=== 동일 상품명 중 최저가 항목 ===")
    print(f"{'상품명':<40} {'최저가':<10} {'제품 사이트'}")
    print("-" * 80)
    for ProductName, (Price, ProductSite) in LowestPriceDict.items():
        DisplayName = ProductName if len(ProductName) <= 40 else ProductName[:37] + "..."
        print(f"{DisplayName:<40} {Price:<10} {ProductSite}")
    print("-" * 80)

def Main():
    # 검색어 입력
    Query = input("검색어를 입력하세요: ").strip()
    if not Query:
        return

    # API 호출
    ClientId = "MzsKEpdM0C7Sd6pHEJaJ"
    ClientSecret = "WdnkycaTdf"
    Items = SearchNaverShop(Query, ClientId, ClientSecret)
    if not Items:
        return

    # CSV 저장 및 필터링
    BaseDir = os.path.dirname(os.path.abspath(__file__))
    CsvDir = os.path.join(BaseDir, "Data")
    CsvFilename = "ProductPrice.csv"
    CsvPath = SaveFilteredCsv(Items, CsvDir, CsvFilename)

    # 최저가 출력
    FilterLowestPriceFromCsv(CsvPath)

if __name__ == "__main__":
    Main()