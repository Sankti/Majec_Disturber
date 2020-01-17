from tkinter import *
from threading import Thread
 
running = False
 
window = Tk()
window.title("Majec Disturber")
window.geometry('300x360')
window.iconbitmap('icon_.ico')

majec1_img = PhotoImage(file="img\Majec_1.gif")
majec1_photo_label = Label(window, image=majec1_img)
majec2_img = PhotoImage(file="img\Majec_2.gif")
majec2_photo_label = Label(window, image=majec2_img)
majec3_img = PhotoImage(file="img\Majec_3.gif")
majec3_photo_label = Label(window, image=majec3_img)
majec4_img = PhotoImage(file="img\Majec_4.gif")
majec4_photo_label = Label(window, image=majec4_img)
 
title = Label(window, text="Majec Disturber®", fg="brown", font=("Times New Roman", 28, "bold"))
undertitle = Label(window, text="Raging Majec Simulator™", fg="black", font=("arial", 14))
copyright = Label(window, text="©2020 King Adam Corporation", fg="grey", font=("arial", 8))
message_box = Text(window, width=25, height=2, wrap=WORD, fg="black", font=("Courier New", 10))
button = Button(window, text="Disturb Majec", bg="khaki", fg="dim gray", font=("Courier New", 14, "bold"))
message_box.config(state=DISABLED)

def write(string):
    message_box.config(state=NORMAL)
    message_box.insert("end", string)
    message_box.see("end")
    message_box.config(state=DISABLED)

rage_level = 0

def start_count(event):
    global running
    write("\n" + "\n" + "Commencing disturbance...")
    running = True
    majec2_photo_label.grid(row=3, columnspan=3, pady=20)
    global rage_level
    rage_level += 1
	
def evaluate():
	majec1_photo_label.grid_forget()
	majec2_photo_label.grid_forget()
	majec3_photo_label.grid_forget()
	majec4_photo_label.grid_forget()
	
	if rage_level < 3:
		majec1_photo_label.grid(row=3, columnspan=3, pady=20)
		write("\n" + "\n" + "Majec is unamused")
	elif rage_level < 5:
		majec3_photo_label.grid(row=3, columnspan=3, pady=20)
		write("\n" + "\n" + "Majec is raging!")
	else:
		majec4_photo_label.grid(row=3, columnspan=3, pady=20)
		write("\n" + "\n" + "Majec has had it!!!")

def stop_count(event):
    global running
    running = False
    evaluate()

button.bind('<ButtonPress-1>',start_count)
button.bind('<ButtonRelease-1>',stop_count)

title.grid(row=0, columnspan=3)
undertitle.grid(row=1, columnspan=3)
copyright.grid(row=2, columnspan=3)
majec1_photo_label.grid(row=3, columnspan=3, pady=20)
message_box.grid(row=4, columnspan=3, pady=20)
button.grid(row=5, column=1)
write("Hold the button to enhance disturbance.")
 
window.mainloop()
