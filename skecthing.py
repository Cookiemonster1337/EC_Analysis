import tkinter as tk
from tkinter import Frame




frame_1 = tk.Tk()

frame_1.title("FRAME I")
frame_1.geometry("{}x{}".format(500, 350))
frame_1.maxsize(500, 350)

top_menu_frame = Frame(main_menu_frame, bg='blue', width=500, height=350)
top_menu_frame.grid_propagate(0)

bot_menu_frame = Frame(main_menu_frame, bg='green', width=500, height=50)
bot_menu_frame.grid_propagate(0)

top_menu_frame.grid(row=0)
bot_menu_frame.grid(row=1)


frame1_button = tk.Button(frame_1, text='Data Import',
                               width=40, command=)

frame_1.mainloop()


# frame_2 = tk.Tk()
#
# frame_2.title("FRAME II")
# frame_2.geometry("{}x{}".format(500, 350))
# frame_2.maxsize(500, 350)
#
# frame_2.mainloop()







