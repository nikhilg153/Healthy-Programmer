#Healthy programmer
# Pygame module to play audio from pygame import mixer
from pygame import mixer
from datetime import datetime
from time import time

def audioloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exerxise = time()
    watersec = 45
    eyesec = 30
    physec = 50

    while True:
        if time() - init_water > watersec:
            print("Time for drinking water.Enter drank to stop the alarm\n")
            audioloop("water.mp3", "drank")
            init_water = time()
            log("Water drank at")

        if time() - init_eyes > eyesec:
            print("Time to do eye exercise.Enter done to stop the alarm\n")
            audioloop("eyes.mp3", "done")
            init_eyes = time()
            log("Eye exercise done at")

        if time() - init_exerxise > physec:
            print("Time to do physical exercise.Enter exdone to stop the alarm\n")
            audioloop("water.mp3", "exdone")
            init_exerxise = time()
            log("Physical exercise done  at")


