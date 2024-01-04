
import tkinter as tk

root=tk.Tk()
root.title("simple calculator")

def on_button_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0,tk.END)
            entry.insert(tk.END,str(result))
        except Exception as e:
            entry.delete(0,tk.END)
            entry.insert(tk.END,"Error")
    elif button_text == "C":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,button_text)

entry=tk.Entry(root,width=12,font=("Arial",17))
entry.grid(row=0,column=0,columnspan=4)


buttons=[
    '7','8','9','/',
    '4','5','6','*',
    '0','.','C','+',
    '=',
]

row_index,col_index =1,0
for button_text in buttons:
    button=tk.Button(root,text=button_text,width=5,height=2,font=('Arial',15),command=lambda btn=button_text:on_button_click(btn))
    button.grid(row=row_index,column=col_index)
    col_index += 1
    if col_index >3:
        col_index = 0
        row_index +=1
        
root.mainloop()