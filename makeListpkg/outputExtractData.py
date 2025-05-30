def printList(infoList):
    print("\n📊 가격 비교 결과:")
    for item in infoList:
        print(f"\n[{item['사이트']}]\n상품명: {item['상품명']}\n가격: {item['가격']}")