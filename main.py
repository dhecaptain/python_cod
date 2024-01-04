import tkinter as tk

root=tk.Tk()
root.title("Python")
root.geometry("800x600")

label=tk.Label(root,text="my first gui",font=("Arial",))
label.pack(padx=10,pady=10)

textbox=tk.Text(root,font=("Arial",10))
textbox.pack(padx=10)

button=tk.Button(root,text="show message",font=("Arial",18))
button.pack(padx=10,pady=10)

button=tk.Button(root,text="show message",font=("Arial",18),command=show_message)
button.pack(padx=10,pady=10)

def show_message():
        if check_state.get()==0:
            print(textbox.get('1.0',tk.END))
        else:
            messagebox.showinfo(title="Message",message=textbox.get('1.0',tk.END))



root.mainloop()
