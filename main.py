import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import TicTacToeGUI

class PlayerChooserApp:
    def __init__(self,root):
        self.root = root
        self.root.state("normal")
        self.root.geometry("500x500+550+80")
        self.root.title("Player Chooser")

        self.create_widgets()

    def create_widgets(self):
        two_player_btn = ctk.CTkButton(self.root, width=340, height=70, border_width=5, corner_radius=8,
                                       text="TWO PLAYER", font=("Arial", 30), command=self.two_player_command)
        two_player_btn.place(x=85, y=100)

        ai_computer_btn = ctk.CTkButton(self.root, width=340, height=70, border_width=5, corner_radius=8,
                                        text="AI Computer", font=("Arial", 30), compound="left",
                                        command=self.computer_ai_command)
        ai_computer_btn.place(x=85, y=200)

        random_computer_btn = ctk.CTkButton(self.root, width=340, height=70, border_width=5, corner_radius=8,
                                            text="Random Computer", font=("Arial", 30), command=self.computer_command)
        random_computer_btn.place(x=85, y=300)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def trynum(self, *args):
        try:
            int(self.number.get())
        except ValueError:
            alls = self.number_var.get()
            filtered_alls = ''.join(char for char in alls if char.isnumeric())
            self.number_var.set(filtered_alls)

    def run_ai_computer(self):
        if self.number_var.get() =="" or int(self.number_var.get()) < 1:
            messagebox.showerror("Tic Tac Toe", "Enter vaild number of rounds")
        else:
            self.clear_frame(self.root)
            tic_tac_toe = TicTacToeGUI(self.root, self.radio_var.get(), self.number_var.get(), self.x_name_var.get(), "AI",self.p_var.get())
            tic_tac_toe.run()

    def computer_ai_command(self):
        self.clear_frame(self.root)
        self.root.configure(fg_color="white")

        first_name = ctk.CTkFrame(self.root, fg_color="white")
        first_name.place(x=170, y=100)
        self.p_var=ctk.StringVar()
        combobox = ctk.CTkComboBox(first_name,values=["X", "O"], variable=self.p_var,state="readonly",width=50)
        combobox.place(x=0,y=0)
        combobox.set("X")  # set initial value
        self.x_name_var =ctk.StringVar()
        self.x_name = ctk.CTkEntry(first_name, placeholder_text="Name of Player",textvariable=self.x_name_var,width=110)
        self.x_name.place(x=60, y=0)

        num_of_game_frame = ctk.CTkFrame(self.root, fg_color="white")
        num_of_game_frame.place(x=170, y=150)
        games_label = ctk.CTkLabel(num_of_game_frame, text="#", font=("Arial", 30))
        games_label.place(x=0, y=0)
        self.number_var = tk.StringVar()
        self.number = ctk.CTkEntry(num_of_game_frame, placeholder_text="Number of Game", textvariable=self.number_var)
        self.number_var.trace("w", self.trynum)
        self.number.place(x=30, y=0)

        self.radio_var = ctk.StringVar(value="X")
        radio_frame = ctk.CTkFrame(self.root, fg_color="white")
        my_rad1 = ctk.CTkRadioButton(radio_frame, text="X is First", value="X",
                                     variable=self.radio_var,
                                     hover=True,
                                     font=("Arial", 22),
                                     )
        my_rad1.pack(pady=10)

        my_rad2 = ctk.CTkRadioButton(radio_frame, text="O is First", value="O",
                                     variable=self.radio_var,
                                     hover=True,
                                     font=("Arial", 22),
                                     )
        my_rad2.pack(pady=10)
        radio_frame.place(x=170, y=200)

        run_btn = ctk.CTkButton(self.root, text="RUN", font=('consolas', 24), command=self.run_ai_computer)
        run_btn.place(x=170, y=300)
        run_btn = ctk.CTkButton(self.root, text="BACK", font=('consolas', 24), command=self.back,fg_color="#99582a")
        run_btn.place(x=170, y=350)

    def run_computer(self):
        if self.number_var.get() =="" or int(self.number_var.get()) < 1:
            messagebox.showerror("Tic Tac Toe", "Enter vaild number of rounds")
        else:
            self.clear_frame(self.root)
            tic_tac_toe = TicTacToeGUI(self.root, self.radio_var.get(), self.number_var.get(), self.p_name_var.get(), "Random",self.p_var.get())

            tic_tac_toe.run_random()

    def computer_command(self):
        self.clear_frame(self.root)
        self.root.configure(fg_color="white")

        first_name = ctk.CTkFrame(self.root, fg_color="white")
        first_name.place(x=170, y=100)
        self.p_var=ctk.StringVar()
        combobox = ctk.CTkComboBox(first_name,values=["X", "O"], variable=self.p_var,state="readonly",width=50)
        combobox.place(x=0,y=0)
        combobox.set("X")  # set initial value
        self.p_name_var=ctk.StringVar()
        self.p_name = ctk.CTkEntry(first_name, placeholder_text="Name of Player",textvariable=self.p_name_var,width=110)
        self.p_name.place(x=60, y=0)

        num_of_game_frame = ctk.CTkFrame(self.root, fg_color="white")
        num_of_game_frame.place(x=170, y=150)
        games_label = ctk.CTkLabel(num_of_game_frame, text="#", font=("Arial", 30))
        games_label.place(x=0, y=0)
        self.number_var = tk.StringVar()
        self.number = ctk.CTkEntry(num_of_game_frame, placeholder_text="Number of Game", textvariable=self.number_var)
        self.number_var.trace("w", self.trynum)

        self.number.place(x=30, y=0)

        self.radio_var = ctk.StringVar(value="X")
        radio_frame = ctk.CTkFrame(self.root, fg_color="white")
        my_rad1 = ctk.CTkRadioButton(radio_frame, text="X is First", value="X",
                                     variable=self.radio_var,
                                     hover=True,
                                     font=("Arial", 22),
                                     )
        my_rad1.pack(pady=10)

        my_rad2 = ctk.CTkRadioButton(radio_frame, text="O is First", value="O",
                                     variable=self.radio_var,
                                     hover=True,
                                     font=("Arial", 22),
                                     )
        my_rad2.pack(pady=10)
        radio_frame.place(x=170, y=200)

        run_btn = ctk.CTkButton(self.root, text="RUN", font=('consolas', 24), command=self.run_computer)
        run_btn.place(x=170, y=300)
        run_btn = ctk.CTkButton(self.root, text="BACK", font=('consolas', 24), command=self.back,fg_color="#99582a")
        run_btn.place(x=170, y=350)

    def run_two(self):
        if self.number_var.get() =="" or int(self.number_var.get()) < 1:
            messagebox.showerror("Tic Tac Toe", "Enter vaild number of rounds")
        else:
            self.clear_frame(self.root)
            tic_tac_toe = TicTacToeGUI(self.root, self.radio_var.get(), self.number_var.get(), self.p_name_var.get(),
                                   self.p2_name_var.get(),"")
            tic_tac_toe.run_p()

    def open_alert(self):
        def coun():
            print("ds")
            top.destroy()
        top = tk.Toplevel()  # create window if its None or destroye
        top.geometry("600x300+650+200")
        top.title("Python")
        label = ctk.CTkLabel(top, text="ToplevelWindow")
        label.place(x=150,y=50)
        coun_btn = ctk.CTkButton(top, text="coun", font=('consolas', 24), command=coun)
        coun_btn.place(x=30, y=100)
        end_btn = ctk.CTkButton(top, text="End", font=('consolas', 24), command="",fg_color="#99582a")
        end_btn.place(x=230, y=100)
        top.mainloop()

    def back(self):
        self.clear_frame(self.root)
        app = PlayerChooserApp(self.root)
        app.mainloop()
    def two_player_command(self):
        self.clear_frame(self.root)
        self.root.configure(fg_color="white")

        self.p_name_var = ctk.StringVar()
        self.p2_name_var = ctk.StringVar()
        first_name = ctk.CTkFrame(self.root, fg_color="white")
        first_name.place(x=170, y=100)
        x_label = ctk.CTkLabel(first_name, text="X", font=("Arial", 30))
        x_label.place(x=0, y=0)
        self.x_name = ctk.CTkEntry(first_name, placeholder_text="Name of first Player",textvariable=self.p_name_var)
        self.x_name.place(x=30, y=0)
        secound_name = ctk.CTkFrame(self.root, fg_color="white")
        secound_name.place(x=170, y=150)
        o_label = ctk.CTkLabel(secound_name, text="O", font=("Arial", 30))
        o_label.place(x=0, y=0)
        self.o_name = ctk.CTkEntry(secound_name, placeholder_text="Name of secound Player",textvariable=self.p2_name_var)
        self.o_name.place(x=30, y=0)

        num_of_game_frame = ctk.CTkFrame(self.root, fg_color="white")
        num_of_game_frame.place(x=170, y=200)
        games_label = ctk.CTkLabel(num_of_game_frame, text="#", font=("Arial", 30))
        games_label.place(x=0, y=0)
        self.number_var=ctk.StringVar()
        self.number = ctk.CTkEntry(num_of_game_frame, placeholder_text="Number of Game",textvariable=self.number_var)
        self.number_var.trace("w", self.trynum)

        self.number.place(x=30, y=0)

        self.radio_var = ctk.StringVar(value="X")
        radio_frame = ctk.CTkFrame(self.root, fg_color="white")
        my_rad1 = ctk.CTkRadioButton(radio_frame, text="X is First", value="X",
                                     variable=self.radio_var,
                                     hover=True,
                                     font=("Arial", 22),
                                     )
        my_rad1.pack(pady=10)

        my_rad2 = ctk.CTkRadioButton(radio_frame, text="O is First", value="O",
                                     variable=self.radio_var,
                                     hover=True,
                                     font=("Arial", 22),
                                     )
        my_rad2.pack(pady=10)
        radio_frame.place(x=170, y=250)

        run_btn = ctk.CTkButton(self.root, text="RUN", font=('consolas', 24), command=self.run_two)
        run_btn.place(x=170, y=350)
        back_btn = ctk.CTkButton(self.root, text="Back", font=('consolas', 24), command=self.back,fg_color="#99582a")
        back_btn.place(x=170, y=400)

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = ctk.CTk()
    app = PlayerChooserApp(root)
    app.mainloop()
