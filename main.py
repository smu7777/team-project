from tkinter import *
from tkinter import messagebox
from inputpkg.inputWindow import makeInputWindow, getQuery
from webDataFetchpkg.playwright import compare_prices
from ListAndOutputpkg.compileResultList import makeList
from ListAndOutputpkg.outputWindow import printList

# 실행은 여기서 합니다

# 메인 윈도우 만들기
makeInputWindow()

# 상품명 가져오기 및 확인
query = getQuery()

if not query.strip():
    exit()

# 가져온 상품명으로 웹사이트에서 데이터 추출하기
results = compare_prices(query)

# 리스트 만들기 (리스트명은 infoList로 설정)
infoList = makeList(results)

# 결과 출력 (추후 GUI로 변경 예정)
printList(infoList)
