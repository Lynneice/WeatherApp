#
import tkinter as tk

HEIGHT = 500
WIDTH = 600
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH )
canvas.pack()

background_image=tk.PhotoImage(file='rainwindow.jpg')
backgroun_label= tk.Label(root, image = background_image)
background_label.place(relheight=1, relwidth=1)


"""using the place method is a geometry manager that organizes widgets 
in a table-like structure within the parent widget. relx=0.1 (relative x set to 10%
will add padding to either side on the x axis)
"""
frame = tk.Frame(root, bg = '#ABDEDC', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth =0.65, relheight=1)

button = tk.Button(frame, text = "Test Button", font=40, bg = '#8A9797', fg = '#ABC7DE')
button.place(relx=0.7, relheight=1, relwidth=0.3 )



lower_frame = tk.Frame(root, bg='#ABDEDC', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg= 'white')
label.place(relwidth=1, relheight=1)

root.mainloop()