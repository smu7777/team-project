def makeInfoList(results):
    infoList = []
    for item in results:
        infoList.append({
            "site": item["source"],
            "title": item["title"],
            "price": item["price"],
            "link": item["link"]
        })
    return infoList
