import pygame
from pygame.locals import *
import time
import random

class Scene():
    def __init__(self, name):
        self.objs = []
        self.name = name
        self.gforce = 10
        
    def add_object(self, obj):
        self.objs.append(obj)
        self.objs.sort(key=lambda object : object.z_index)
       
class GameObject():
    def __init__(self, Name, position, sprite, width_height=None, z_index=1):
        self.name = Name
        self.position = list(position)
        self.sprite = pygame.image.load(sprite)
        self.width_height = width_height
        self.z_index = z_index
        self.script = None
        self.components = {"Static" : 0, "Dynamic" : 0}
        if (self.width_height != None):
            self.sprite = pygame.transform.scale(self.sprite, self.width_height)
        else:
            self.width_height = (self.sprite.get_width() , self.sprite.get_height())
        self.borders = (self.width_height[0] + self.position[0], self.width_height[1] + self.position[1])
        
    def translate(self, vector):
        self.position[0] = self.position[0] + vector[0]
        self.position[1] = self.position[1] + vector[1]
    
    def kill(self, map):
        map.objs.remove(self.name)

    def script_run(self):
        if self.script != None:
            self.script(self)    

class Engine():
    def __init__(self, window_h, window_w, delay=50, caption="myGame"):
        self.window_h = window_h
        self.window_w = window_w
        self.delay = delay
        self.clock = pygame.time.Clock()
        self.wn = pygame.display.set_mode((self.window_h, self.window_w))
        pygame.display.set_caption(caption)

    def render(self, scene):
        self.wn.fill((0, 0, 0))
        for obj in scene.objs:
            self.wn.blit(obj.sprite, obj.position)
        pygame.display.update()

    def calls(self, scene):
        for ob in scene.objs:
            ob.script_run()
    
    def _is_collision(self, obj1, obj2):
        if (obj2.components["Static"] == 0 and obj2.components["Dynamic"] == 0 ):
            return 0
        if (obj1.components["Static"] == 0 and obj1.components["Dynamic"] == 0 ):
            return 0
        first_ob1 = (obj1.position[0], obj1.position[1])
        first_ob2 = (obj2.position[0], obj2.position[1])
        if first_ob2[0] > first_ob1[0] > obj1.borders[0]:
            if first_ob2[1] > first_ob1[1] > obj1.borders[1]:
                return 1
        if first_ob1[0] > first_ob2[0] > obj2.borders[0]:
            if first_ob1[1] > first_ob2[1] > obj2.borders[1]:
                return 1
        return 0

    def physics(self, scn):
        for obj in scn.objs:
            if (obj.components["Dynamic"] == 1):
                w = obj.width_height[0]
                h = obj.width_height[1]
                for cols in scn.objs:
                    if self._is_collision(obj, cols) != 1:
                        print("Collision")
                        obj.translate((0, scn.gforce))

    def update(self, scane):
        running = True

        while running:
            self.clock.tick(self.delay)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            self.calls(scane)
            #self.physics()
            self.render(scane)
