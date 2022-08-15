import pygame
from pygame.locals import *
import time
import random


class Scene():
    def __init__(self, name):
        self.objs = []
        self.name = name
        i = 0
        while (i < len(self.objs) and i + 1 < len(self.objs)):
            if self.objs[i].z_index > self.objs[i + 1].z_index:
                temp = self.objs[i]
                self.objs[i] = self.objs[i + 1]
                self.objs[i + 1] = temp
            i = i + 1

    def add_object(self, obj):
        self.objs.append(obj)
       
class GameObject():
    def __init__(self, Name, position, sprite, width_height=None, z_index=1):
        self.name = Name
        self.position = list(position)
        self.sprite = pygame.image.load(sprite)
        self.width_height = width_height
        self.z_index = z_index
        if (self.width_height != None):
            self.sprite = pygame.transform.scale(self.sprite, self.width_height)
        else:
            self.width_height = (self.sprite.get_width() , self.sprite.get_height())
        
    def translate(self, vector):
        self.position[0] = self.position[0] + vector[0]
        self.position[1] = self.position[1] + vector[1]
    
    def kill(self, map):
        map.objs.remove(self.name)
    

class Cr_Window():
    def __init__(self, window_h, window_w):
        self.window_h = window_h
        self.window_w = window_w
        self.wn = pygame.display.set_mode((self.window_h, self.window_w))

    def set_window(self, caption="myGame"):
        pygame.display.set_caption(caption)

    def update(self, scene):
        self.wn.fill((0, 0, 0))
        for obj in scene.objs:
            self.wn.blit(obj.sprite, obj.position)
            pygame.display.update()
        