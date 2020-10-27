import tkinter as tk
import time
import threading
global autoXP, manualXP, roundTitle, button
from google.cloud import vision
import re
import pyautogui
global autoXPIsOn
autoXPIsOn = False



def getRoundsToPlay():

    pyautogui.screenshot('energyCount.png', region=(x + 286, y + 430, 45, 32))  # Get a screenshot of the the current elixer count using coorinants relative to the game boundaries.
    pyautogui.screenshot('energyCost.png', region=(x + 494, y + 380, 36, 24))  # Get a screenshot of the the energy cost using coorinants relative to the game boundaries.
    energyCount = detect_text("energyCount.png")
    energyCost = detect_text("energyCost.png")
    return int(energyCount / energyCost)


def detect_text(path):
    """Detects text in the file."""

    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations




    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return int(re.search(r'\d+', texts[0].description).group())


def playRounds():
    time.sleep(0.5)
    pyautogui.click(x + 121, y + 189)  # click on unicorn way
    time.sleep(0.5)
    pyautogui.click(x + 500, y + 430)  # click play button
    time.sleep(0.5)

    skipButton = pyautogui.pixel(int(x + 215), int(y + 459))
    while skipButton[0] != 158 and skipButton[1] != 20 and skipButton[2] != 20:  # wait for the pixel color to be red to indicate that the skip button is on screen
        time.sleep(0.1)
        skipButton = pyautogui.pixel(int(x + 215), int(y + 459))

    pyautogui.click(x + 215, y + 459)  # click on the skip button
    time.sleep(0.5)
    pyautogui.click(x + 398, y + 254)  # click confirm skip
    time.sleep(0.5)
    pyautogui.click(x + 278, y + 254)  # click to place pet
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click(x + 241, y + 214)  # click on space to place first tower
    time.sleep(0.5)
    pyautogui.click(x + 322, y + 169)  # click to buy the first avalon tower
    time.sleep(0.5)
    pyautogui.click(x + 241, y + 214)  # click on space to select first avalon tower
    time.sleep(0.5)
    pyautogui.click(x + 236, y + 162)  # click to upgrade the first avalon tower
    time.sleep(0.5)
    pyautogui.click(x + 269, y + 310)  # click on space to place second tower
    time.sleep(0.5)
    pyautogui.click(x + 351, y + 260)  # click to buy the second avalon tower
    time.sleep(0.5)
    pyautogui.click(x + 269, y + 310)  # click on space to select second avalon tower
    time.sleep(0.5)
    pyautogui.click(x + 270, y + 258)  # click to upgrade the second avalon tower
    time.sleep(0.5)
    pyautogui.click(x + 602, y + 439)  # click on the GO button
    time.sleep(0.5)
    pyautogui.click(x + 567, y + 19)  # click fast forward

    skipButton = pyautogui.pixel(int(x + 586), int(y + 459))
    while skipButton[0] != 105 and skipButton[1] != 202 and skipButton[2] != 10:  # wait for the pixel color to be green to indicate that the next button is on screen
        time.sleep(0.1)
        skipButton = pyautogui.pixel(int(x + 586), int(y + 459))

    pyautogui.click(x + 586, y + 459)  # click next button
    time.sleep(0.7)
    skipButton = pyautogui.pixel(int(x + 179), int(y + 270))
    while skipButton[0] != 13 and skipButton[1] != 116 and skipButton[2] != 183:  # wait for the pixel color to be blue to indicate that the feed pet button is on screen
        time.sleep(0.1)
        skipButton = pyautogui.pixel(int(x + 179), int(y + 270))
    time.sleep(0.5)
    pyautogui.click(x + 179, y + 270)  # click feed pet button

    skipButton = pyautogui.pixel(int(x + 317), int(y + 415))
    while skipButton[0] != 142 and skipButton[1] != 29 and skipButton[2] != 229:  # wait for the pixel color to be purple to indicate that pet snacks are on screen
        time.sleep(0.1)
        skipButton = pyautogui.pixel(int(x + 317), int(y + 415))

    pyautogui.click(x + 112, y + 226)  # click on the first pet snack (highest tier)
    time.sleep(0.5)
    pyautogui.click(x + 317, y + 415)  # click on the select button

    skipButton = pyautogui.pixel(int(x + 483), int(y + 421))
    while skipButton[0] != 103 and skipButton[1] != 204 and skipButton[2] != 10:  # wait for the pixel color to be green to indicate the play button is on screen
        time.sleep(0.1)
        skipButton = pyautogui.pixel(int(x + 483), int(y + 421))

    pyautogui.click(x + 483, y + 421)  # click on the play button
    pyautogui.moveTo(x,y)
    time.sleep(1)




def startThread(amountOfRuns):
    if autoXPIsOn == False:
        roundsToPlay = amountOfRuns.get()
        if roundsToPlay != "" and roundsToPlay != None and roundsToPlay != " ":
            button.config(state=tk.DISABLED)
            t = threading.Thread(target=lambda: startGame(amountOfRuns))
            t.daemon = True
            t.start()
    else:
        button.config(state=tk.DISABLED)
        t = threading.Thread(target=lambda: startGame(amountOfRuns))
        t.daemon = True
        t.start()



def startGame(amountOfRuns):
    global x, y

    time.sleep(1)

    chromeLocation = pyautogui.locateCenterOnScreen('../../Desktop/GrubXPImages/chromeUnfocused.jpg',
                                                    confidence=0.94)

    if chromeLocation != None:
        pyautogui.moveTo(chromeLocation)
        pyautogui.click()
        time.sleep(1)

    findGrubOnScreen = pyautogui.locateOnScreen('../../Desktop/GrubXPImages/grubLevelSelect.jpg',
                                                confidence=0.9)

    if findGrubOnScreen == None:
        return

    x = findGrubOnScreen[0]
    y = findGrubOnScreen[1]

    if autoXPIsOn == True:
        roundsToPlay = getRoundsToPlay()
    else:
        roundsToPlay = int(amountOfRuns.get())
    if roundsToPlay > 0:



        for i in range(roundsToPlay):
            roundTitle.config(text="Round: " + str(i + 1) + " / " + str(roundsToPlay))

            playRounds()

        button.config(state=tk.NORMAL)



def switchToAutomatic(entryToChange):
    global autoXPIsOn
    entryToChange.config(state=tk.DISABLED)
    autoXPIsOn = True

def switchToManual(entryToChange):
    global autoXPIsOn
    entryToChange.config(state=tk.NORMAL)
    autoXPIsOn = False

r = tk.Tk()
r.geometry("500x500")
r.config(background='#34b518')
r.title('Grub Guardian Bot')
mainTitle = tk.Label(r, text="Grub Guardian XP Tool", font='Helvetica 18 bold', fg='#0059b3', bg="#34b518")
roundTitle = tk.Label(r, text="Round: 0 / 0", font='Helvetica 14 bold', fg='#fc9d03', bg="#34b518")
autoXP = tk.Radiobutton(r, text="Automatic Mode", value=1, command=lambda: switchToAutomatic(runAmount), bg="#34b518", font='Helvetica 12')
manualXP = tk.Radiobutton(r, text="Manual Mode", value=2, command=lambda: switchToManual(runAmount), bg="#34b518", font='Helvetica 12')
roundTitle.place(x=190, y=80)
mainTitle.place(x=110,y=50)
autoXP.place(x=120, y=150)
manualXP.place(x=270, y=150)
runAmount = tk.Entry(r, width=20)
runAmount.place(x=300, y=227)
runLabel = tk.Label(r, text="# of runs:", font='Helvetica 10', bg="#34b518")
runLabel.place(x=240, y=225)
button = tk.Button(r, text='Start', width=25, command=lambda: startThread(runAmount))
button.place(x=165, y=300)




r.mainloop()
