from tkinter import *

window = Tk()
window.title("웹사이트별 가격 비교")
window.geometry("1920x1080")

label = Label(window, text="테스트", font=("Arial", 100))
label.pack()

window.mainloop()

#제품명입력
from inputAndURLpkg import getProductName
getProductName.getProductName()


#각웹사이트의 검색URL 생성

#해당사이트의 HTML 요청 시 정상적 응답?

#수신받은 HTML BeautifulSoup으로 파싱

#원하는 제품 정보 추출 후 출력리스트 생성, 출력 데이터 출력