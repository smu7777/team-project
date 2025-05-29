import tkinter as tk
from tkinter import messagebox

def makingWindow():
    # 검색 기능 구현
    def productSearch():
        query = entry.get()
        if not query.strip():
            messagebox.showwarning("입력 오류", "상품명을 입력하세요.")
            return
        result_label.config(text="검색 중입니다...")

    # 메인 윈도우 설정
    window = tk.Tk()
    window.title("최저가 상품 검색기")
    window.geometry("1000x500")

    # 입력 안내
    label = tk.Label(window, text="상품명을 입력해주세요:")
    label.pack(pady=10)

    # 텍스트 입력
    entry = tk.Entry(window, width=40)
    entry.pack()

    # 검색 버튼
    search_button = tk.Button(window, text="검색", command=productSearch)
    search_button.pack(pady=10)

    # 결과 출력
    result_label = tk.Label(window, text="", fg="blue", wraplength=350, justify="left")
    result_label.pack(pady=10)

    # GUI 실행
    window.mainloop()