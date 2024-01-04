
import tkinter as tk

root= tk.Tk()

root.geometry("500x500")
root.title("My first gui")

label=tk.Label(root,text="Hello world!",font=("Arial",16))
label.pack(padx=20,pady=15)

textbox=tk.Text(root,height=3,font=("Arial",18))
textbox.pack(padx=10)

buttonFrame=tk.Frame(root)
buttonFrame.columnconfigure(0,weight=1)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=1)

btn1=tk.Button(buttonFrame,text="1",font=("Arial",18))
btn1.grid(rows=1,column=0,sticky=tk.W+tk.E)

btn2=tk.Button(buttonFrame,text="2",font=("Arial",18))
btn2.grid(rows=1,column=1,sticky=tk.W+tk.E)

btn3=tk.Button(buttonFrame,text="3",font=("Arial",18))
btn3.grid(rows=1,column=0,sticky=tk.W+tk.E)

btn4=tk.Button(buttonFrame,text="4",font=("Arial",18))
btn4.grid(rows=2,column=0,sticky=tk.W+tk.E)

btn5=tk.Button(buttonFrame,text="5",font=("Arial",18))
btn5.grid(rows=2,column=1,sticky=tk.W+tk.E)

btn6=tk.Button(buttonFrame,text="6",font=("Arial",18))
btn6.grid(rows=2,column=2,sticky=tk.W+tk.E)

btn7=tk.Button()

buttonFrame.pack(fill='x')

root.mainloop()
