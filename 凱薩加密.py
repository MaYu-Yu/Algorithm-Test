import tkinter as tk
from tkinter import font
from tkinter.constants import BOTH 
from typing import Text

class Windows:
    def __init__(self):
# setting
    # set self.app 
        self.app =  tk.Tk()
        self.app.title("HW")
        self.app.geometry("332x365")
        self.app.resizable(0,0)
        self.app['bg'] = 'pink'
        self.frame1 = tk.Frame(self.app)
        self.frame2 = tk.Frame(self.app)
        
        self.font_style = ("標楷體", 20, 'bold')
    # set textBox
        self.right_text = tk.Text(self.frame1, font=self.font_style, width=8, height=10)
        self.move_text = tk.Text(self.frame1, font=self.font_style, width=5, height=10)
        self.left_text = tk.Text(self.frame1, font=self.font_style, width=8, height=10)
    # set btn
        self.right_btn = tk.Button(self.frame2, text = "加密->", \
            command= lambda: self.cc_password(True), font=self.font_style ).pack()
        self.left_btn = tk.Button(self.frame2, text = "<-解密", \
            command= lambda: self.cc_password(False), font=self.font_style ).pack()
      
    def cc_password(self, isRight):
        move = int(self.move_text.get(1.0, tk.END+"-1c"))
        cc_txt = ""
        if isRight: 
            now_txt = self.right_text
            other_txt = self.left_text
        else:
            now_txt = self.left_text   
            other_txt = self.right_text   
            move = -move

        for i in now_txt.get(1.0, tk.END+"-1c"):
            cc_txt += chr(ord(i)+move)
        other_txt.delete(1.0, tk.END)
        other_txt.insert(tk.END, cc_txt)

    def start(self):
        self.frame1.pack()        
        self.frame2.pack()  
        self.right_text.pack(side=tk.LEFT)
        self.move_text.pack(side=tk.LEFT)
        self.left_text.pack(side=tk.LEFT)

        self.app.mainloop()
if __name__ == "__main__":
    app = Windows()
    app.start()