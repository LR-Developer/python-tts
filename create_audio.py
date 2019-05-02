from gtts import gTTS

import pygame

def create_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/olokinho.mp3')

    olokinho = 'audios/olokinho.mp3'

    pygame.mixer.init(24000)
    pygame.init()

    pygame.mixer.music.load(olokinho)
    pygame.mixer.music.play(-1)
    pygame.event.wait()

create_audio('olokinho meu')