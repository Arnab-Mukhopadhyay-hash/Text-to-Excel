
from pygame import mixer
from datetime import datetime
from time import time

# function to play the music on loop
def playonloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
# while is required since we need to play the whole music till something is entered
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

# this is to make a file where we will save the time stamps and the messages of the works done
def log(msg):
    with open("mylog.txt", "a") as file:
        file.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # playonloop("Eyes.mp3", "stop")
    init_water = time()     # this stores the present time in the variable
    init_eyes = time()      # same as before
    init_exercise = time()  # same as before

    watersec = 5    # this is the time interval
    eyesec = 3
    exesec = 4

    while True:
        if time() - init_water > watersec:
            print("Drank to stop: ")
            playonloop("DrinkWater.mp3", "Drank")
            log("Drank water : ")
            init_water = time()

        if time() - init_exercise > exesec:
            print("ExDone to stop: ")
            playonloop("Workout.mp3", "ExDone")
            log("Physical activity : ")
            init_exercise = time()

        if time() - init_eyes > eyesec:
            print("EyDone to stop: ")
            playonloop("Eyes.mp3", "EyDone")
            log("Slept at : ")
            init_eyes = time()
