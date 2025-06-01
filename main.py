from inputpkg.inputWindow import makeInputWindow, getQuery
from webDataFetchpkg.crawlAndCompare import compare_prices
from listAndOutputpkg.compileResultList import makeList
from listAndOutputpkg.outputWindow import makeOutputWindow
from webDataFetchpkg.naverCrawler import crawlNaver

# 실행은 여기서 합니다

# 입력 윈도우 만들기
makeInputWindow()

# 상품명 가져오기 및 확인
query = getQuery()

if not query.strip():
    exit()

# 가져온 상품명으로 웹사이트에서 데이터 추출하기
#results = compare_prices(query)

# 네이버 크롤러
crawlNaver(query)

# 리스트 만들기 (리스트명은 infoList로 설정)
#infoList = makeList(results)

# 윈도우 만들고 결과 출력
#makeOutputWindow(infoList)
