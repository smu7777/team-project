from tkinter import *
import webbrowser

def makeOutputWindow(infoList):
    window = Tk()
    window.title("웹사이트 가격 비교 프로그램")
    window.geometry("1000x1200")

    canvas = Canvas(window)
    scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    scrollable_frame = Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    for item in infoList:
        frame = Frame(scrollable_frame, bd=1, relief="solid")
        frame.pack(fill="x", padx=20, pady=16)

        labelSite = Label(frame, text=f"[{item['site']}]", font=("나눔명조", 24, "bold"), anchor="w")
        labelSite.pack(anchor="w", padx=20, pady=(10, 0))

        labelTitle = Label(frame, text=f"상품명: {item['title']}", font=("나눔명조", 20), anchor="w")
        labelTitle.pack(anchor="w", padx=40, pady=(5, 0))

        labelPrice = Label(frame, text=f"가격: {item['price']}원", font=("나눔명조", 20), anchor="w")
        labelPrice.pack(anchor="w", padx=40, pady=(0, 5))

        labelLink = Label(frame, text=f"링크: {item['link']}", font=("나눔명조", 16), fg="blue", cursor="hand2", anchor="w")
        labelLink.pack(anchor="w", padx=40, pady=(0, 10))
        labelLink.bind("<Button-1>", lambda e, url=item['link']: webbrowser.open(url))

    window.mainloop()