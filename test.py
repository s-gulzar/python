import tkinter
root = tkinter.Tk(  )
for r in range(10):
   for c in range(8):
      tkinter.Label(root, text='Gulzar Ahmad Shaik     ', borderwidth=1 ).grid(row=r,column=c)
root.mainloop()