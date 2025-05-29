from tkinter import *
from tkinter import messagebox
from interfacepkg.mainWindow import makingWindow, getQuery
from webDataFetchpkg.playwright import compare_prices

# 실행은 여기서 합니다

# 메인 윈도우 만들기
## 매우 심각한 문제점 ##: makingWindow() 안의 mainloop()가 끝나야 다음 줄이 실행되므로 창이 꺼진 후에 파싱이 실행함.
## 예상되는 해결책 ##: 입력값을 받은 후에 창을 닫고 파싱을 실행함 root.destroy()
makingWindow()

# 상품명 가져오기
query = getQuery()

# 가져온 상품명으로 웹사이트에서 데이터 추출하기
results = compare_prices(query)

#리스트 만들기()
print("\n📊 가격 비교 결과:")
for site, title, price in results:
    print(f"\n[{site}]\n상품명: {title}\n가격: {price}")