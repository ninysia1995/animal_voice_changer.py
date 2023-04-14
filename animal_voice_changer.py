import pygame
from pydub import AudioSegment
from pydub.playback import play

def animal_voice_changer(animal, speed, volume):
    animal_sounds = {"cat": "cat.wav", "dog": "dog.wav", "cow": "cow.wav", "rooster": "rooster.wav"}
    sound = AudioSegment.from_wav(animal_sounds[animal])
    sound = sound.speedup(playback_speed=speed)
    sound = sound + volume
    play(sound)

animal_voice_changer("cat", 1.5, 5)
