# import tkinter as tk
# import random
# import time

# class ClickGame:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Basip oyna")
        
#         self.score = 0
#         self.time_left = 30

#         self.label = tk.Label(master, text="Waqit ozi 30 sekunt")
#         self.label.pack()

#         self.score_label = tk.Label(master, text="Ball: 0")
#         self.score_label.pack()

#         self.button = tk.Button(master, text="Bos!", command=self.increment_score)
#         self.button.pack(pady=20)

#         self.start_game()

#     def start_game(self):
#         self.score = 0
#         self.time_left = 10
#         self.update_timer()
#         self.button['state'] = 'normal'
#         self.button['text'] = "Bas!"
#         self.update_score()

#     def update_timer(self):
#         if self.time_left > 0:
#             self.label.config(text=f"waqit: {self.time_left} sekunt")
#             self.time_left -= 1
#             self.master.after(1000, self.update_timer)
#         else:
#             self.label.config(text="Waqit tawsildi!")
#             self.button['state'] = 'disabled'

#     def increment_score(self):
#         self.score += 1
#         self.update_score()


#     def update_score(self):
#         self.score_label.config(text=f"Ball: {self.score}")

#     def move_button(self):
#         x = random.randint(0, 300)
#         y = random.randint(0, 200)
#         self.button.place(x=x, y=y)

# if  __name__== "__main__":
#     root = tk.Tk()
#     game = ClickGame(root)
#     root.mainloop()