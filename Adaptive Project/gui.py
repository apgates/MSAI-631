import tkinter as tk
from pet import Pet

class PetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Pet")

        self.pet = Pet("Buddy")

        self.status_label = tk.Label(root, text="Welcome to Virtual Pet!")
        self.status_label.pack()

        self.feed_button = tk.Button(root, text="Feed", command=self.feed_pet)
        self.feed_button.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play_with_pet)
        self.play_button.pack()

        self.rest_button = tk.Button(root, text="Rest", command=self.rest_pet)
        self.rest_button.pack()

        self.mood_button = tk.Button(root, text="Check Mood", command=self.check_mood)
        self.mood_button.pack()

    def feed_pet(self):
        self.pet.feed()
        self.update_status("You fed the pet.")

    def play_with_pet(self):
        self.pet.play()
        self.update_status("You played with the pet.")

    def rest_pet(self):
        self.pet.rest()
        self.update_status("The pet is resting.")

    def check_mood(self):
        mood = self.pet.mood()
        self.update_status(mood)

    def update_status(self, message):
        self.status_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PetApp(root)
    root.mainloop()
