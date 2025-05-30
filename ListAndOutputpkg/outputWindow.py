from tkinter import *

def makeOutputWindow(infoList):
    window = Tk()
    window.title("웹사이트  가격 비교 프로그램")
    window.geometry("1000x1200")

    mainFrame = Frame(window)
    mainFrame.pack(fill="both", expand=True)

    for item in infoList:
        frame = Frame(mainFrame, bd=1, relief="solid")
        frame.pack(fill="x", padx=20, pady=16)

    label1 = Label(frame, text=f"[{item['사이트']}]", font=("나눔명조", 24, "bold"), anchor="w")
    label1.pack(anchor="w", padx=20, pady=(10, 0))

    label2 = Label(frame, text=f"상품명: {item['상품명']}", font=("나눔명조", 20), anchor="w")
    label2.pack(anchor="w", padx=40, pady=(5, 0))

    label3 = Label(frame, text=f"가격: {item['가격']}", font=("나눔명조", 20), anchor="w")
    label3.pack(anchor="w", padx=40, pady=(0, 10))

    window.mainloop()