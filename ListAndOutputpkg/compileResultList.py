def makeList(results):
    infoList = []
    for site, title, price in results:
        infoList.append({
            "사이트": site,
            "상품명": title,
            "가격": price
    })
    return infoList