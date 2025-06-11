from inputpkg.inputWindow import makeInputWindow, getQuery
from webDataFetchpkg.compareAndSort import comparePrices
from listAndOutputpkg.compileResultList import makeInfoList
from listAndOutputpkg.outputWindow import makeOutputWindow

# 입력 윈도우 만들기
makeInputWindow()

# 상품명 가져오기 및 확인
query = getQuery()

if not query.strip():
    exit()

# 가져온 상품명으로 웹사이트에서 데이터 추출하기
results = comparePrices(query)

# 각 상품의 정보를 담은 results 딕셔너리를 infoList에 담기
infoList = makeInfoList(results)

# 윈도우 만들고 결과 출력
makeOutputWindow(infoList)
