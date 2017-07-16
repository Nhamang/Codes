import tkinter as tk

class RPSLS(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_start()

    def singleName():
        self.pack_forget()
        self.player1Name = tk.Entry(self, text="Player 1").pack()

    def multiName(self):
        pack_forget()
        self.player1Name = tk.Entry(self, text="Player 1").pack()
        self.player2Name = tk.Entry(self, text="Player 2").pack()
        
    def create_start(self):
        self.singlePlayer = tk.Button(self, command=self.singleName(), text="P1", height="5", width ="15").pack(side="left")
        self.multiPlayer = tk.Button(self, command=self.multiName(), text="P2", height="5", width="15").pack(side="right")

        



root = tk.Tk()
root.title("RPSLS game type")
root.geometry("300x50")
game = RPSLS(master=root)
game.mainloop()
