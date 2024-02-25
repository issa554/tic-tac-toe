import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
class TicTacToeGUI:
    def go_home(self):
        from main import PlayerChooserApp
        clear_frame(self.root)
        app = PlayerChooserApp(self.root)
        app.mainloop()
    def go_back(self):
        from main import PlayerChooserApp
        clear_frame(self.root)
        app = PlayerChooserApp(self.root)
        if self.s_name=="AI":
            app.computer_ai_command()
        elif self.s_name=="Random":
            app.computer_command()
        else:
            app.two_player_command()

    def __init__(self,root,f,num,f_name,s_name,c):
        self.root = root
        clear_frame(self.root)
        self.root.title("Tic Tac Toe")
        self.p1_sccore=0
        self.p2_sccore=0
        self.f=f#who is first
        self.num_of_game=num
        self.num_of_this=1
        self.current_player = f
        self.label = ctk.CTkLabel(self.root,text=self.current_player + " turn", font=('consolas',40))
        if s_name=="Random" or s_name=="AI":
            self.label.configure(text="your turn")
        self.label.place( x=550,y=30)
        self.left_frame = ctk.CTkFrame(self.root,width=350,fg_color="white",height=1000)
        self.left_frame.place( x=20,y=30)
        self.s_name=s_name
        self.f_name=f_name
        self.p1_frame = ctk.CTkFrame(self.left_frame,width=300,height=150,fg_color="#bde0fe")
        self.p1_frame.place(x=0,y=120)
        self.p2_frame = ctk.CTkFrame(self.left_frame,width=300,height=150,fg_color="#ffc8dd")
        self.p2_frame.place(x=0,y=300)
        self.frame = ctk.CTkFrame(self.root)
        self.frame.place(x=400,y=150)
        self.right_frame = ctk.CTkFrame(self.root,width=350,fg_color="white",height=1000)
        self.right_frame.place( x=900,y=30)
        self.result_frame = ctk.CTkFrame(self.right_frame,width=300,height=50,fg_color="#caf0f8")
        self.result_frame.place(x=0,y=120)
        self.stat_frame = ctk.CTkFrame(self.right_frame,width=300,height=270,fg_color="white")
        self.stat_frame.place(x=0,y=180)
        self.p1_name = ctk.CTkLabel(self.p1_frame,text=f_name+" (X)",font=("Arial",28))
        self.p1_name.place(x=10,y=10)
        self.p1_sccore_lable =ctk.CTkLabel(self.p1_frame,text="SCORE = 0",font=("Arial",28))
        self.p1_sccore_lable.place(x=10,y=50)
        self.p2_name = ctk.CTkLabel(self.p2_frame,text=s_name+f" (O)",font=("Arial",28))
        self.p2_name.place(x=10,y=10)
        self.c=c
        self.com="X"
        if self.c=="X":
            self.com="O"
        if c=="O":
            self.p2_name.configure(text=s_name+f" (X)")
            self.p1_name.configure(text=f_name+f" (O)")
        self.p2_sccore_lable =ctk.CTkLabel(self.p2_frame,text="SCORE = 0",font=("Arial",28))
        self.p2_sccore_lable.place(x=10,y=50)
        self.result =ctk.CTkLabel(self.result_frame,text="0/"+self.num_of_game+" Rounds",font=("Arial",28))
        self.result.place(x=10,y=10)
        back_button = ctk.CTkButton(self.left_frame, text="Back \"Rest Game\"", command=self.go_back, width=100,height=40,fg_color="#2b2d42",font=("Arial",18))
        back_button.place(x=10,y=520)
        home_button = ctk.CTkButton(self.left_frame, text="Back To Home", command=self.go_home, width=100,height=40,fg_color="#2b2d42",font=("Arial",18))
        home_button.place(x=10,y=470)


        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None, None, None] for _ in range(3)]

    def make_move(self, row, col):#for player aginst ai
        if self.board[row][col] == ' ' and self.check_winner() is False :
            self.board[row][col] = self.c
            self.buttons[row][col].configure(text=self.c, state="disabled")
            self.label.configure(text=("copmuter turn"))
            if self.check_winner()==self.c:
                    self.p1_sccore+=1
                    self.label.configure(text=("You wins"))
                    messagebox.showinfo("Tic Tac Toe", "You win!")
                    self.p1_sccore_lable.configure(text="SCORE = "+str(self.p1_sccore))
                    self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")
                    if self.num_of_this <int(self.num_of_game)  :
                        self.num_of_this+=1
                        self.reset_game()
            elif self.is_board_full():
                self.label.configure(text=("TIE"))
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")
                if self.num_of_this <int(self.num_of_game)  :
                    self.num_of_this+=1
                    self.reset_game()
            else:
                self.current_player = self.com
                self.computer_move()

    def random_move(self, row, col):
        if self.board[row][col] == ' ' and self.check_winner() is False:
            self.board[row][col] = self.c
            self.buttons[row][col].configure(text=self.c, state="disabled")
            self.label.configure(text=("copmuter turn"))
            if self.check_winner()==self.c:
                self.p1_sccore+=1
                self.p1_sccore_lable.configure(text="SCORE = "+str(self.p1_sccore))

                if int(self.p1_sccore) > (int(self.num_of_game))-int((self.num_of_this)) and int(self.num_of_game) != (self.num_of_this) :
                    self.open_alert()
                else:
                    messagebox.showinfo("Tic Tac Toe", "You win!")
                    if self.num_of_this <int(self.num_of_game)  :
                        self.num_of_this+=1
                        self.reset_game()
                self.label.configure(text=("You wins"))
                self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")

            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")
                if self.num_of_this <int(self.num_of_game)  :
                    self.num_of_this+=1
                    self.reset_game()
            else:
                self.current_player = self.com
                self.computer_random_move()

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text='', state="normal",fg_color="#14213d")
                self.board[i][j] = ' '
        self.current_player = self.f
        self.label.configure(text=self.current_player+" turn")
        if self.current_player==self.com and self.s_name=="AI":
                random_i = random.randint(0, 2)
                random_j = random.randint(0, 2)
                self.board[random_i][random_j] = self.com
                self.buttons[random_i][random_j].configure(text=self.com, state="disabled")
                self.label.configure(text=("your turn"))
        if self.current_player==self.com and self.s_name=="Random":
            self.label.configure(text="copmuter turn")
            self.computer_random_move()
        if self.s_name=="AI" or self.s_name=="Random":
            self.label.configure(text="your turn")

    def computer_move(self):
        best_score = float('-inf')
        best_move = None
        allmoveS=[]
        allmove=[]
        clear_frame(self.stat_frame)
        self.stat_frame.configure(fg_color="#52b788")
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.com
                    scores = self.minimax(self.board,  False)
                    score =scores[0]
                    staL = ctk.CTkLabel(self.stat_frame,text=f"score for is({i , j }) : {score} ," +" ".join(scores[1]),width=300)
                    staL.pack()
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        staL = ctk.CTkLabel(self.stat_frame,text=f"best_score is ({best_move[0] , best_move[1] }) : {best_score}" ,width=300)
        staL.pack()        
        if best_move and self.check_winner() is False:
            self.board[best_move[0]][best_move[1]] = self.com
            self.buttons[best_move[0]][best_move[1]].configure(text=self.com, state="disabled")
            self.label.configure(text=("your turn"))
            if self.check_winner()==self.com:
                messagebox.showinfo("Tic Tac Toe", "Computer wins!")
                self.p2_sccore+=1
                self.label.configure(text=("Computer wins"))
                self.p2_sccore_lable.configure(text="SCORE = "+str(self.p2_sccore))
                self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")
                if self.num_of_this <int(self.num_of_game)  :
                    self.num_of_this+=1
                    self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.label.configure(text=("TIE"))
                self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")
                if self.num_of_this <int(self.num_of_game)  :
                    self.num_of_this+=1
                    self.reset_game()
            else:
                self.current_player = self.c

    def computer_random_move(self):
        my_move = None
        move=[]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    move.append((i,j))
        my_move = random.choice(move)

        if my_move and self.check_winner() is False:
            self.board[my_move[0]][my_move[1]] = self.com
            self.buttons[my_move[0]][my_move[1]].configure(text=self.com, state="disabled")
            self.label.configure(text=("your turn"))


            if self.check_winner() ==self.com:
                self.p2_sccore+=1
                self.p2_sccore_lable.configure(text="SCORE = "+str(self.p2_sccore))

                if int(self.p2_sccore) > (int(self.num_of_game))-int((self.num_of_this)) and int(self.num_of_game) != (self.num_of_this) :
                    self.open_alert()
                else:
                    messagebox.showinfo("Tic Tac Toe", "Computer win!")
                    if self.num_of_this <int(self.num_of_game)  :
                        self.num_of_this+=1
                        self.reset_game()
                self.label.configure(text=("Computer wins"))
                self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")
            

            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")
                if self.num_of_this <int(self.num_of_game)  :
                    self.num_of_this+=1
                    self.reset_game()
            else:
                self.current_player = self.c

    def minimax(self, board, maximizing_player):
        scores = {self.com: 1, self.c: -1, 'TIE': 0}
        if self.check_winner_ai()==self.c:
            return scores[self.c],["Lose"]
        elif self.check_winner_ai()==self.com:
            return scores[self.com],["Win"]
        elif self.is_board_full():
            return scores["TIE"],["Tie"]
        if maximizing_player:
            st =[]
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = self.com
                        eval = self.minimax(board, False)
                        board[i][j] = ' '
                        max_eval = max(max_eval, eval[0])
                        for ev in eval[1]:
                            if ev not in st:
                                st.append(ev)
            return max_eval,st
        else:
            st=[]
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = self.c
                        eval = self.minimax(board,  True)
                        board[i][j] = ' '
                        min_eval = min(min_eval, eval[0])
                        for ev in eval[1]:
                            if ev not in st:
                                st.append(ev)
            return min_eval,st

    def next_turn(self,row, column): # this for two player
        if self.board[row][column] == ' ' and self.check_winner() is False:
            if self.current_player == 'X':
                self.buttons[row][column].configure(text = 'X')
                self.board[row][column] = 'X'
                if self.check_winner() is False:
                    self.label.configure(text=("O turn"))
                    self.current_player='O'
                elif self.check_winner() =='X':
                    self.p1_sccore+=1
                    self.label.configure(text=("X wins"))
                    messagebox.showinfo("Tic Tac Toe", "X win!")
                    self.p1_sccore_lable.configure(text="SCORE = "+str(self.p1_sccore))
                    self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")
                    if self.num_of_this <int(self.num_of_game)  :
                        self.num_of_this+=1
                        self.reset_game()
                elif self.is_board_full():
                    self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")                    
                    self.label.configure(text="Tie!")
                    messagebox.showinfo("Tic Tac Toe", "TIE")
                    if self.num_of_this <int(self.num_of_game) :
                        self.num_of_this+=1
                        self.reset_game()
            else:
                self.board[row][column] = 'O'
                self.buttons[row][column].configure(text = 'O')

                if self.check_winner() is False:
                    self.label.configure(text="X turn")
                    self.current_player='X'

                elif self.check_winner() =='O':
                    self.p2_sccore+=1
                    self.p2_sccore_lable.configure(text="SCORE = "+str(self.p2_sccore))
                    self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")                    
                    self.label.configure(text="O wins")
                    messagebox.showinfo("Tic Tac Toe", "O win!")
                    if self.num_of_this <int(self.num_of_game) :
                        self.num_of_this+=1
                        self.reset_game()
                elif self.is_board_full():
                    self.result.configure(text=str(self.num_of_this)+"/"+str(self.num_of_game)+" Rounds")                    
                    self.label.configure(text="Tie!")
                    messagebox.showinfo("Tic Tac Toe", "TIE")
                    if self.num_of_this <int(self.num_of_game) :
                        self.num_of_this+=1
                        self.reset_game()

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.buttons[row][0].configure(fg_color="green")
                self.buttons[row][1].configure(fg_color="green")
                self.buttons[row][2].configure(fg_color="green")
                return self.board[row][0]
        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != " ":
                self.buttons[0][column].configure(fg_color="green")
                self.buttons[1][column].configure(fg_color="green")
                self.buttons[2][column].configure(fg_color="green")
                return self.board[0][column]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]!= " ":
            self.buttons[0][0].configure(fg_color="green")
            self.buttons[1][1].configure(fg_color="green")
            self.buttons[2][2].configure(fg_color="green")
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.buttons[0][2].configure(fg_color="green")
            self.buttons[1][1].configure(fg_color="green")
            self.buttons[2][0].configure(fg_color="green")
            return self.board[0][2]
        elif self.is_board_full():
            for row in range(3):
                for column in range(3):
                    self.buttons[row][column].configure(fg_color="yellow")
            return "Tie"
        else:
            return False

    def check_winner_ai(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                return self.board[row][0]
        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != " ":
                return self.board[0][column]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]!= " ":
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        elif self.is_board_full():
            return "Tie"
        else:
            return False

    def run(self):
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j] = ctk.CTkButton(self.frame, text='', font=('normal', 24), width=150, height=150,fg_color="#14213d",
                                                command=lambda row=i, col=j: self.make_move(row, col))
                    self.buttons[i][j].grid(row=i, column=j)        
            if self.current_player!=self.c:
                random_i = random.randint(0, 2)
                random_j = random.randint(0, 2)
                self.board[random_i][random_j] = self.com
                self.buttons[random_i][random_j].configure(text=self.com, state="disabled")
                self.label.configure(text=("your turn"))
            self.root.state('zoomed')  #make screen full
            self.root.mainloop()

    def run_p(self):
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j] = ctk.CTkButton(self.frame, text='', font=('normal', 24), width=150, height=150,fg_color="#14213d",
                                     command=lambda row=i, col=j: self.next_turn(row, col))
                    self.buttons[i][j].grid(row=i, column=j) 
            self.root.state('zoomed')  #make screen full  
            self.root.mainloop()        

    def open_alert(self):
        def coun():
            self.num_of_this+=1
            self.reset_game()
            top.destroy()
        def end():
            top.destroy()
        top = tk.Toplevel()  # create window if its None or destroye
        top.geometry("600x300+630+200")
        top.title("Tic Tac Toe")
        thWiner=self.f_name
        if int(self.p2_sccore) > int(self.p1_sccore):
            thWiner=self.s_name
        if thWiner=="":
            thWiner="You"    
        label = ctk.CTkLabel(top, text=f"The Game Decided By { thWiner } ,want Continue or End ?")
        label.place(x=60,y=50)
        coun_btn = ctk.CTkButton(top, text="Continue", font=('consolas', 24), command=coun)
        coun_btn.place(x=30, y=100)
        end_btn = ctk.CTkButton(top, text="End", font=('consolas', 24), command=end,fg_color="#99582a")
        end_btn.place(x=230, y=100)
        top.mainloop()

    def run_random(self):
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j] = ctk.CTkButton(self.frame, text='', font=('normal', 24), width=150, height=150,fg_color="#14213d",
                    command=lambda row=i, col=j: self.random_move(row, col))
                    self.buttons[i][j].grid(row=i, column=j)   
            if self.current_player!=self.c:
                self.computer_random_move()   
            self.root.state('zoomed')  #make screen full
            self.root.mainloop() 

if __name__ == "__main__":
    tic_tac_toe = TicTacToeGUI()
    tic_tac_toe.run()


