import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

root = tk.Tk()

# definition
def num_to_str(msg):
    ones = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]

    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen"
    ]

    tys = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"
    ] # リストを作成

    if msg == 0: # 0の時はzeroを返す
        return "zero"
    elif msg < 10: # nが一桁の時はonesから返す
        return ones[msg]
    elif msg < 20: # nが二桁の時はteensから返す
        return teens[msg - 10] # インデックスと対応させる(ex:n = 12のとき、インデックスは2番目(12 - 10 = 2))
    elif msg < 100: # nが100未満の時はtysとonesを組み合わせる
        ten = tys[msg // 10] # 10の位を取り出す
        one = ones[msg % 10] # 1の位(10で割ったときの余り)を取り出す
        if one: # もし1の位があれば"-"で繋げる
            return ten + "-" + one
        else: # なければtenをそのまま返す
            return ten
    else: #nが三桁のとき
        hundred = ones[msg // 100] + " hundred" #100の位の数字を取り出す
        rest = msg % 100 # 下二桁を取得
        if rest == 0: # もし下二桁が0ならそのままhundredを返す
            return hundred
        else: # 下二桁があるならhundredとandを繋いで下二桁の英語を返す
            return hundred + " and " + num_to_str(rest)

# Setting up some windows properties
scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()
x = (scr_width - 450) // 2
y = (scr_height - 450) // 2
root.title("Number Translator")
root.minsize(200, 200)
root.geometry(f"450x450+{x}+{y}")
root.resizable(False, False)

def WhenButtonClicked(event = None):
    msg = ent.get()
    try:
        if msg:
            messagebox.showinfo("Answer", num_to_str(int(msg)))
        else:
            messagebox.showwarning("Oohps!", "You entered nothing. :(")
    except:
        messagebox.showerror("Error", "・Character string\n           or\n・Number over 1000")
    ent.delete(0, tk.END)

# Create two labels
tk.Label(root, text="Number Translator", font=("Helvetica", 20)).pack(expand=True)
tk.Label(root, text="Enter the number:\n(Please enter less than 1000)").pack()

# Create a button
ent = tk.Entry(root)
ent.pack()
btn = tk.Button(root, text="Click Here!", command=WhenButtonClicked, bg="green", fg="white")
btn.pack(side=tk.BOTTOM, expand=True)

root.bind("<Return>", WhenButtonClicked)
root.mainloop()