import pygame
import math
class vectors:
    def __init__(self, speed, ang):
        
        self.speed = speed
        self.ang = ang
        self.iniAng = ang
    def update(self):
        self.ang = (self.ang+self.speed) %360

    def ini(self, x1, y1, x2, y2, colorC, screen):
        self.x2 = x2
        self.x1 = x1
        self.y2 = y2
        self.y1 = y1
        self.startpoint = [self.x1, self.y1]
        self.endpoint = [self.x2, self.y2]
        
        
        
    def rotate(self, screen, Color, colorC):
        if self.x2 == 0:
            pass
        else:
            try:
                pygame.draw.circle(screen, colorC, (int(self.startpoint[0]), int(self.startpoint[1])),int(abs(self.x2)), 1)
            except ValueError:
                pass
        self.endpoint = [self.x2*math.cos(math.pi*self.ang/180), self.x2*math.sin(math.pi*self.ang/180)]
        self.current_endpoint = [self.endpoint[0]+self.startpoint[0], self.startpoint[1]+self.endpoint[1]]
        pygame.draw.line(screen, Color, self.startpoint, self.current_endpoint, 2)


