from inputpkg.inputWindow import makeInputWindow, getQuery
from webDataFetchpkg.compareAndSort import comparePrices
from Outputpkg.outputWindow import makeOutputWindow

# 입력 윈도우 만들기
makeInputWindow()

# 상품명 가져오기 및 확인
query = getQuery()

if not query.strip():
    exit()

# 가져온 상품명으로 웹사이트에서 데이터 추출한 후 리스트로 정리
results = comparePrices(query)

# 윈도우 만들고 결과 출력
makeOutputWindow(results)
