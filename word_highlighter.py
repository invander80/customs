import tkinter
from tkinter import Text, Tk

root = Tk()


def highlighter(char, event=None):
    length = len(char)
    index = int(round(float(txt.index(tkinter.INSERT)), 0))
    val = len(txt.get("1.0", "end-1c"))
    for x in range(len(txt.get("1.0", "end-1c"))):
        if char in txt.get(f"{index}.{x}", "end-1c") :
            val = x
            txt.tag_config("Hello", background=txt.cget("bg"), foreground="red")
    vals = str(val + length)
    txt.tag_add("Hello", f"{index}.{str(val)}", f"{index}.{vals}")


txt = Text(root)
txt.grid(columnspan=3)

root.bind("<Key>", lambda event: highlighter("Hello"))


root.mainloop()
