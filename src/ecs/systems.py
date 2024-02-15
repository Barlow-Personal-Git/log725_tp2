from src.ecs.components import AudioComponent
import pygame.mixer

class AudioSystem:
    def __init__(self):
        pygame.mixer.init()

    def process(self, entities):
        for entity in entities:
            if entity.has_component(AudioComponent):
                audio_component = entity.get_component(AudioComponent)
                pygame.mixer.Channel(0).play(audio_component.sound, loops=-1, maxtime= 0, fade_ms= 0)
                pygame.mixer.Channel(0).set_volume(0.5)
