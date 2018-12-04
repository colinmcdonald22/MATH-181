from tkinter import *
import riemann


class IntegrationGUI:

    def __init__(self, master):
        self.master = master

        master.title("Riemann Sum Calculator")
        master.geometry("1120x480")
        master.resizable(False, False)
        master.configure(background='white')

        ########## Labeling/Instructions

        self.label = Label(master, text="Enter values in boxes and select a mode", font="16", background='white')
        self.label.place(x=20, y=20)

        ########## Enter Bounds/Rectangle Selection

        self.enter_b = Entry(master, text="1")
        self.enter_b.place(x=50, y=80)

        self.enter_a = Entry(master)
        self.enter_a.place(x=50, y=390)

        self.b_label = Label(master, text="b = ", background='white')
        self.b_label.place(x=20, y=80)

        self.a_label = Label(master, text="a = ", background='white')
        self.a_label.place(x=20, y=390)

        self.rectangle_selection_label = Label(master, text="Number of rectangles", background='white')
        self.rectangle_selection_label.place(x=180, y=430)
        self.rectangle_selection = Entry(master)
        self.rectangle_selection.place(x=180, y=450)

        ########## Enter Function

        self.enter_function = Entry(master)
        self.enter_function.place(x=145, y=245)

        self.enter_function_label = Label(master, text="dx", background='white')
        self.enter_function_label.place(x=270, y=245)

        ########## Mode Buttons

        self.mode_label = Label(master, text="Mode", background='white')
        self.mode_label.place(x=380, y=430)

        self.left_mode_button = Button(text="LEFT", command=lambda: self.update_mode("Left"))
        self.mid_mode_button = Button(text="MID", command=lambda: self.update_mode("Middle"))
        self.right_mode_button = Button(text="RIGHT", command=lambda: self.update_mode("Right"), relief=SUNKEN)

        self.left_mode_button.place(x=335, y=450)
        self.mid_mode_button.place(x=380, y=450)
        self.right_mode_button.place(x=425, y=450)

        ########## Functional Buttons

        self.integrate_button = Button(master, text="Update", command=self.integrate)
        self.integrate_button.place(x=400, y=240)

        self.integration_sign = Label(master, text="∫", font="Helvetica 180", background='white')
        self.integration_sign.place(x=70, y=115)

        # Insert default values
        self.enter_b.insert(0, "4")
        self.enter_a.insert(0, "-4")
        self.rectangle_selection.insert(0, "10")
        self.enter_function.insert(0, "3 * (x^2) + 1.5 * (x^3)")
        self.selected_mode = "Right"

        self.drawing_area = None
        self.integrate()

    def integrate(self):
        # Read values from text inputs
        func = self.enter_function.get().replace("^", "**")
        n = int(self.rectangle_selection.get())
        a = float(self.enter_a.get())
        b = float(self.enter_b.get())

        sum, delta_x, rectanges = riemann.compute_nth_riemann_sum(n, func, a, b, self.selected_mode)

        # If we're going to overwrite our old drawing we must call this
        if self.drawing_area:
            self.drawing_area.destroy()

        # Plot the results of the computation with matplotlib
        self.drawing_area = Canvas(self.master, width=600, height=500)
        self.drawing_area.pack(side=RIGHT, anchor=E)
        riemann.plot_riemann_sum(self.drawing_area, n, func, a, b, sum, delta_x, rectanges)

    def update_mode(self, mode):
        self.selected_mode = mode

        self.left_mode_button.config(relief=SUNKEN if mode == "Left" else RAISED)
        self.mid_mode_button.config(relief=SUNKEN if mode == "Middle" else RAISED)
        self.right_mode_button.config(relief=SUNKEN if mode == "Right" else RAISED)


root = Tk()
gui = IntegrationGUI(root)
root.mainloop()
