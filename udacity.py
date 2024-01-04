
import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hell Tkinter")
        
        self.label_text="Choose one"
        self.label=tk.Label(self,text=self.label_text)
        self.label.pack(fill=tk.BOTH,expand=1,padx=100,pady=30)
        
        self.hello_button=tk.Button(self,text="Say Hello",command=self.say_hello)
        self.hello_button.pack(side=tk.LEFT,padx=(20,0),pady=(0,20))
        
        self.goodbye_button=tk.Button(self,text="GoodBye",command=self.say_goodbye)
        self.goodbye_button.pack(side=tk.RIGHT,padx=(0,20),pady=(0,20))
        
        
    def say_hello(self):
        self.label_text="Hello World"
        self.label.config(text=self.label_text)
        
    def say_goodbye(self):
        self.label.text="Goodbye \n (closing in 2 seconds)"
        self.label.config(text=self.label.text)
        self.after(2000,self.destroy)
        
if __name__=="__main__":
    window=Window()
    window.mainloop()