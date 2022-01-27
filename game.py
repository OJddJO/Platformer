from kandinsky import fill_rect as fRect,draw_string as dStr,get_pixel as gColor,set_pixel as pixel
from ion import *
from random import *
from time import *

SW,SH=320,222
GW,GH=150,192

x,y=30,100
pf_col=[(70,70,255),(0,0,0)]

class GameEngine:
  def init():
    fRect(0,0,SW,SH,'black')
    fRect(10,10,GW,GH,'white')
    return True
  def quit():
    if keydown(KEY_ZERO):
      return False

class Entity:
  def player():
    for L in range(10):
      for l in range(10):
        pixel(x+l,y+L,'red')
    def mvmt():
      global x,y
      def gravity():
        global x,y
        def grounded():
          global x,y
          for i in range(10):
            test=gColor(x+i,y+10)
            if test==pf_col[1]:
              return True
        if grounded():
          yVel=0
        else:
          yVel=-1
          for i in range(abs(yVel)):
            for g in range(10):
              pixel(x+g,y-i,'white')
        return yVel
      if keydown(KEY_LEFT):
        x-=1
        for i in range(10):
          pixel(x+11,i,'white')
      if keydown(KEY_RIGHT):
        x+=1
        for i in range(10):
          pixel(x-1,i,'white')
      yVel = gravity()
      y-=yVel
    mvmt()
  class plateform:
    pass
run=GameEngine.init()

while run:
  Entity.player()
  GameEngine.quit()
