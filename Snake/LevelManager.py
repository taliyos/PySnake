import pygame
from pygame.locals import *
import colors
from Levels import *
import random

class LevelManager(object):
    def __init__(this, _screen, _eventHandler):
        this.screen = _screen
        this.currentLevel = 0
        this.eventHandler = _eventHandler
        this.levelList = Levels(this.screen,this.eventHandler)
        this.Level1 = Level1(this.screen, this.eventHandler, False, this)
        this.ID = random.random()
        this.previousLevel = 0;
    def Level0(this):
        if (this.previousLevel == 1):
            this.Level1.__init__(this.screen,this.eventHandler,False,this)
        this.levelList.MainMenu(this)
        
    def Update(this):
        #print(this.currentLevel)
        #print(this.ID)
        #print(this.currentLevel)
        if (this.currentLevel == 0):
            this.Level0()
            #print("MENU")
        elif (this.currentLevel == 1):
            this.Level1.Update()
            #print("GAME")

