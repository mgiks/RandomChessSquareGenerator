import random
import keyboard
import os
import gtts
from time import sleep

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

while True:
    if keyboard.read_key() == "`":
        square = f"{random.choice(letters)}-{random.choice(numbers)}"
        os.system('cls')
        print()
        sleep(0.1)
        print(square)
     
        output = gtts.gTTS(text=square, lang="en", slow=False)

        output.save("output.mp3") 

        os.system("start output.mp3") 



