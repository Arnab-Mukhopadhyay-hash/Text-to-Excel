"""
Reminder for:
- To drink a total of 3.5 l water after some time interval between 9-5pm.
- To do eye exercise after every 30 mins.
- To perform physical activity after every 45 minutes.

pygame module to play audio

audio played till the programmer enters the input which implies the he has done the task.

For Water, the user should enter "Drank"
For Eye Exercise, the user should enter "EyDone"
For Physical Exercise, the user should enter "ExDone"

"""
import pygame
import time


def playDrinkingWater():
    time.sleep(5)   # 3600 sec
    print("Drink 500ml of water, enter Drank to stop the sound: ")
    pygame.mixer.init()
    pygame.mixer.music.load('DrinkWater.mp3')
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

    while True:
        a = input()
        if a == "Drank":
            pygame.mixer.music.stop()


def playExercise():
    time.sleep(3)   # 1800 sec
    print("Do some physical activity, enter ExDone to stop the music: ")
    pygame.mixer.init()
    pygame.mixer.music.load('Eyes.mp3')
    pygame.mixer.music.play()

    while True:
        a = input()
        if a == "ExDone":
            pygame.mixer.music.stop()


def playEyes():
    time.sleep(4.5)     # 1500 sec
    print("Do some eye exercise, enter EyDone to stop the music: ")
    pygame.mixer.init()
    pygame.mixer.music.load('Workout.mp3')
    pygame.mixer.music.play()

    while True:
        a = input()
        if a == "ExDone":
            pygame.mixer.music.stop()


# localtime = time.localtime()
# var = time.strftime("%I:%M:%S %p", localtime)

while True:
    # if var == "09:00:00 PM":
    #     break
    playDrinkingWater()
    playEyes()
    playExercise()



