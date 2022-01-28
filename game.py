from kandinsky import fill_rect as fRect,draw_string as dStr,get_pixel as gColor,set_pixel as pixel
from ion import *
from random import *
from time import *

SW,SH=320,222
GW,GH=300,200

x,y,yVel,t=50,100,0,15
pf_col=[(70,70,255),(0,0,0)]
rTime,rMax=5,5

lvl=[[(10,150,20,40,pf_col[1])]]

class GameEngine:
  def init():
    fRect(0,0,SW,SH,pf_col[1])
    fRect(10,10,GW,GH,'gray')
    return True
  def quit():
    if keydown(KEY_ZERO):fRect(0,0,SW,SH,'black');return False
    else:return True
  def refresh():
    global rTime,rMax
    if rTime==0:fRect(10,10,GW,GH,'gray');rTime=rMax
    else:rTime-=1
  def pause():
    if keydown(KEY_BACKSPACE):
      p=True;sleep(0.2)
      while p:
        if keydown(KEY_BACKSPACE):
          p=False
          sleep(0.5)
class Entity:
  def player():
    for L in range(10):
      for l in range(10):
        pixel(x+l,y+L,'purple')
    def mvmt():
      global x,y
      def grounded():
        for i in range(10):
          test=gColor(x+i,y+10)
          if test==pf_col[1]:return True
      def gravity():
        global y,yVel,t
        if not grounded():
          if yVel>-5:
            if t==0:yVel-=1;t=15
            else:t-=1
          for s in range(abs(yVel)):
            for i in range(10):
              pixel(x+i,y-s,'gray')
          for s in range(2):
            for i in range(10):
              pixel(x+i,y+10+s,'gray')
        else:yVel=0
        return yVel
      def jump():
        global y,yVel
        if keydown(KEY_OK):
          if grounded():
            y-=5;yVel=2
      def colision(key):
        if key=="R":test=gColor(x+10,y)
        if key=="L":test=gColor(x-1,y)
        if test==pf_col[1]:return True
      if keydown(KEY_LEFT):
        if not colision("L"):
          x-=1
          for i in range(10):
            pixel(x+10,y+i,'gray')
      elif keydown(KEY_RIGHT):
        if not colision("R"):
          x+=1
          for i in range(10):
            pixel(x-1,y+i,'gray')
      jump()
      yVel=gravity()
      y-=yVel
    mvmt()
  def platform():
    def hitbox():
      pass


run=GameEngine.init()

while run:
  GameEngine.pause()
  GameEngine.refresh()
  Entity.player()
  run=GameEngine.quit()