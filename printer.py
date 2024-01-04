
import tkinter as tk

root=tk.Tk()

root.geometry("500x500")
root.title("DAVID")

label=tk.Label(root,text="my message",font=("Arial",18))
label.pack(padx=10,pady=10)



textbox=tk.Text(root,height=6,font=("Arial",18))
textbox.pack(padx=10,pady=10)

root.mainloop()