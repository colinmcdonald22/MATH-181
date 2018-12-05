from tkinter import *
from tkinter.ttk import Combobox
import riemann


class IntegrationGUI:

    def __init__(self, master):
        self.master = master

        master.title("Riemann Sum Calculator")
        master.geometry("1020x480")
        master.resizable(False, False)
        master.configure(background='white')

        ########## Labels

        self.integration_sign = Label(master, font=("Calibri", 250), text="∫", background='white')
        self.integration_sign.place(x=70, y=0)

        self.b_label = Label(master, text="b = ", background='white')
        self.b_label.place(x=125, y=75)

        self.a_label = Label(master, text="a = ", background='white')
        self.a_label.place(x=75, y=385)

        self.rectangle_selection_label = Label(master, text="Rectangles", background='white')
        self.rectangle_selection_label.place(x=100, y=425)

        self.enter_function_label = Label(master, text="dx", background='white')
        self.enter_function_label.place(x=360, y=240)

        self.mode_label = Label(master, text="Mode", background='white')
        self.mode_label.place(x=215, y=425)

        ########## Enter Bounds/Rectangle Selection

        self.enter_b = Entry(master, width=5)
        self.enter_b.place(x=150, y=75)

        self.enter_a = Entry(master, width=5)
        self.enter_a.place(x=100, y=385)

        self.rectangle_selection = Entry(master, width=5)
        self.rectangle_selection.place(x=115, y=445)

        ########## Function

        self.enter_function = Entry(master, width=31)
        self.enter_function.place(x=170, y=240)

        ########## Mode

        self.mode_selector = Combobox(master, text="Right", values=["Left", "Middle", "Right"], state='readonly', width=8)
        self.mode_selector.place(x=200, y=445)

        ########## Functional Buttons

        self.integrate_button = Button(master, text="Update", command=self.integrate)
        self.integrate_button.place(x=315, y=440)

        # Insert default values
        self.enter_b.insert(0, "4")
        self.enter_a.insert(0, "-4")
        self.rectangle_selection.insert(0, "10")
        self.enter_function.insert(0, "3 * (x^2) + 1.5 * (x^3)")
        self.mode_selector.set("Right")

        self.drawing_area = None
        self.integrate()

    def integrate(self):
        # Read values from text inputs
        func = self.enter_function.get().replace("^", "**")
        n = int(self.rectangle_selection.get())
        a = float(self.enter_a.get())
        b = float(self.enter_b.get())

        sum, delta_x, rectangles = riemann.compute_nth_riemann_sum(n, func, a, b, self.mode_selector.get())

        # If we're going to overwrite our old drawing we must call this
        if self.drawing_area:
            self.drawing_area.destroy()

        # Plot the results of the computation with matplotlib
        self.drawing_area = Canvas(self.master, width=600, height=500)
        self.drawing_area.pack(side=RIGHT, anchor=E)
        riemann.plot_riemann_sum(self.drawing_area, n, func, a, b, sum, delta_x, rectangles)


root = Tk()
gui = IntegrationGUI(root)
root.mainloop()
