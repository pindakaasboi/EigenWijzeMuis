import random
import time
import pyautogui
from tkinter import messagebox
import webbrowser

pyautogui.FAILSAFE = False

class EigenwijzeMuis:
    def __init__(self, naam):
        self.naam = naam
        self.schermbreedte, self.schermlengte = pyautogui.size()

    def beweeg(self, dx, dy):
        nieuwe_x = min(max(0, pyautogui.position()[0] + dx), self.schermbreedte)
        nieuwe_y = min(max(0, pyautogui.position()[1] + dy), self.schermlengte)
        pyautogui.moveTo(nieuwe_x, nieuwe_y, duration=0.25)
        print(f"{self.naam} beweegt naar ({nieuwe_x}, {nieuwe_y})")

    def willekeurige_beweging(self):
        while True:
            dx = random.randint(-200, 200)
            dy = random.randint(-200, 200)
            self.beweeg(dx, dy)
            random_tijd = random.randint(0, 1)
            time.sleep(random_tijd)  # Wacht random tijd tussen de bewegingen

            # Kans op klikken
            if random.random() < 0.2:
                pyautogui.click()
                print(f"{self.naam} klikt op ({pyautogui.position()[0]}, {pyautogui.position()[1]})")

            # Kans op typen
            if random.random() < 0.1:
                zinnen = [
                    "Hallo, ik ben een eigenwijze muis!",
                    "Ik hou ervan om over het scherm te zwerven.",
                    "Mijn favoriete kleur is gatenkaas.",
                    "Soms wil ik gewoon YouTube kijken",
                    "Muis zijn is niet altijd even makkelijk, snap je?"
                ]
                zin = random.choice(zinnen)
                pyautogui.press("enter")
                pyautogui.typewrite(zin, interval=0.1)
                pyautogui.press("enter")
                print(f"{self.naam} typt: {zin}")

            # Kans op het openen van een browser en een website bezoeken
            if random.random() < 0.05:
                websites = [
                    "https://www.google.com",
                    "https://www.youtube.com",
                    "https://www.spotify.com",
                    "https://www.amazon.com"
                ]
                website = random.choice(websites)
                webbrowser.open(website)
                print(f"{self.naam} opent website: {website}")

# Testen van de muisklasse
if __name__ == "__main__":
    muis = EigenwijzeMuis("Muis")
    try:
        muis.willekeurige_beweging()
    except KeyboardInterrupt:
        print("\nProgramma gestopt door gebruiker.")
    finally:
        # Voer "boze" bewegingen uit als het programma wordt gestopt
        for _ in range(30):
            muis.beweeg(random.randint(-100, 100), random.randint(-100, 100))
