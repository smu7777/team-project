from tkinter import *
from tkinter import messagebox

def makingWindow():
    # 메인 윈도우 설정
    window = Tk()
    window.title("웹사이트별 가격 비교 프로그램")
    window.geometry("1000x500")

    # 입력 안내
    label = Label(window, text="상품명을 입력해주세요", font=("나눔명조", 32,"bold"))
    label.pack(pady=10)

    # 텍스트 입력
    entry = Entry(window, width=80, font=("나눔명조", 24))
    entry.pack(padx=50)

    # 결과 출력
    searchLoading = Label(window, text="", fg="blue", wraplength=700, justify="left", font=("나눔명조", 24))
    searchLoading.pack(pady=10)

    # 검색 기능 구현
    def productSearch():
        query = entry.get()
        if not query.strip():
            messagebox.showwarning("입력 오류", "상품명을 입력하세요.")
            return
        searchLoading.config(text="검색 중입니다...")

    # 검색 버튼
    searchButton = Button(window, text="검색", command=productSearch, font=("나눔명조", 24), width=10)
    searchButton.pack(pady=10)

    # GUI 실행
    window.mainloop()